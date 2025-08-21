import os
import json
import matplotlib.pyplot as plt
import traceback

# Load the JSON file
with open("test_codes.json", "r") as f:
    examples = json.load(f)

# Create output directory
os.makedirs("correct_plots", exist_ok=True)

# Execution loop
for idx, item in enumerate(examples, start=1):
    code = item.get("code", "")
    filename = f"correct_plots/example{idx}.png"
    print(f"Running example {idx}...")

    try:
        # Clear any existing figures
        plt.close("all")

        # Create a fresh namespace
        local_ns = {}

        # Run the code
        exec(code, {"__builtins__": __builtins__}, local_ns)

        # Check if a figure was created and save it
        if plt.get_fignums():
            plt.savefig(filename)
            print(f"Saved plot to {filename}")
        else:
            print("No plot generated.")
    except Exception as e:
        print(f"Error in example {idx}:\n{traceback.format_exc()}")

print("Done.")
