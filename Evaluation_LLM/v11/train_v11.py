from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer, DataCollatorForLanguageModeling
from peft import get_peft_model, LoraConfig, TaskType, prepare_model_for_kbit_training
import torch

# === Settings ===
model_name = "Qwen/Qwen2.5-Coder-14B-Instruct"
data_path = "v11_500.jsonl"     #small 500 or 1000
output_dir = "./ft_lora_v11_2_500"        

# === Load tokenizer and base model ===
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    load_in_4bit=True,
    trust_remote_code=True,
    torch_dtype=torch.float16
)

# === QLoRA Preparation ===
model = prepare_model_for_kbit_training(model)
peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["c_attn", "q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM
)
model = get_peft_model(model, peft_config)

# === Load dataset ===
dataset = load_dataset("json", data_files=data_path, split="train")

# === Tokenization ===
def tokenize(example):
    prompt = f"Instruction:\n{example['instruction']}\n\nInput:\n{example['input']}\n\nResponse:"
    full_text = prompt + " " + example["output"]
    if tokenizer.eos_token:
        full_text += tokenizer.eos_token
    return tokenizer(full_text, truncation=True, padding="max_length", max_length=2048)

tokenized_dataset = dataset.map(tokenize, remove_columns=dataset.column_names)

# === Training arguments ===
training_args = TrainingArguments(
    output_dir=output_dir,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    num_train_epochs=3,
    learning_rate=2e-4,
    fp16=True,
    logging_steps=10,
    save_strategy="epoch",
    report_to="none"
)

# === Data collator ===
collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# === Trainer ===
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    data_collator=collator
)

# === Train ===
trainer.train()
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)
