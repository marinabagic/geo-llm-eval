import json
import traceback
import os
import matplotlib.pyplot as plt

# === USER CONFIGURATION ===
CSV_PATH = "LUCAS_with_country_info.csv"
SHAPEFILE_PATH = "natural_earth_data/ne_10m_admin_0_countries.shp"
GEO_PATH = "geo_df.gpkg"
RAG_FILE = "code_rag_snippets.json"
CODE_LOG_FILE = "executed_code_log.txt"
PLOT_OUTPUT_DIR = "plots_output"

# Ensure plot output directory exists
os.makedirs(PLOT_OUTPUT_DIR, exist_ok=True)

# Load examples
with open(RAG_FILE, "r", encoding="utf-8") as f:
    examples = json.load(f)

with open(CODE_LOG_FILE, "w", encoding="utf-8") as log_file:
    for i, ex in enumerate(examples):
        print("=" * 80)
        print(f"Example {i + 1}: {ex['question']}")
        print("=" * 80)

        # Save code snippet to log
        log_file.write(f"{'='*80}\nExample {i + 1}: {ex['question']}\n{'='*80}\n")
        log_file.write(ex["code"] + "\n\n")

        try:
            # Run the code with matplotlib in context
            local_vars = {"plt": plt}
            exec(ex["code"], {}, local_vars)

            # Save any plot generated
            fig = plt.gcf()
            if fig.get_axes():  # Only save if there is a plot
                fig_path = os.path.join(PLOT_OUTPUT_DIR, f"plot_{i + 1:02d}.png")
                fig.savefig(fig_path)
                plt.close(fig)
            print("Success")
        except Exception:
            print("Failed with error:")
            print(traceback.format_exc())

        input("Press Enter to continue to next example...")
