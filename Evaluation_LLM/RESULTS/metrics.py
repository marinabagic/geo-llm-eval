import os
import json
from difflib import SequenceMatcher
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from nltk.translate.meteor_score import meteor_score
from rouge_score import rouge_scorer
from transformers import AutoTokenizer, AutoModel
import torch
from tqdm import tqdm


# SETTINGS
GENERATED_DIR = "plain_qwen_full/generated"
REFERENCE_FILE = "test_codes.json"
EMBEDDING_MODEL_NAME = "microsoft/codebert-base"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load CodeBERT
tokenizer = AutoTokenizer.from_pretrained(EMBEDDING_MODEL_NAME)
model = AutoModel.from_pretrained(EMBEDDING_MODEL_NAME).to(DEVICE)

def embed_code(code):
    inputs = tokenizer(code, return_tensors="pt", truncation=True, padding=True, max_length=512)
    inputs = {k: v.to(DEVICE) for k, v in inputs.items()}
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings.cpu().numpy()[0]

# Load references
with open(REFERENCE_FILE, "r", encoding="utf-8") as f:
    reference_data = json.load(f)
references = [item["code"] for item in reference_data]

# Load generated outputs
hypotheses = []
for i in range(1, len(references) + 1):
    with open(os.path.join(GENERATED_DIR, f"generated_{i}.py"), "r", encoding="utf-8") as f:
        hypotheses.append(f.read().strip())

# Initialize scorers
rouge = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
smooth = SmoothingFunction().method4

# Evaluate
results = []
for ref, hyp in tqdm(zip(references, hypotheses), total=len(references)):
    bleu = sentence_bleu([ref.split()], hyp.split(), smoothing_function=smooth)
    meteor = meteor_score([ref.split()], hyp.split())
    rouge_l = rouge.score(ref, hyp)['rougeL'].fmeasure
    levenshtein = SequenceMatcher(None, ref, hyp).ratio()

    # CodeBERT embedding similarity
    try:
        emb_ref = embed_code(ref)
        emb_hyp = embed_code(hyp)
        codebert_sim = torch.nn.functional.cosine_similarity(
            torch.tensor(emb_ref), torch.tensor(emb_hyp), dim=0
        ).item()
    except Exception as e:
        print("CodeBERT error:", e)
        codebert_sim = 0.0

    results.append({
        "bleu": bleu,
        "meteor": meteor,
        "rougeL": rouge_l,
        "levenshtein": levenshtein,
        "codebert": codebert_sim,
    })

# Compute averages
avg = lambda key: sum(r[key] for r in results) / len(results)
print("\nAverage Scores:")
print(f"BLEU:        {avg('bleu'):.4f}")
print(f"METEOR:      {avg('meteor'):.4f}")
print(f"ROUGE-L:     {avg('rougeL'):.4f}")
print(f"Levenshtein: {avg('levenshtein'):.4f}")
print(f"CodeBERT:    {avg('codebert'):.4f}")
