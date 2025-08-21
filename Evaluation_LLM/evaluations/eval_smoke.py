from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch, re

# ← exact same GUIDELINES from train_smoke.py:
GUIDELINES = """Follow these rules for every example:
1. Use GeoPandas for spatial operations.
2. Always project to EPSG:3035 for Europe.
3. Wrap code in a ```python … ``` block.
4. Use fig, ax = plt.subplots(figsize=(10,10)) and pass ax=ax when plotting.
5. Save plots with plt.savefig('autonomous/autonomousGIS-main/output/plot.png').
6. Do not merge or modify shapefiles—only plot them.
7. When displaying categorical values (e.g., LC0_Desc), convert to codes and use a legend.
8. Use predicate='intersects' (not op) in any gpd.sjoin.
9. Always end your script with plt.close() after saving.
10. Don’t include any explanatory text in your output—only the code.
"""

model_id = "Qwen/Qwen2.5-Coder-14B-Instruct"
adapter_dir = "smoke_lora"

tokenizer = AutoTokenizer.from_pretrained(adapter_dir, use_fast=True)
base = AutoModelForCausalLM.from_pretrained(
    model_id,
    load_in_4bit=True, device_map="auto",
    llm_int8_enable_fp32_cpu_offload=True, torch_dtype="auto"
)
model = PeftModel.from_pretrained(base, adapter_dir)
model.eval()

# ← here we **include** GUIDELINES in the prompt
prompt = (
    GUIDELINES
    + "\n### Instruction:\n"
      "Plot all the points that have pH_CaCl2 > 6.\n"
      "### Input:\n"
      "LUCAS-SOIL-2018.csv\n"
      "### Response:\n"
)

inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=512)

raw = tokenizer.decode(outputs[0], skip_special_tokens=True)
m = re.search(r"```python\n(.*?)```", raw, re.DOTALL)
clean = f"```python\n{m.group(1).strip()}\n```" if m else raw

print(clean)
