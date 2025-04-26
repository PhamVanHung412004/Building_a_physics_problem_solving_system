from add_path import add
add()

from package import (
    re,
    BeautifulSoup
)

# def clean_question(raw_text : str) -> tuple:
#     # Chuẩn hóa input
#     raw_text = raw_text.strip()
    
#     # Tách câu hỏi và đáp án (dựa vào \nA hoặc \\A)
#     if "\nA" in raw_text:
#         parts = raw_text.split("\nA", 1)
#     elif "\\A" in raw_text:
#         parts = raw_text.split("\\A", 1)
#     else:
#         parts = [raw_text, ""]  # Nếu không có đáp án thì để trống

#     question = parts[0].strip()
#     select = parts[1].strip()

#     # Xử lý câu hỏi: bỏ số thứ tự nếu có
#     # Ví dụ: 1. Câu hỏi, 2) Câu hỏi, 3 Câu hỏi
#     question = re.sub(r"^\d+\s*[\.\)]?\s*", "", question)
#     question = question.replace("\n", " ").strip()  # Xóa xuống dòng trong câu hỏi

#     # Xử lý đáp án
#     select = select.replace('\n', '').strip()  # Xóa hết xuống dòng cũ

#     # Thêm xuống dòng trước B., C., D. để phân chia đáp án
#     select = re.sub(r'(?=[BCD]\.)', r'\n', select)

#     # Đảm bảo bắt đầu bằng A.
#     if not select.startswith("A."):
#         select = "A. " + select

#     select = select.strip()

#     return (question, select)

def clean_question(raw_text : str) -> tuple:
    # Tách phần câu hỏi và đáp án
    if "\nA" in raw_text:
        parts = raw_text.split("\nA", 1)
    elif "\\A" in raw_text:
        parts = raw_text.split("\\A", 1)
    else:
        parts = [raw_text, ""]

    # Xử lý phần câu hỏi
    question = parts[0].strip()
    vtri = re.search(r"\d+", question)
    
    if vtri:
        question = question[vtri.end():].strip()
    question = question.replace(":", "")
    question = question.replace("\n", "").strip()

    # Xử lý phần đáp án
    select = parts[1].strip()
    select = select.replace('\n', '')
    
    select = re.sub(r'(?=[BCD]\.)', r'\n', select)
    select = select.strip()

    if not select.startswith("A."):
        select = "A" + select

    return (question, select)

def solution(string : str) -> tuple:
    oke = True
    left = -1
    right = -1
    while(oke):        
        begin = -1
        end = -1

        for i in range(len(string)):
            if (string[i] == '<' and string[i + 1 : i + 1 + 4] == "math"):
                begin = i
            if (string[i] == ">" and string[i - 4: i] == "math"):
                end = i
        
        if (begin == -1 or end == -1):
            oke = False
        else:  
            left = begin
            right = end
            string = string.replace(string[begin : end + 1], " ") 
        
    if (string[-1] == '→'):
        string = string[ : -1]

    return (left,right)

def parse_element(el):
    children = el.find_all(recursive=False)
    if el.name == "mfrac":
        if len(children) >= 2:
            numerator = parse_element(children[0])
            denominator = parse_element(children[1])
            return f"({numerator}/{denominator})"
        else:
            return ""  # Tránh lỗi nếu thiếu phần tử

    elif el.name == "mroot":
        if len(children) >= 2:
            radicand = parse_element(children[0])
            index = parse_element(children[1])
            return f"√{index}({radicand})"
        elif len(children) == 1:
            radicand = parse_element(children[0])
            return f"√({radicand})"
        else:
            return ""

    elif el.name == "msup":
        if len(children) >= 2:
            base = parse_element(children[0])
            exponent = parse_element(children[1])
            return f"{base}^{exponent}"
        else:
            return ""

    elif el.name == "msub":
        if len(children) >= 2:
            base = parse_element(children[0])
            subscript = parse_element(children[1])
            return f"{base}_{subscript}"
        else:
            return ""

    elif el.name == "msubsup":
        if len(children) >= 3:
            base = parse_element(children[0])
            subscript = parse_element(children[1])
            exponent = parse_element(children[2])
            return f"{base}_{subscript}^{exponent}"
        else:
            return ""

    elif el.name == "mo":
        return f" {el.text} "

    elif el.name in {"mi", "mn"}:
        return el.text

    elif el.name == "mrow":
        return ''.join(parse_element(child) for child in children)

    elif el.name == "mfenced":
        return f"({''.join(parse_element(child) for child in children)})"

    else:
        return ''.join(parse_element(child) for child in children)
    
def clean_mathml(mathml_string : str) -> str:
    soup = BeautifulSoup(mathml_string, "xml")
    try:     
        return parse_element(soup.math)
    except ZeroDivisionError as e:
        return mathml_string
    
def fix_spacing_and_comma(text : str) -> str:
    
    # 1. Sửa dấu phẩy giữa số thành dấu chấm (4 , 2 => 4.2)
    text = re.sub(r'(\d)\s*,\s*(\d)', r'\1.\2', text)
    
    # 2. Thêm khoảng trắng trước và sau các toán tử cơ bản (=, +, -, *, /, ^)
    text = re.sub(r'(?<=[^\s])([=+\-*/^])(?=[^\s])', r' \1 ', text)
    
    # 3. Xóa khoảng trắng thừa (nén về 1 dấu cách)
    text = re.sub(r'\s+', ' ', text)
    
    # 4. Xóa khoảng trắng sau dấu mở ngoặc hoặc trước dấu đóng ngoặc
    text = re.sub(r'\(\s+', '(', text)
    text = re.sub(r'\s+\)', ')', text)
    
    # 5. Xóa khoảng trắng ở đầu/cuối
    text = text.strip()
    return text
