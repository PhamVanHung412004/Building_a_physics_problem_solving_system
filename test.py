import re
def clean_question(text):
    index = re.search(":",text).start()
    t = ""
    for i in range(int((len(text)-index)/2)):
        t = t + text[i]

    return t
def clean_answer(text):
    text = text.replace("\n","")

    return text

def main():
    cauhoi =  "Câu hỏi 2 trang 108 Vật Lí 10: Giải thích vì sao toàn bộ các mũi tên trên hình 1.5 đều được vẽ với độ dài như nhau. Câu hỏi 2 trang 108 Vật Lí 10: Giải thích vì sao toàn bộ các mũi tên trên hình 1.5 đều được vẽ với độ dài như nhau. Câu hỏi 2 trang 108 Vật Lí 10:"
    text = clean_question(cauhoi)
    print(text)
    
main()