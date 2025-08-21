# eval_compare.py
import json
import csv
import random
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
from tqdm import tqdm

TEST_FILE = "test_set.jsonl"
BASE_ID   = "Qwen/Qwen2.5-Coder-14B-Instruct"
ADAPTER   = "geocode_lora"
SAMPLE_N  = 20  # broj nasumičnih primjera za evaluaciju

# 1) load baseline
tok_base = AutoTokenizer.from_pretrained(BASE_ID, use_fast=True)
mdl_base = AutoModelForCausalLM.from_pretrained(
    BASE_ID,
    load_in_4bit=True, device_map="auto",
    llm_int8_enable_fp32_cpu_offload=True, torch_dtype="auto"
)

# 2) load fine-tuned
tok_ft = AutoTokenizer.from_pretrained(ADAPTER, use_fast=True)
base   = AutoModelForCausalLM.from_pretrained(
    BASE_ID,
    load_in_4bit=True, device_map="auto",
    llm_int8_enable_fp32_cpu_offload=True, torch_dtype="auto"
)
mdl_ft = PeftModel.from_pretrained(base, ADAPTER)
mdl_ft.eval()

def generate(model, tokenizer, instr, inp):
    prompt = f"### Instruction:\n{instr}\n### Input:\n{inp}\n### Response:\n"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    out    = model.generate(**inputs, max_new_tokens=512)
    return tokenizer.decode(out[0], skip_special_tokens=True)

# 3) učitaj sve linije i uzmi nasumični uzorak
with open(TEST_FILE, "r", encoding="utf-8") as fin:
    all_lines = fin.readlines()
sampled_lines = random.sample(all_lines, k=min(SAMPLE_N, len(all_lines)))

# 4) iterate and compare with tqdm over sample
with open("eval_results_sample.csv", "w", newline="", encoding="utf-8") as fout:
    writer = csv.writer(fout)
    writer.writerow(["instruction", "baseline", "fine_tuned"])
    for line in tqdm(sampled_lines, desc="Evaluating", unit="ex"):
        ex = json.loads(line)
        b = generate(mdl_base, tok_base, ex["instruction"], ex["input"])
        f = generate(mdl_ft,   tok_ft,   ex["instruction"], ex["input"])
        writer.writerow([ex["instruction"], b, f])

print("Saved eval_results_sample.csv")
