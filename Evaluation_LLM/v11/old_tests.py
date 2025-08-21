from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import torch

# === Load Fine-Tuned Model v9 ===
model_path = "./ft_lora_v11_small"
print("Loading fine-tuned model (v10 small)...")
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

# === Evaluation Test Cases (cleaned & improved) ===
queries = [
    # Basic spatial filters
    "Plot all points in Croatia where 'OC' is below 20.",
    "Plot all points in Austria where 'pH_CaCl2' > 5 and LC0_Desc is 'Woodland'.",

    # Europe-wide categorical filter
    "Plot all the points with LC0_Desc = Grassland in Europe.",

    # Statistical filters
    "Plot all points in Slovakia where 'K' is above its 85th percentile.",
    "Create a map of Belgium highlighting points where 'pH_H2O' is in the bottom 10 percentile.",

    # Category coloring
    "Plot all points in Poland where 'OC' > median and color them by LU_DESC.",
    "Show how land cover categories vary across France on a map.",

    # Clustering tasks (cleaned)
    "Perform KMeans clustering on TH_LAT and TH_LONG to identify 4 clusters in Europe and plot them.",
    "Perform KMeans clustering on OC and K values and plot the clusters in Spain.",

    # Custom styling and color logic
    "Plot the points in Europe with 'pH_H2O' > 4 in blue and others in red.",
    "Create a map of Italy where each point is colored by its LC0_Desc category.",

    # Europe-wide threshold plot
    "Plot all points in Europe where 'K' is below its median value.",

    # NEW additions tailored to recent improvements
    "Plot all points in Spain where 'OC' is above median and LU_DESC is 'Woodland'.",
    "Map woodland locations in Finland where pH_CaCl2 < 5.",
    "Visualize all locations in Norway where both 'K' and 'pH_H2O' are above their 70th percentile."
]

# === Run test
for i, instruction in enumerate(queries):
    print(f"\n=== Test Case {i + 1}: {instruction} ===")
    result = generate(instruction)
    print(result)
