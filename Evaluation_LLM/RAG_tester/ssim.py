import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from PIL import Image
import imagehash
import pandas as pd

# Config
correct_dir = "../RAG_tester/correct_plots"
results_base = "../RESULTS"
model_name = "plain_qwen_full"  # change this to any model
generated_dir = os.path.join(results_base, model_name, "plots")

# List of filenames to evaluate
example_ids = [16, 17, 18, 19, 20, 21, 24, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
total_examples = len(example_ids)

results = []
missing_ids = []

for idx in example_ids:
    correct_path = os.path.join(correct_dir, f"example{idx}.png")
    generated_path = os.path.join(generated_dir, f"plot{idx}.png")

    if not os.path.exists(correct_path) or not os.path.exists(generated_path):
        print(f"Missing file for example {idx}")
        missing_ids.append(idx)
        continue

    try:
        # Load and convert to grayscale
        correct_img = cv2.imread(correct_path, cv2.IMREAD_GRAYSCALE)
        gen_img = cv2.imread(generated_path, cv2.IMREAD_GRAYSCALE)

        if correct_img.shape != gen_img.shape:
            gen_img = cv2.resize(gen_img, (correct_img.shape[1], correct_img.shape[0]))

        # SSIM
        ssim_score = ssim(correct_img, gen_img)

        # PSNR
        psnr_score = cv2.PSNR(correct_img, gen_img)

        # Hash difference
        hash1 = imagehash.average_hash(Image.open(correct_path))
        hash2 = imagehash.average_hash(Image.open(generated_path))
        hash_diff = hash1 - hash2

        results.append({
            "example": idx,
            "SSIM": round(ssim_score, 4),
            "PSNR": round(psnr_score, 2),
            "HashDiff": hash_diff
        })
    except Exception as e:
        print(f"Error processing example {idx}: {e}")
        missing_ids.append(idx)

# Save and show full per-example results
df = pd.DataFrame(results)
df.to_csv(f"{model_name}_image_similarity_metrics.csv", index=False)

# Print individual results
print("\n--- Per-Example Metrics ---")
print(df[["example", "SSIM", "PSNR", "HashDiff"]])

# Summary stats
generated_count = len(df)
missing_count = total_examples - generated_count
print(f"\nModel: {model_name}")
print(f"Generated: {generated_count}/{total_examples}")
print(f"Missing examples: {missing_ids}")

# Unpenalized (only actual outputs)
print("\n--- Unpenalized Averages (only generated plots) ---")
print(df.drop(columns="example").mean(numeric_only=True))

# Penalized (missing = worst-case)
penalized_df = df.copy()
for idx in missing_ids:
    penalized_df.loc[len(penalized_df)] = {"example": idx, "SSIM": 0.0, "PSNR": 0.0, "HashDiff": 64}

print("\n--- Penalized Averages (missing = worst score) ---")
print(penalized_df.drop(columns="example").mean(numeric_only=True))
