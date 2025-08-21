import os
import geopandas as gpd
import numpy as np
from math import radians
import pandas as pd

# --- CONFIGURATION ---
model_names = ["qwen_bby_5", "plain_qwen_full", "qwen_bbn_4", "qwen_norag_ft_13"]
geo_base = "geo_outputs"
correct_dir = os.path.join(geo_base, "correct")
example_ids = [16, 17, 18, 19, 20, 21, 24, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
radius_km = 10

# --- Fast Vectorized Haversine Distance (in km) ---
def haversine_distance(lat2, lon2, lat1, lon1):
    R = 6371
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2[:, None] - lat1
    dlon = lon2[:, None] - lon1
    a = np.sin(dlat / 2.0)**2 + np.cos(lat1) * np.cos(lat2[:, None]) * np.sin(dlon / 2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))
    return R * c  # shape: [len(lat2), len(lat1)]

# --- SAS Calculation ---
def compute_sas(correct_gdf, generated_gdf, radius_km):
    if correct_gdf.empty or generated_gdf.empty:
        return 0.0

    correct_gdf = correct_gdf.to_crs(epsg=4326)
    generated_gdf = generated_gdf.to_crs(epsg=4326)

    correct_coords = np.array([[p.y, p.x] for p in correct_gdf.geometry if p.is_valid])
    gen_coords = np.array([[p.y, p.x] for p in generated_gdf.geometry if p.is_valid])

    if len(correct_coords) == 0 or len(gen_coords) == 0:
        return 0.0

    lat1, lon1 = gen_coords[:, 0], gen_coords[:, 1]
    lat2, lon2 = correct_coords[:, 0], correct_coords[:, 1]

    distances = haversine_distance(lat2, lon2, lat1, lon1)
    hits = (distances <= radius_km).any(axis=1).sum()

    return min(hits / len(gen_coords), 1.0)

# --- Main Evaluation Loop ---
print(">>> Starting fast SAS evaluation")

for model in model_names:
    print(f"\n=== SAS Evaluation for Model: {model} ===")
    gen_dir = os.path.join(geo_base, f"generated_{model}")
    results = []
    missing_ids = []

    for idx in example_ids:
        print(f"→ Evaluating example {idx}...", end=" ")

        correct_path = os.path.join(correct_dir, f"example{idx}.geojson")
        generated_path = os.path.join(gen_dir, f"example{idx}.geojson")

        if not os.path.exists(correct_path) or not os.path.exists(generated_path):
            print("❌ Missing")
            missing_ids.append(idx)
            continue

        try:
            correct_gdf = gpd.read_file(correct_path)
            generated_gdf = gpd.read_file(generated_path)
            sas_score = compute_sas(correct_gdf, generated_gdf, radius_km)
            score_pct = round(sas_score * 100, 2)
            results.append({"example": idx, "SAS": score_pct})
            print(f"✅ {score_pct}%")
        except Exception as e:
            print(f"💥 Error: {e}")
            missing_ids.append(idx)

    # Save results
    df = pd.DataFrame(results)
    out_path = f"{model}_sas_scores.csv"
    df.to_csv(out_path, index=False)

    print(f"\nSaved: {out_path}")
    print(f"Generated: {len(df)}/{len(example_ids)}")
    print(f"Missing: {missing_ids}")

    # Score summary
    if not df.empty:
        unpen = round(df["SAS"].mean(), 2)
        pen = round(df["SAS"].sum() / len(example_ids), 2)
        print(f"Unpenalized SAS: {unpen}%")
        print(f"Penalized SAS: {pen}%")
    else:
        print("Unpenalized SAS: 0.0%")
        print("Penalized SAS: 0.0%")
