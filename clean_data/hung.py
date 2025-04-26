"from bs4 import BeautifulSoup

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
        if el.name == "mfrac":
            numerator = parse_element(el.find_all(recursive=False)[0])
            denominator = parse_element(el.find_all(recursive=False)[1])
            return f"{numerator}/{denominator}"
        elif el.name in {"mi", "mn", "mo"}:
            return el.text
        else:
            return ''.join(parse_element(child) for child in el.find_all(recursive=False))

    return parse_element(soup.math)


def main():
    
main()