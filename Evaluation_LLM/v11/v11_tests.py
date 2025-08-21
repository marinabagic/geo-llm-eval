from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

# === Load Fine-Tuned Model v11 ===
model_path = "./ft_lora_v11_500"  # small 500 1000
print("Loading fine-tuned model (v11 500)...")
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
base_model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-Coder-14B-Instruct",
    device_map="auto",
    load_in_4bit=True,
    trust_remote_code=True,
    torch_dtype=torch.float16
)
model = PeftModel.from_pretrained(base_model, model_path)

# === Generation function ===
def generate(instruction):
    input_text = "Assume the file 'LUCAS_with_country_info.csv' is available and can be used in your code. You are familiar with its structure and contents."
    prompt = f"Instruction:\n{instruction}\n\nInput:\n{input_text}\n\nResponse:"
    inputs = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)
    with torch.no_grad():
        output = model.generate(inputs, max_new_tokens=512, do_sample=False, temperature=0.7)
    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    return decoded.split("Response:")[-1].strip()

# === Evaluation Test Cases (fresh, not in training JSONL) ===
queries = [
    "Show all points in Hungary where 'CaCO3' is greater than 10 and 'LC0_Desc' is 'Cropland'.",
    "Map the locations in Denmark where 'Ox_Fe' is above its median and 'LU1_Desc' contains 'Forest'.",
    "Plot the distribution of 'Elev' across Austria, using a color gradient from light blue to dark red.",
    "Display German samples where 'N' is above 0.3 and 'LC1_Desc' is not 'Artificial land'.",
    "Visualize European points where 'CaCO3' is less than 5 and 'LU' is equal to 211.",
    "Show all samples in Lithuania where 'TH_LAT' is greater than 55.5 and 'K' is below the 25th percentile.",
    "Plot a map of Slovenia with points colored by 'pH_CaCl2', but only for 'Shrubland' in LC1_Desc.",
    "Display points in Czech Republic where 'NUTS_2' starts with 'CZ' and 'OC' is greater than 30.",
    "Map the samples in Belgium where 'Ox_Al' is above its 90th percentile, colored by 'LC0_Desc'.",
    "Highlight all samples in Bulgaria with 'EC' greater than 0.6 and 'LU1_Desc' containing 'Crop'.",
     "Plot all samples from France where 'LC0_Desc' is 'Cropland'.",
    "Show the distribution of 'pH_H2O' in Germany using a color scale.",
    "Display all points in Italy where 'OC' is greater than 20.",
    "Plot LUCAS samples in Sweden with 'pH_CaCl2' less than 5.5.",
    "Map all locations in Finland colored by 'LU1_Desc'."
]

# === Run test
for i, instruction in enumerate(queries):
    print(f"\n=== Test Case {i + 1}: {instruction} ===")
    result = generate(instruction)
    print(result)
