from package import re
import json
from read_file import Read_File_Json
from package import Path
from bs4 import BeautifulSoup

def clean_question(raw_text):
    #
    if "\nA" in raw_text:
        parts = raw_text.split("\nA", 1)
    elif "\A" in raw_text:
        parts = raw_text.split("\A", 1)
    else:
        
        parts = [raw_text, ""]
    
    question = parts[0].strip()
    
   
    vtri = re.search(r"\d+", question)
    if vtri:
        question = question[vtri.end():].strip()
    
    question = question.replace("\n","")
    select = parts[1].strip()
    select = select.replace('\n', '')
    select = re.sub(r'(?=[BCD]\.)', r'\n', select)
    select.strip()
    if not select.startswith("A."):
        select = "A" + select

    return question, select


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

def clean_mathml(mathml_string):
    soup = BeautifulSoup(mathml_string, "xml")

    def parse_element(el):
        # Xử lý phân số
        if el.name == "mfrac":
            numerator = parse_element(el.find_all(recursive=False)[0])
            denominator = parse_element(el.find_all(recursive=False)[1])
            return f"({numerator}/{denominator})"
        
        # Xử lý căn bậc
        elif el.name == "mroot":
            radicand = parse_element(el.find_all(recursive=False)[0])
            index = parse_element(el.find_all(recursive=False)[1]) if len(el.find_all(recursive=False)) > 1 else ''
            return f"√{index}({radicand})" if index else f"√({radicand})"
        
        # Xử lý chỉ số trên (exponentiation)
        elif el.name == "msup":
            base = parse_element(el.find_all(recursive=False)[0])
            exponent = parse_element(el.find_all(recursive=False)[1])
            return f"{base}^{exponent}"
        
        # Xử lý chỉ số dưới (subscript)
        elif el.name == "msub":
            base = parse_element(el.find_all(recursive=False)[0])
            subscript = parse_element(el.find_all(recursive=False)[1])
            return f"{base}_{subscript}"
        
        # Xử lý chỉ số trên và dưới (msubsup)
        elif el.name == "msubsup":
            base = parse_element(el.find_all(recursive=False)[0])
            subscript = parse_element(el.find_all(recursive=False)[1])
            exponent = parse_element(el.find_all(recursive=False)[2])
            return f"{base}_{subscript}^{exponent}"
        
        # Xử lý các toán tử
        elif el.name == "mo":
            return f" {el.text} "
        
        # Xử lý các biến và số
        elif el.name == "mi" or el.name == "mn":
            return el.text
        
        # Xử lý nhóm các phần tử con (mrow)
        elif el.name == "mrow":
            return ''.join(parse_element(child) for child in el.find_all(recursive=False))
        
        # Xử lý các dấu ngoặc
        elif el.name == "mfenced":
            return f"({''.join(parse_element(child) for child in el.find_all(recursive=False))})"
        
        else:
            return ''.join(parse_element(child) for child in el.find_all(recursive=False))

    return parse_element(soup.math)



def main():
    mang = []
    path = Path(__file__).parent/"clean_data/500_cau_hoi_trac_nghiem/500_trac_nghiem_11.json"
    texts = Read_File_Json(path).Read()
    # text = {
    #     "cau_hoi": "Câu 8. Một con lắc đơn có khối lượng 2 kg và có độ dài 4 m, dao động điều hòa ở nơi có gia tốc trọng trường 9,8 m/s2. Cơ năng dao động của con lắc là 0,2205 J. Biên độ góc của con lắc bằng\nA.\n4,3\n0\n.\nB.\n0,7\n0\n.\nC.\n1,3\n0\n.\nD.\n2,1\n0\n.",
    #     "dap_an": [
    #         "Ta có: W=mgl2α2maxW=mgl2αmax2<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mtext>W</mtext><mo>=</mo><mfrac><mrow><mi>m</mi><mi>g</mi><mi mathvariant=\"script\">l</mi></mrow><mn>2</mn></mfrac><msubsup><mi>α</mi><mi>max</mi><mn>2</mn></msubsup></math>⇒αmax=√2Wmgl=√2.0,22052.9,8.4=0,075(rad)≈4,30⇒αmax=2Wmgl=2.0,22052.9,8.4=0,075rad≈4,30<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mo>⇒</mo><msub><mi>α</mi><mi>max</mi></msub><mo>=</mo><msqrt><mfrac><mrow><mn>2</mn><mi>W</mi></mrow><mrow><mi>m</mi><mi>g</mi><mi mathvariant=\"script\">l</mi></mrow></mfrac></msqrt><mo>=</mo><msqrt><mfrac><mn>2.0,2205</mn><mn>2.9,8.4</mn></mfrac></msqrt><mo>=</mo><mn>0,075</mn><mfenced><mrow><mi>r</mi><mi>a</mi><mi>d</mi></mrow></mfenced><mo>≈</mo><msup><mn>4,3</mn><mn>0</mn></msup></math>",
    #         "Đáp án đúng là A."
    #     ]
    # }
    for text in texts:
        cauhoi, luachon = clean_question(text["cau_hoi"])
        ts = text["dap_an"]
        cleaned_ds = []
        for t in ts:
            left, right = solution(t)
            if left != -1 and right != -1:
                # Ensure you're slicing correctly
                mathml_content = t[left:right + 1]  # Adjust slicing logic here
                cleaned_mathml = clean_mathml(mathml_content)
                cleaned_ds.append(cleaned_mathml)
            else:
                cleaned_ds.append(t)
        ds = {}
        ds["title"] = "trac nghiem"
        ds["cau_hoi"] = cauhoi
        ds["cac_lua_chon"] = [luachon]
        ds["giai_thich"] = cleaned_ds
        mang.append(ds)
    
    with open("ds_500_tracnghiem_11.json", "a", encoding="utf-8") as file:
        json.dump(mang, file, ensure_ascii=False, indent=4)

main()


