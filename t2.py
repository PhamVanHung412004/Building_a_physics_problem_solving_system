import re

def clean_question(raw_text):
    # Kiểm tra và chia câu hỏi và các lựa chọn
    if "\nA" in raw_text:
        parts = raw_text.split("\nA", 1)
    elif "\A" in raw_text:
        parts = raw_text.split("\A", 1)
    else:
        parts = [raw_text, ""]

    # Lấy câu hỏi (phần trước A)
    question = parts[0].strip()

    # Loại bỏ số câu hỏi, nếu có
    vtri = re.search(r"\d+", question)
    if vtri:
        question = question[vtri.end():].strip()

    # Loại bỏ dấu "\n" trong câu hỏi
    question = question.replace("\n", " ")

    # Lấy phần lựa chọn (phần sau A)
    select = parts[1].strip()
    select = select.replace('\n', '')
    
    # Thêm dấu '\n' trước B, C, D nếu chúng có trong chuỗi lựa chọn
    select = re.sub(r'(?=\n[BCD]\.)', r'\n', select)
    

    select = select.strip()

    # Đảm bảo rằng lựa chọn bắt đầu với "A."
    if not select.startswith("A."):
        select = "A" + select

    return question, select

def main():
    # Dữ liệu ví dụ
    text = {
        "cau_hoi": "Câu 4. Một hạt bụi nhỏ có khối lượng m = 0,1 mg, nằm lơ lửng trong điện trường giữa hai bản kim loại phẳng. Các đường sức điện có phương thẳng đứng và chiều hướng từ dưới lên trên. Hiệu điện thế giữa hai bản là 120 V. Khoảng cách giữa hai bản là 1 cm. Xác định điện tích của hạt bụi. Lấy g = 10 m/s2.\nA. 8,3.10-8 C.\nB. 8,0.10-10 C.\nC. 3,8.10-11 C.\nD. 8,9.10-11 C.",
    }
    
    # Gọi hàm xử lý câu hỏi và lựa chọn
    question, select = clean_question(text["cau_hoi"])

    # In kết quả
    print("Câu hỏi: ", question)
    print("Các lựa chọn: ", select)

# Chạy chương trình
main()
