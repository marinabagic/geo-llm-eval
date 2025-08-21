import os
import json
import glob
from codebleu import calc_codebleu

def load_reference_codes(ref_file):
    with open(ref_file, 'r') as f:
        data = json.load(f)
    return {item['question']: item['code'] for item in data}

def load_generated_codes(gen_dir):
    generated_codes = {}
    for file_path in sorted(glob.glob(os.path.join(gen_dir, "*.py"))):
        file_name = os.path.basename(file_path)
        with open(file_path, 'r') as f:
            generated_codes[file_name] = f.read()
    return generated_codes

def evaluate_codebleu(ref_codes, gen_codes, questions):
    scores = {}
    for question in questions:
        ref_code = ref_codes.get(question, "")
        gen_file = f"generated_{questions.index(question) + 1}.py"
        gen_code = gen_codes.get(gen_file, "")
        if ref_code and gen_code:
            score = calc_codebleu([ref_code], [gen_code], lang="python")
            scores[question] = score
    return scores

def main():
    pred_dir = "plain_qwen_full/generated"  # Updated path
    ref_file = "test_codes.json"      # Updated path
    
    # Ensure paths are absolute if needed
    pred_dir = os.path.join(os.path.dirname(__file__), pred_dir)
    ref_file = os.path.join(os.path.dirname(__file__), ref_file)
    
    # Load reference and generated codes
    ref_codes = load_reference_codes(ref_file)
    gen_codes = load_generated_codes(pred_dir)
    
    # Extract questions for matching
    questions = list(ref_codes.keys())
    
    # Evaluate using CodeBLEU
    scores = evaluate_codebleu(ref_codes, gen_codes, questions)
    
    # Print results
    print("CodeBLEU Scores:")
    for question, score in scores.items():
        print(f"{question}: {score}")
    
    # Calculate and print average score
    avg_score = sum(score['codebleu'] for score in scores.values()) / len(scores) if scores else 0
    print(f"Average CodeBLEU Score: {avg_score}")

if __name__ == "__main__":
    main()