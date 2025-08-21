import glob, json, os

IN_DIR = "useful_geocode"
OUT = "geocode_instructions.jsonl"

def process_json_array(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def process_plain_text(path):
    with open(path, encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]
    # turn each line into a dict matching your schema
    return [{"Instruction": line, "Input": "", "Output": ""} for line in lines]

with open(OUT, "w", encoding="utf-8") as out:
    for path in sorted(glob.glob(os.path.join(IN_DIR, "*_instruction.txt"))):
        try:
            arr = process_json_array(path)
        except json.JSONDecodeError:
            arr = process_plain_text(path)
        for e in arr:
            entry = {
                "instruction": e.get("Instruction", ""),
                "input":       e.get("Input", ""),
                "output":      e.get("Output", "")
            }
            out.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(f"Wrote {OUT}")
