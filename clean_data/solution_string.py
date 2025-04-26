from bs4 import BeautifulSoup

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
    text = "Biên độ của dao động là: A=L2=102=5(cm)A=L2=102=5(cm)<math xmlns=\"http://www.w3.org/1998/Math/MathML\"><mi>A</mi><mo>=</mo><mfrac><mi>L</mi><mn>2</mn></mfrac><mo>=</mo><mfrac><mn>10</mn><mn>2</mn></mfrac><mo>=</mo><mn>5</mn><mo>(</mo><mi>c</mi><mi>m</mi><mo>)</mo></math>"
    left, right = solution(text)
    if left != -1 and right != -1:
        mathml_content = text[left:right + 1]
        cleaned_mathml = clean_mathml(mathml_content)
        print(f"Cleaned MathML: {cleaned_mathml}")

main()
