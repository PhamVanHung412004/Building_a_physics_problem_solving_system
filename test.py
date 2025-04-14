import re
from docx import Document
def extract_questions(text):
    question_dict = {}
    matches = re.split(r"(Câu\s+\d+[:\.])", text)
    for i in range(1, len(matches), 2):
        key = matches[i].strip().replace(":", "").replace(".", "")
        content = matches[i+1].strip()
        options = re.findall(r"([A-D])\.\s*(.*?)\s*(?=(?:[A-D]\.|$))", content, re.DOTALL)

        if options:
            question_text = re.split(r"[A-D]\.", content)[0].strip()
            question_dict[key] = {
                "question": question_text,
                "options": {opt[0]: opt[1].strip() for opt in options}
            }
        else:
            question_dict[key] = {
                "question": content.strip(),
                "options": None
            }
    return question_dict


def main():
    doc = Document("dataset/BUỔI 7 - LUYỆN TẬP DAO ĐỘNG ĐIỀU HOÀ.docx")
    full_text = "\n".join([para.text for para in doc.paragraphs])
    result = extract_questions(full_text)
    print(result)
main()