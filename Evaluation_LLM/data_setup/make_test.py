#!/usr/bin/env python3
import glob, json, os

IN_DIR = "useful_geocode"
OUT    = "geocode_test_set.jsonl"

def load_json_array(path):
    """Load a file that’s a top-level JSON array of {Instruction, Input, Output} dicts."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def load_plain_text(path):
    """If JSON load fails, treat each nonblank line as an Instruction with empty I/O."""
    with open(path, encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]
    return [{"Instruction": line, "Input": "", "Output": ""} for line in lines]

with open(OUT, "w", encoding="utf-8") as out:
    for path in sorted(glob.glob(os.path.join(IN_DIR, "*_evaluation.txt"))):
        try:
            examples = load_json_array(path)
        except json.JSONDecodeError:
            examples = load_plain_text(path)
        for e in examples:
            instr = e.get("Instruction","").strip()
            inp   = e.get("Input","")
            # coerce list→string if needed
            if isinstance(inp, list):
                inp = "\n".join(str(x) for x in inp)
            inp   = inp.strip()
            outp  = e.get("Output","").strip()
            out.write(json.dumps({
                "instruction": instr,
                "input":       inp,
                "output":      outp
            }, ensure_ascii=False) + "\n")

print(f"Wrote {OUT}")
