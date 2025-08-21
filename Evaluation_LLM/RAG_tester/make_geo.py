import os
import geopandas as gpd
import traceback

# --- CONFIG ---
model_names = ["qwen_bby_5", "plain_qwen_full", "qwen_bbn_4", "qwen_norag_ft_13"]
geo_output_base = "../geo_outputs"  # saving alongside RAG_tester, same level as RESULTS
results_base = "../RESULTS"         # parent dir from RAG_tester

# Ensure output folder structure exists
os.makedirs(geo_output_base, exist_ok=True)

print("\n=== Extracting GeoDataFrames from Generated Models ===")

for model in model_names:
    gen_dir = os.path.join(results_base, model, "generated")
    out_dir = os.path.join(geo_output_base, f"generated_{model}")
    os.makedirs(out_dir, exist_ok=True)

    print(f"\n🔍 Model: {model}")

    try:
        files = sorted(os.listdir(gen_dir))
    except FileNotFoundError:
        print(f"❌ Directory not found: {gen_dir}")
        continue

    for fname in files:
        if not fname.endswith(".py"):
            continue

        try:
            example_num = int(fname.split("_")[-1].replace(".py", ""))
            full_path = os.path.join(gen_dir, fname)
            save_path = os.path.join(out_dir, f"example{example_num}.geojson")

            with open(full_path, "r") as f:
                code = f.read()

            local_ns = {}
            exec(code, {"__builtins__": __builtins__}, local_ns)

            for var in local_ns.values():
                if isinstance(var, gpd.GeoDataFrame):
                    var.to_crs(epsg=4326).to_file(save_path, driver="GeoJSON")
                    print(f"✅ Saved {model} example{example_num}.geojson")
                    break

        except Exception as e:
            print(f"❌ Error in {model} example {fname}:\n{traceback.format_exc()}")
