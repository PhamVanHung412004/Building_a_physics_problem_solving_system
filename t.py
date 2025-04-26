import re
import json
from pathlib import Path
from bs4 import BeautifulSoup

def clean_question(raw_text):
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

    question = question.replace("\n", "")
    select = parts[1].strip()
    select = select.replace('\n', '')
    select = re.sub(r'(?=[BCD]\.)', r'\n', select)
    select = select.strip()
    if not select.startswith("A."):
        select = "A." + select

    return question, select

def solution(string: str) -> list:
    """
    Trả về danh sách các đoạn (left, right) chứa MathML trong string.
    """
    positions = []
    oke = True

    while oke:
        begin = string.find('<math')
        end = string.find('</math>')

        if begin == -1 or end == -1:
            oke = False
        else:
            end += len('</math>')  # lấy hết </math>
            positions.append((begin, end))
            # Xóa đoạn đã xử lý để tìm tiếp
            string = string[:begin] + ' '*(end-begin) + string[end:]
    
    return positions

def clean_mathml(mathml_string):
    soup = BeautifulSoup(mathml_string, "xml")

    def parse_element(el):
        if el.name == "mfrac":
            numerator = parse_element(el.find_all(recursive=False)[0])
            denominator = parse_element(el.find_all(recursive=False)[1])
            return f"({numerator}/{denominator})"
        elif el.name == "mroot":
            radicand = parse_element(el.find_all(recursive=False)[0])
            index = parse_element(el.find_all(recursive=False)[1]) if len(el.find_all(recursive=False)) > 1 else ''
            return f"√{index}({radicand})" if index else f"√({radicand})"
        elif el.name == "msup":
            base = parse_element(el.find_all(recursive=False)[0])
            exponent = parse_element(el.find_all(recursive=False)[1])
            return f"{base}^{exponent}"
        elif el.name == "msub":
            base = parse_element(el.find_all(recursive=False)[0])
            subscript = parse_element(el.find_all(recursive=False)[1])
            return f"{base}_{subscript}"
        elif el.name == "msubsup":
            base = parse_element(el.find_all(recursive=False)[0])
            subscript = parse_element(el.find_all(recursive=False)[1])
            exponent = parse_element(el.find_all(recursive=False)[2])
            return f"{base}_{subscript}^{exponent}"
        elif el.name == "mo":
            return f" {el.text} "
        elif el.name == "mi" or el.name == "mn":
            return el.text
        elif el.name == "mrow":
            return ''.join(parse_element(child) for child in el.find_all(recursive=False))
        elif el.name == "mfenced":
            return f"({''.join(parse_element(child) for child in el.find_all(recursive=False))})"
        else:
            return ''.join(parse_element(child) for child in el.find_all(recursive=False))

    return parse_element(soup.math)

def main():
    mang = []

    text = {
        "cau_hoi": "Câu 8. Một con lắc đơn có khối lượng 2 kg và có độ dài 4 m, dao động điều hòa ở nơi có gia tốc trọng trường 9,8 m/s2. Cơ năng dao động của con lắc là 0,2205 J. Biên độ góc của con lắc bằng\nA.\n4,3\n0\n.\nB.\n0,7\n0\n.\nC.\n1,3\n0\n.\nD.\n2,1\n0\n.",
        "dap_an": [
            "Ta có: W=mgl2α2maxW=mgl2αmax2<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mtext>W</mtext><mo>=</mo><mfrac><mrow><mi>m</mi><mi>g</mi><mi mathvariant=\"script\">l</mi></mrow><mn>2</mn></mfrac><msubsup><mi>α</mi><mi>max</mi><mn>2</mn></msubsup></math>⇒αmax=√2Wmgl=√2.0,22052.9,8.4=0,075(rad)≈4,30⇒αmax=2Wmgl=2.0,22052.9,8.4=0,075rad≈4,30<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mo>⇒</mo><msub><mi>α</mi><mi>max</mi></msub><mo>=</mo><msqrt><mfrac><mrow><mn>2</mn><mi>W</mi></mrow><mrow><mi>m</mi><mi>g</mi><mi mathvariant=\"script\">l</mi></mrow></mfrac></msqrt><mo>=</mo><msqrt><mfrac><mn>2.0,2205</mn><mn>2.9,8.4</mn></mfrac></msqrt><mo>=</mo><mn>0,075</mn><mfenced><mrow><mi>r</mi><mi>a</mi><mi>d</mi></mrow></mfenced><mo>≈</mo><msup><mn>4,3</mn><mn>0</mn></msup></math>",
            "Đáp án đúng là A."
        ]
    }

    cauhoi, luachon = clean_question(text["cau_hoi"])
    ts = text["dap_an"]

    cleaned_mathmls = []
    for t in ts:
        mathml_positions = solution(t)
        for left, right in mathml_positions:
            mathml_content = t[left:right]
            cleaned_mathml = clean_mathml(mathml_content)
            cleaned_mathmls.append(cleaned_mathml)

    ds = {
        "title": "trắc nghiệm",
        "cau_hoi": cauhoi,
        "cac_lua_chon": luachon,
        "giai_thich": cleaned_mathmls
    }

    mang.append(ds)

    with open("ds_500_tracnghiem_11.json", "w", encoding="utf-8") as file:
        json.dump(mang, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
