from add_path import add
add()

from package import (
    re,
    BeautifulSoup,
    Dict
)

def char_test(char : str):
    '''
    char : kí tự muốn kiểm tra
    '''
    return 65 <= ord(char) and ord(char) <= 65 + 32

def check_charactor(char : str):
    return chr(ord(char[0]) - 32) + '.' + char[2 : ] if (len(char) >= 2) and (97 <= ord(char[0]) and ord(char[0]) <= 122) and (char[1] == ')') else '-1'

def check_char(vector_answer : list[str]) -> bool:
    '''
    vector_answer : chứa danh sách các câu trả lời
    '''
    cnt = 0
    for i in range(len(vector_answer[1 : ])):
        char = vector_answer[i][0]
        if (char_test(char)):
            cnt += 1
            
    return True if (cnt >= 2 and cnt <= 4) else False

def check_char_index(vector_answer : list[str], char : str) -> str:
    '''
    vector_answer : chứa danh sách các câu trả lời
    char : kí tự đáp án đúng của câu đấy
    '''
    index = -1
    for i in range(len(vector_answer)):
        if (char_test(vector_answer[i][0])):
            if (vector_answer[i][0] == char):
                index = i
                break
    return vector_answer[index]

def get_char(text : str) -> str:    
    '''
    text : từng đoạn văn bản trong danh sách các câu trả lời
    '''
    for i in range(len(text) - 1, -1, -1):
        if (char_test(text[i])):
            return i
        
def index_char_true(vector : list) -> str:
    '''
    vector : chứa các danh sach câu trả lời
    '''
    index = -1    
    for i in range(len(vector)):
        if ("đúng" in vector[i][1 : ] or "Đúng" in vector[i][1 : ]):
                index = i
                break       
    return vector[index]


def convert_dict(options_raw : Dict[str , str]) -> Dict[str , str]:
    '''
    options_raw : gom dap an va noi dung dap an
    '''
    options = {}
    for line in options_raw:
        match = re.match(r"([A-D])\.\s*(.*)", line)
        if match:
            options[match.group(1)] = match.group(2).strip()

    return options

# kiểm tra xem kí tự in hoa tìm được có hợp lệ hay không
def range_char(char : str) -> bool:
    '''
    char : ki tu cua dap an dung
    '''
    table_char = ['A', 'B', 'C', 'D']    
    return char in table_char

def check_value(string : str) -> tuple:
    index = -1
    oke = False
    for i in range(len(string)):
        if (char_test(string[i])):
            index = i 
            oke = True
            break                             
    return (oke,index)

def check(options : Dict[str , str]) -> Dict[str , str]:
    '''
    options : gom dap an va noi dung cua dap an
    '''
    dict_new = {}
    for key, value in options.items():
        oke, index = check_value(value)
        if (oke and range_char(value[index])):
            title1 = value[ : index]
            dict_new[key] = title1
            dict_new[value[index]] = value[index + 1 : ]            
        else:
            dict_new[key] = value
    
    value_dict_tmp = dict(sorted(dict_new.items()))
    return value_dict_tmp


def dict_to_text(data : Dict[str, str]) -> list[str]:
    '''
    data : dap an va noi dung cua dap an
    '''
    return [key + "." + value for key, value in data.items()]

def solution(string : str) -> tuple:
    '''
    string : doan van ban dua vao
    '''
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


def clean_choice(options_raw : list[str]) -> Dict[str , str]:
    '''
    list_text : danh sach cac doan text cua dap an lua chon
    '''
    options = {}
    current_key = None
    current_text = []

    for line in options_raw:
        match = re.match(r"^([A-D])\.\s*$", line.strip())  # Chỉ chứa "A.", "B.
        if match:
            # Lưu đáp án trước đó nếu có
            if current_key is not None:
                options[current_key] = " ".join(current_text).strip()
            # Bắt đầu đáp án mới
            current_key = match.group(1)
            current_text = []
        elif current_key:
            current_text.append(line.strip())

    # Đừng quên lưu đáp án cuối cùng
    if current_key is not None:
        options[current_key] = " ".join(current_text).strip()
    return options

def parse_element(el):
    """Đệ quy parse một element MathML thành chuỗi công thức."""
    children = el.find_all(recursive=False)
    if el.name == "mfrac":
        if len(children) >= 2:
            numerator = parse_element(children[0])
            denominator = parse_element(children[1])
            return f"({numerator}/{denominator})"
        else:
            return ""

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
    
    elif el.name == "mtext":
        return el.text

    elif el.name == "mrow":
        return ''.join(parse_element(child) for child in children)

    elif el.name == "mfenced":
        return f"({''.join(parse_element(child) for child in children)})"

    else:
        return ''.join(parse_element(child) for child in children)

def clean_mathml(mathml_string: str) -> str:
    """Làm sạch MathML thành chuỗi toán học đơn giản."""
    soup = BeautifulSoup(mathml_string, "xml")
    try:
        parsed = parse_element(soup.find("math"))
        return beautify_formula(parsed)
    except Exception as e:
        # Nếu MathML lỗi thì trả lại nguyên văn
        return mathml_string

def beautify_formula(text: str) -> str:
    """Beautify spacing + sửa dấu phẩy thành dấu chấm cho số."""
    # Đổi dấu phẩy trong số thành dấu chấm
    text = re.sub(r'(\d)\s*,\s*(\d)', r'\1.\2', text)
    
    # Thêm khoảng trắng trước/sau các toán tử cơ bản
    text = re.sub(r'(?<=[^\s])([=+\-*/^])(?=[^\s])', r' \1 ', text)
    
    # Bỏ khoảng trắng thừa
    text = re.sub(r'\s+', ' ', text)
    
    # Bỏ khoảng trắng sau dấu ( hoặc trước dấu )
    text = re.sub(r'\(\s+', '(', text)
    text = re.sub(r'\s+\)', ')', text)

    return text.strip()

def extract_all_mathml(text: str) -> list:
    """Tách tất cả các đoạn <math>...</math> trong text."""
    mathmls = re.findall(r'(<math.*?</math>)', text, flags=re.DOTALL)
    return mathmls

def clean_text_with_mathml(text: str) -> str:
    """Thay tất cả các đoạn MathML trong text thành công thức đẹp."""
    mathmls = extract_all_mathml(text)
    for mathml in mathmls:
        cleaned = clean_mathml(mathml)
        text = text.replace(mathml, cleaned)
    return text

def search_index(char : str, string : str) -> str:    
    index = -1
    for i in range(len(string)):
        if (string[i] == char):
            index = i
    string = string.replace(string[index: ], "")

    return string

def check_string(string : str) -> int:
    index = -1
    for i in range(len(string)):
        if (string[i] == ':'):
            index = i
            break
    return index 

def string_seach_character(character : str, string_before : str) -> str:
    oke = False
    index_ = -1
    for i in range(len(string_before)):
        if (string_before[i] == ':'):
            oke = True
            index_ = i
    if (oke):
        return string_before[ : index_ + 1]
    else:
        index = -1
        for i in range(len(string_before)):
            if (character == string_before[i]):
                index = i
                break
        return string_before[ : index + 1]

def convert_doube_string_from_string(text : str) -> str:
    vector_text = text.split()
    text_new = " ".join(vector_text)

    vector_array = text_new.split(" ")

    set_check = set()

    vector_text_new = []

    for i in vector_array:
        if (i not in set_check):
            vector_text_new.append(i)
            set_check.add(i)

    text_beautiful = " ".join(vector_text_new)
    return text_beautiful   

def smart_clean(raw_text):
    """
    Làm sạch text và tự động thêm toán tử (*, /) hợp lý cho công thức vật lý cấp 3.
    """
    # 1. Xóa xuống dòng và khoảng trắng thừa
    text = raw_text.replace('\n', '').replace(' ', '')

    # 2. Các hàm toán học đặc biệt cần bảo toàn
    functions = ['sin', 'cos', 'tan', 'log', 'ln', 'sqrt', 'exp']
    
    # 3. Đánh dấu các hàm đặc biệt (tạm thời)
    for func in functions:
        text = re.sub(rf'\b{func}\b', f'#{func}#', text)
    
    # 4. Bây giờ mới quét từng ký tự
    result = ''
    prev_char = ''
    operators = set('+-*/^()')

    for ch in text:
        if prev_char:
            if (
                (prev_char.isalpha() and ch.isalpha()) or
                (prev_char.isalpha() and ch.isdigit()) or
                (prev_char.isdigit() and ch.isalpha()) or
                (prev_char == ')' and (ch.isalpha() or ch.isdigit() or ch == '(')) or
                ((prev_char.isalpha() or prev_char.isdigit()) and ch == '(')
            ):
                result += '*'
        result += ch
        prev_char = ch

    # 5. Bỏ đánh dấu các hàm đặc biệt
    for func in functions:
        result = result.replace(f'#{func}#', func)

    # 6. Trường hợp đặc biệt: nếu input là 1 chữ + 1 số (ví dụ: "T4" => "T / 4")
    if re.fullmatch(r'[A-Za-z]\d', text.replace('#', '')):
        return f"{text[0]} / {text[1]}"
    
    return result

def solution_double_string(text : str) -> list[str]:
    oke = True 
    data = []
    while(oke):
        begin = int(1e9)
        end = -1
        for i in range(len(text)):
            if (text[i] == '\n'):
                begin = min(begin,i)
                end = max(end,i)
        if (begin == int(1e9) and end == -1):
            oke = False

        texts = text[begin : end + 1]
        text_clean = smart_clean(texts)
        text = text.replace(texts,text_clean)
        print(text)
        data.append(texts)
    return data
    
def main():

    text_test = "\nT\n=\n2\nπ\nω\n=\n2\nπ\n√\nl\ng T\n=\n2\nπ\nω\n=\n2\nπ\n√\nl\ng T\n=\n2\nπ\nω\n=\n2\nπ\n√\nl\ng T\n=\n2\nπ\nω\n=\n2\nπ\n√\nl\n"
    print(solution_double_string(text_test))
    # print(text_test)


main()