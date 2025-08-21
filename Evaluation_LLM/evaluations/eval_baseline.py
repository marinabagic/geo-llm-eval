from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import re

model_id = "Qwen/Qwen2.5-Coder-14B-Instruct"

# 1) učitaj tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True)

# 2) učitaj bazni model (4-bit kvantizacija, device_map auto)
base = AutoModelForCausalLM.from_pretrained(
    model_id,
    load_in_4bit=True,
    device_map="auto",
    llm_int8_enable_fp32_cpu_offload=True,
    torch_dtype="auto"
)
base.eval()

# 3) isti prompt
prompt = (
    "### Instruction:\n"
    "Plot all the points that have pH_CaCl2 > 6.\n"
    "### Input:\n"
    "LUCAS-SOIL-2018.csv\n"
    "### Response:\n"
)

# 4) generiraj
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
outputs = base.generate(**inputs, max_new_tokens=512)

# 5) očisti samo prvi ```python…``` blok
raw = tokenizer.decode(outputs[0], skip_special_tokens=True)
m = re.search(r"```python\n(.*?)```", raw, re.DOTALL)
if m:
    clean = "```python\n" + m.group(1).strip() + "\n```"
else:
    clean = raw

# 6) ispiši u konzolu
print(clean)
