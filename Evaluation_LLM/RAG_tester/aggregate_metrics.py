import os
import json
import pandas as pd

# Directory with individual metrics
metrics_dir = "metrics"
output_csv = "all_metrics_summary.csv"

# Load all metric files
records = []
for filename in sorted(os.listdir(metrics_dir)):
    if filename.endswith(".json"):
        path = os.path.join(metrics_dir, filename)
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            record = {
                "question_id": filename.replace("_metrics.json", ""),
                "question": data["question"],
                "bleu": data["metrics"]["bleu"],
                "meteor": data["metrics"]["meteor"],
                "rougeL": data["metrics"]["rougeL"],
                "cosine_similarity": data["metrics"]["cosine_similarity"],
                "ast_match": data["metrics"]["ast_match"],
                "levenshtein": data["metrics"]["levenshtein"]
            }
            records.append(record)

# Convert to DataFrame
df = pd.DataFrame(records)
df.to_csv(output_csv, index=False)
print(f"Aggregated metrics saved to: {output_csv}")
