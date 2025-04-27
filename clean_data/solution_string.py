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
        match = re.match(r"^([A-D])\.\s*$", line.strip())  # Chỉ chứa "A.", "B.",...
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

def binary_search(char : str, table_char : list[str], table_check : list[bool]) -> bool:
    l = 0
    r = len(table_char)
    while(l < r):
        mid = int((l + r) >> 1)
        if (char == table_char[mid] and table_check[mid] == False):
            table_check[mid] = True
            return True
        elif (char < table_char[mid]):
            l = mid + 1
        else:
            r = mid - 1
    return False

def caculate(count : int, length : int) -> int:
    if (length != 0):
        return int(count / length) * 100
    else:
        return 0
        

def string_seach_character(string_clean : str, string_before : str) -> str:
    length = len(string_clean)
    vector_char = [string_clean[i] for i in range(len(string_clean))]
    vector_char.sort()
    table_check = [False for i in range(len(string_clean))]
    for i in range(len(string_before) - length):
        count_char = 0
        sub_string = string_before[i : i + length]
        for j in range(len(sub_string)):
            if (binary_search(sub_string[i], vector_char, table_check) != -1):
                count_char += 1
        if (caculate(count_char, len(sub_string)) >= 60):
            string_before = string_before.replace(string_before[i : i + length], "")
            break
        else:
            continue
    return string_before    

def fix_spacing_and_comma(text : str) -> str:
    '''
    text : doan text muon lam dep
    '''    
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