# eval_verbose.py
import json, csv, random
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
from tqdm import tqdm

TEST_FILE = "test_set.jsonl"
BASE_ID   = "Qwen/Qwen2.5-Coder-14B-Instruct"
ADAPTER   = "geocode_lora"
SAMPLE_N  = 20   # ← pull a random subset to keep runtime reasonable

# 1) Load baseline
tok_base = AutoTokenizer.from_pretrained(BASE_ID, use_fast=True)
mdl_base = AutoModelForCausalLM.from_pretrained(
    BASE_ID,
    load_in_4bit=True, device_map="auto",
    llm_int8_enable_fp32_cpu_offload=True, torch_dtype="auto"
)
mdl_base.eval()

# 2) Load fine-tuned
tok_ft = AutoTokenizer.from_pretrained(ADAPTER, use_fast=True)
base   = AutoModelForCausalLM.from_pretrained(
    BASE_ID,
    load_in_4bit=True, device_map="auto",
    llm_int8_enable_fp32_cpu_offload=True, torch_dtype="auto"
)
mdl_ft = PeftModel.from_pretrained(base, ADAPTER)
mdl_ft.eval()

def generate(model, tokenizer, instr, inp, max_new_tokens=1024):
    prompt = f"### Instruction:\n{instr}\n### Input:\n{inp}\n### Response:\n"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    outs   = model.generate(**inputs, max_new_tokens=max_new_tokens)
    return tokenizer.decode(outs[0], skip_special_tokens=True).strip()

# 3) Read test set, optionally sample
with open(TEST_FILE, encoding="utf-8") as f:
    lines = f.readlines()
if SAMPLE_N and SAMPLE_N < len(lines):
    lines = random.sample(lines, SAMPLE_N)

# 4) Evaluate and write verbose CSV
with open("eval_verbose.csv", "w", newline="", encoding="utf-8") as fout:
    writer = csv.writer(fout)
    writer.writerow(["Instruction","Input","Expected","Baseline","Fine-Tuned"])
    for line in tqdm(lines, desc="Evaluating", unit="ex"):
        ex = json.loads(line)
        instr   = ex.get("instruction","").strip()
        inp     = ex.get("input","").strip()
        expected= ex.get("output","").strip()

        b_out = generate(mdl_base, tok_base, instr, inp)
        f_out = generate(mdl_ft,   tok_ft,   instr, inp)

        writer.writerow([instr, inp, expected, b_out, f_out])

print("Done! See eval_verbose.csv for side-by-side comparison.")
