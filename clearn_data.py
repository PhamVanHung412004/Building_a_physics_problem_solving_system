import json
import re

# Đọc file JSON gốc
with open("data_clean_fine_turning.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

cleaned_data = []

for item in raw_data:
    question = item["cau_hoi"].strip()

    # Xử lý đáp án
    options_raw = item["cac_dap_an"].split('\n')
    options = {}
    for line in options_raw:
        match = re.match(r"([A-D])\.\s*(.*)", line)
        if match:
            options[match.group(1)] = match.group(2).strip()

    # Tìm đáp án đúng
    correct_line = next((s for s in item["giai_thich"] if "Đáp án đúng là" in s), "")
    correct_match = re.search(r"Đáp án đúng là:?\s*([A-D])", correct_line)
    correct_answer = correct_match.group(1) if correct_match else ""

    # Gộp giải thích lại
    explanation = " ".join([line.strip() for line in item["giai_thich"]])

    cleaned_data.append({
        "question": question,
        "options": options,
        "correct_answer": correct_answer,
        "explanation": explanation
    })

# Lưu lại file JSON sạch
with open("cleaned_questions.json", "w", encoding="utf-8") as f:
    json.dump(cleaned_data, f, indent=2, ensure_ascii=False)

print(f"✅ Đã làm sạch {len(cleaned_data)} câu hỏi và lưu vào 'cleaned_questions.json'")
