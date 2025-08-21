import os
import json
import evaluate
import numpy as np
import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import Levenshtein

# Load metric modules
bleu = evaluate.load("bleu")
meteor = evaluate.load("meteor")
rouge = evaluate.load("rouge")

# Paths
json_path = "test_codes.json"
output_dir = "metrics"
os.makedirs(output_dir, exist_ok=True)

# Load JSON
with open(json_path, "r") as f:
    data = json.load(f)

# Optional: filter if needed
# data = data[:5]  # for testing a few

# --- Metric Functions ---

def compute_cosine_similarity(ref, hyp):
    vec = TfidfVectorizer().fit_transform([ref, hyp])
    return cosine_similarity(vec[0:1], vec[1:2])[0][0]

def compute_ast_match(ref, hyp):
    try:
        ref_ast = ast.dump(ast.parse(ref))
        hyp_ast = ast.dump(ast.parse(hyp))
        return int(ref_ast == hyp_ast)
    except Exception:
        return 0

def evaluate_pair(reference_code, generated_code):
    return {
        "bleu": bleu.compute(predictions=[generated_code], references=[reference_code])["bleu"],
        "meteor": meteor.compute(predictions=[generated_code], references=[reference_code])["meteor"],
        "rougeL": rouge.compute(predictions=[generated_code], references=[reference_code])["rougeL"],
        "cosine_similarity": compute_cosine_similarity(reference_code, generated_code),
        "ast_match": compute_ast_match(reference_code, generated_code),
        "levenshtein": Levenshtein.distance(reference_code, generated_code)
    }

# --- Main Evaluation Loop ---

for idx, entry in enumerate(data):
    question = entry["question"]
    reference_code = entry["code"]

    generated_code_path = f"generated/generated_{idx:02d}.py"
    if not os.path.exists(generated_code_path):
        print(f"Missing generated code for Q{idx+1}, skipping...")
        continue

    with open(generated_code_path, "r") as gf:
        generated_code = gf.read()

    metrics = evaluate_pair(reference_code, generated_code)

    # Save metrics
    result = {
        "question": question,
        "reference_code": reference_code,
        "generated_code": generated_code,
        "metrics": metrics
    }

    with open(os.path.join(output_dir, f"q{idx+1:02d}_metrics.json"), "w") as mf:
        json.dump(result, mf, indent=2)

    print(f"Evaluated Q{idx+1}: {question}")
