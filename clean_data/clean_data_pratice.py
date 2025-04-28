# -*- coding: utf-8 -*-
from add_path import add
add()
import re
from package import Path,json

from read_file import Read_File_Json
def clean_question(text):
    text = text.replace("\n","")
    index = re.search(":",text).start()
    # t = ""
    # for i in range(index+2,int((len(text)-index)/2)):
    #     t = t + text[i]
    # text = text[index+2:]
    # t = text.split()
    # ds = []
    # for i in
    return text[index+2:int((len(text)-index)/2)]


def clean_answer(text):
    # text = text.replace("\n","")
    vector_array = text.split()
    check = set()
    vecto_new = []

    for vecto in vector_array:
        if len(vecto)>=0:
            if vecto not in check:
                vecto_new.append(vecto)
                check.add(vecto)
    string =""
    last = []
    for vecto in vecto_new:
        if str(vecto) not in string:
            string +=str(vecto)
            last.append(vecto)
   
    text_beautiful = " ".join(last)
    return text_beautiful
    
        


    # return text_last
    # set_check = set()

    # vector_text_new = []

    # for i in vector_array:
    #     if (i not in set_check):
    #         vector_text_new.append(i)
    #         set_check.add(i)

    # text_beautiful = " ".join(vector_text_new)
    # return text_beautiful
def main():
    # text = " Lời giải: Lời giải: Phương trình (6.6):\nu\n=\nA\ncos\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\n) Phương trình (6.6):\nu\n=\nA\ncos\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\n) u\n=\nA\ncos\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\n) u\n=\nA\ncos\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\n) u\n=\nA\ncos\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\n) u u = = A A cos cos (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\n) ( ( 2\nπ\nT\nt\n−\n2\nπ\nλ\nx 2\nπ\nT 2\nπ\nT 2\nπ 2\nπ 2 2 π π T T T t t − − 2\nπ\nλ 2\nπ\nλ 2\nπ 2\nπ 2 2 π π λ λ λ x x ) ) Gọi M và N là hai điểm gần nhau nhất cách nguồn sóng khoảng cách lần lượt là xM và xN. Gọi M và N là hai điểm gần nhau nhất cách nguồn sóng khoảng cách lần lượt là xM và xN. M N - Trường hợp M và N dao động cùng pha: - Trường hợp M và N dao động cùng pha: (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n)\n−\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n)\n=\n2\nk\nπ\n⇒\n2\nπ\nλ\n(\nx\nN\n−\nx\nM\n)\n=\n2\nk\nπ\n⇒\nx\nN\n−\nx\nM\n=\nk\nλ (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n)\n−\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n)\n=\n2\nk\nπ\n⇒\n2\nπ\nλ\n(\nx\nN\n−\nx\nM\n)\n=\n2\nk\nπ\n⇒\nx\nN\n−\nx\nM\n=\nk\nλ (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n)\n−\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n)\n=\n2\nk\nπ\n⇒\n2\nπ\nλ\n(\nx\nN\n−\nx\nM\n)\n=\n2\nk\nπ\n⇒\nx\nN\n−\nx\nM\n=\nk\nλ (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n)\n−\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n)\n=\n2\nk\nπ\n⇒\n2\nπ\nλ\n(\nx\nN\n−\nx\nM\n)\n=\n2\nk\nπ\n⇒\nx\nN\n−\nx\nM\n=\nk\nλ (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n)\n−\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n)\n=\n2\nk\nπ\n⇒\n2\nπ\nλ\n(\nx\nN\n−\nx\nM\n)\n=\n2\nk\nπ\n⇒\nx\nN\n−\nx\nM\n=\nk\nλ (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n) ( ( 2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM 2\nπ\nT 2\nπ\nT 2\nπ 2\nπ 2 2 π π T T T t t − − 2\nπ\nλ 2\nπ\nλ 2\nπ 2\nπ 2 2 π π λ λ λ x\nM x x x M M M ) ) − − (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n) ( ( 2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN 2\nπ\nT 2\nπ\nT 2\nπ 2\nπ 2 2 π π T T T t t − − 2\nπ\nλ 2\nπ\nλ 2\nπ 2\nπ 2 2 π π λ λ λ x\nN x x x N N N ) ) = = 2 2 k k π π ⇒ ⇒ 2\nπ\nλ 2\nπ\nλ 2\nπ 2\nπ 2 2 π π λ λ λ (\nx\nN\n−\nx\nM\n) ( ( x\nN\n−\nx\nM x\nN x x x N N N − − x\nM x x x M M M ) ) = = 2 2 k k π π ⇒ ⇒ x\nN x x x N N N − − x\nM x x x M M M = = k k λ λ Tức là khoảng cách giữa hai điểm gần nhất dao động cùng pha bằng một số nguyên lần bước sóng. Tức là khoảng cách giữa hai điểm gần nhất dao động cùng pha bằng một số nguyên lần bước sóng. - Trường hợp M và N dao động ngược pha: - Trường hợp M và N dao động ngược pha: (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n)\n−\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\n2\nπ\nλ\n(\nx\nN\n−\nx\nM\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\nx\nN\n−\nx\nM\n=\n(\n2\nk\n+\n1\n)\nλ\n2\n=\n(\nk\n+\n0\n,\n5\n)\nλ (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n)\n−\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\n2\nπ\nλ\n(\nx\nN\n−\nx\nM\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\nx\nN\n−\nx\nM\n=\n(\n2\nk\n+\n1\n)\nλ\n2\n=\n(\nk\n+\n0\n,\n5\n)\nλ (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n)\n−\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\n2\nπ\nλ\n(\nx\nN\n−\nx\nM\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\nx\nN\n−\nx\nM\n=\n(\n2\nk\n+\n1\n)\nλ\n2\n=\n(\nk\n+\n0\n,\n5\n)\nλ (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n)\n−\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\n2\nπ\nλ\n(\nx\nN\n−\nx\nM\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\nx\nN\n−\nx\nM\n=\n(\n2\nk\n+\n1\n)\nλ\n2\n=\n(\nk\n+\n0\n,\n5\n)\nλ (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n)\n−\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\n2\nπ\nλ\n(\nx\nN\n−\nx\nM\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\nx\nN\n−\nx\nM\n=\n(\n2\nk\n+\n1\n)\nλ\n2\n=\n(\nk\n+\n0\n,\n5\n)\nλ (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n)\n−\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\n2\nπ\nλ\n(\nx\nN\n−\nx\nM\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\nx\nN\n−\nx\nM\n=\n(\n2\nk\n+\n1\n)\nλ\n2\n=\n(\nk\n+\n0\n,\n5\n)\nλ (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n)\n−\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\n2\nπ\nλ\n(\nx\nN\n−\nx\nM\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\nx\nN\n−\nx\nM\n=\n(\n2\nk\n+\n1\n)\nλ\n2\n=\n(\nk\n+\n0\n,\n5\n)\nλ (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n)\n−\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n)\n=\n(\n2\nk\n+\n1\n)\nπ (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n)\n−\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n)\n=\n(\n2\nk\n+\n1\n)\nπ (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n)\n−\n(\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n)\n=\n(\n2\nk\n+\n1\n)\nπ (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM\n) ( ( 2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nM 2\nπ\nT 2\nπ\nT 2\nπ 2\nπ 2 2 π π T T T t t − − 2\nπ\nλ 2\nπ\nλ 2\nπ 2\nπ 2 2 π π λ λ λ x\nM x x x M M M ) ) − − (\n2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN\n) ( ( 2\nπ\nT\nt\n−\n2\nπ\nλ\nx\nN 2\nπ\nT 2\nπ\nT 2\nπ 2\nπ 2 2 π π T T T t t − − 2\nπ\nλ 2\nπ\nλ 2\nπ 2\nπ 2 2 π π λ λ λ x\nN x x x N N N ) ) = = (\n2\nk\n+\n1\n) ( ( 2\nk\n+\n1 2 2 k k + + 1 1 ) ) π π ⇒\n2\nπ\nλ\n(\nx\nN\n−\nx\nM\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\nx\nN\n−\nx\nM\n=\n(\n2\nk\n+\n1\n)\nλ\n2\n=\n(\nk\n+\n0\n,\n5\n)\nλ ⇒\n2\nπ\nλ\n(\nx\nN\n−\nx\nM\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\nx\nN\n−\nx\nM\n=\n(\n2\nk\n+\n1\n)\nλ\n2\n=\n(\nk\n+\n0\n,\n5\n)\nλ ⇒\n2\nπ\nλ\n(\nx\nN\n−\nx\nM\n)\n=\n(\n2\nk\n+\n1\n)\nπ\n⇒\nx\nN\n−\nx\nM\n=\n(\n2\nk\n+\n1\n)\nλ\n2\n=\n(\nk\n+\n0\n,\n5\n)\nλ ⇒ ⇒ 2\nπ\nλ 2\nπ\nλ 2\nπ 2\nπ 2 2 π π λ λ λ (\nx\nN\n−\nx\nM\n) ( ( x\nN\n−\nx\nM x\nN x x x N N N − − x\nM x x x M M M ) ) = = (\n2\nk\n+\n1\n) ( ( 2\nk\n+\n1 2 2 k k + + 1 1 ) ) π π ⇒ ⇒ x\nN x x x N N N − − x\nM x x x M M M = = (\n2\nk\n+\n1\n) ( ( 2\nk\n+\n1 2 2 k k + + 1 1 ) ) λ\n2 λ\n2 λ λ λ 2 2 2 = = (\nk\n+\n0\n,\n5\n) ( ( k\n+\n0\n,\n5 k k + + 0 0 , , 5 5 ) ) λ λ Tức là khoảng cách giữa hai điểm gần nhất dao động ngược pha bằng một số bán nguyên lần bước sóng. Tức là khoảng cách giữa hai điểm gần nhất dao động ngược pha bằng một số bán nguyên lần bước sóng. Lời giải Vật Lí 11 Bài 6: Các đặc trưng vật lí của sóng hay khác: Mở đầu trang 39 Vật Lí 11: Động đất cùng những dịch chuyển địa chất lớn ở mặt nước hoặc dưới mặt nước sẽ sinh ra những đợt sóng lớn và đột ngột....\nCâu hỏi 1 trang 40 Vật Lí 11: Quan sát Hình 6.2, thực hiện các yêu cầu sau:Cho biết sóng truyền trên dây là sóng dọc hay sóng ngang. ....\nCâu hỏi 2 trang 40 Vật Lí 11: Quan sát Hình 6.3, hãy: Chỉ ra những điểm trên dây đang có trạng thái dao động giống nhau tại thời điểm đang xét.....\nCâu hỏi 3 trang 41 Vật Lí 11: Tốc độ truyền sóng trong môi trường nhanh hay chậm có phụ thuộc tốc độ dao động tại chỗ của các phần tử môi trường không?...\nCâu hỏi 4 trang 42 Vật Lí 11: Từ ví dụ về tốc độ truyền sóng âm trong các môi trường rắn, lỏng và khí, hãy rút ra nhận xét và giải thích sự khác nhau này. ....\nLuyện tập trang 42 Vật Lí 11: Một bạn học sinh đang câu cá trên hồ nước. Khi có sóng đi qua, bạn quan sát thấy phao câu cá nhô lên cao 6 lần....\nLuyện tập trang 43 Vật Lí 11: Biết cường độ ánh sáng của Mặt Trời đo được tại Trái Đất là .... Mở đầu trang 39 Vật Lí 11: Động đất cùng những dịch chuyển địa chất lớn ở mặt nước hoặc dưới mặt nước sẽ sinh ra những đợt sóng lớn và đột ngột.... Mở đầu trang 39 Vật Lí 11: Động đất cùng những dịch chuyển địa chất lớn ở mặt nước hoặc dưới mặt nước sẽ sinh ra những đợt sóng lớn và đột ngột.... Mở đầu trang 39 Vật Lí 11: Động đất cùng những dịch chuyển địa chất lớn ở mặt nước hoặc dưới mặt nước sẽ sinh ra những đợt sóng lớn và đột ngột.... Mở đầu trang 39 Vật Lí 11: Câu hỏi 1 trang 40 Vật Lí 11: Quan sát Hình 6.2, thực hiện các yêu cầu sau:Cho biết sóng truyền trên dây là sóng dọc hay sóng ngang. .... Câu hỏi 1 trang 40 Vật Lí 11: Quan sát Hình 6.2, thực hiện các yêu cầu sau:Cho biết sóng truyền trên dây là sóng dọc hay sóng ngang. .... Câu hỏi 1 trang 40 Vật Lí 11: Quan sát Hình 6.2, thực hiện các yêu cầu sau:Cho biết sóng truyền trên dây là sóng dọc hay sóng ngang. .... Câu hỏi 1 trang 40 Vật Lí 11: Câu hỏi 2 trang 40 Vật Lí 11: Quan sát Hình 6.3, hãy: Chỉ ra những điểm trên dây đang có trạng thái dao động giống nhau tại thời điểm đang xét..... Câu hỏi 2 trang 40 Vật Lí 11: Quan sát Hình 6.3, hãy: Chỉ ra những điểm trên dây đang có trạng thái dao động giống nhau tại thời điểm đang xét..... Câu hỏi 2 trang 40 Vật Lí 11: Quan sát Hình 6.3, hãy: Chỉ ra những điểm trên dây đang có trạng thái dao động giống nhau tại thời điểm đang xét..... Câu hỏi 2 trang 40 Vật Lí 11: Câu hỏi 3 trang 41 Vật Lí 11: Tốc độ truyền sóng trong môi trường nhanh hay chậm có phụ thuộc tốc độ dao động tại chỗ của các phần tử môi trường không?... Câu hỏi 3 trang 41 Vật Lí 11: Tốc độ truyền sóng trong môi trường nhanh hay chậm có phụ thuộc tốc độ dao động tại chỗ của các phần tử môi trường không?... Câu hỏi 3 trang 41 Vật Lí 11: Tốc độ truyền sóng trong môi trường nhanh hay chậm có phụ thuộc tốc độ dao động tại chỗ của các phần tử môi trường không?... Câu hỏi 3 trang 41 Vật Lí 11: Câu hỏi 4 trang 42 Vật Lí 11: Từ ví dụ về tốc độ truyền sóng âm trong các môi trường rắn, lỏng và khí, hãy rút ra nhận xét và giải thích sự khác nhau này. .... Câu hỏi 4 trang 42 Vật Lí 11: Từ ví dụ về tốc độ truyền sóng âm trong các môi trường rắn, lỏng và khí, hãy rút ra nhận xét và giải thích sự khác nhau này. .... Câu hỏi 4 trang 42 Vật Lí 11: Từ ví dụ về tốc độ truyền sóng âm trong các môi trường rắn, lỏng và khí, hãy rút ra nhận xét và giải thích sự khác nhau này. .... Câu hỏi 4 trang 42 Vật Lí 11: Luyện tập trang 42 Vật Lí 11: Một bạn học sinh đang câu cá trên hồ nước. Khi có sóng đi qua, bạn quan sát thấy phao câu cá nhô lên cao 6 lần.... Luyện tập trang 42 Vật Lí 11: Một bạn học sinh đang câu cá trên hồ nước. Khi có sóng đi qua, bạn quan sát thấy phao câu cá nhô lên cao 6 lần.... Luyện tập trang 42 Vật Lí 11: Một bạn học sinh đang câu cá trên hồ nước. Khi có sóng đi qua, bạn quan sát thấy phao câu cá nhô lên cao 6 lần.... Luyện tập trang 42 Vật Lí 11: Luyện tập trang 43 Vật Lí 11: Biết cường độ ánh sáng của Mặt Trời đo được tại Trái Đất là .... Luyện tập trang 43 Vật Lí 11: Biết cường độ ánh sáng của Mặt Trời đo được tại Trái Đất là .... Luyện tập trang 43 Vật Lí 11: Biết cường độ ánh sáng của Mặt Trời đo được tại Trái Đất là .... Luyện tập trang 43 Vật Lí 11: Câu hỏi 6 trang 44 Vật Lí 11: Quan sát Hình 6.3, xác định độ lệch pha của hai điểm A và B trên cùng phương truyền sóng ...\nLuyện tập trang 44 Vật Lí 11: Giải thích vì sao ở Hình 6.6a, đường biểu diễn có một đoạn nằm ngang sau vị trí có toạ độ x1 và ở Hình 6.6b....\nVận dụng trang 44 Vật Lí 11: Đề xuất phương án thí nghiệm và thực hiện thí nghiệm đơn giản để tạo ra sóng truyền trên một sợi dây và xác định các đại lượng đặc trưng của sóng như chu kì, tần số.....\nBài 1 trang 45 Vật Lí 11: Khi đi biển, các thuỷ thủ trên thuyền có thể sử dụng kĩ thuật sonar (một kĩ thuật phát ra sóng siêu âm) ....\nBài 2 trang 45 Vật Lí 11: Hai điểm gần nhất trên cùng phương truyền sóng dao động lệch pha nhau....\nBài 3 trang 45 Vật Lí 11: Một sóng truyền trên một dây rất dài có phương trình: .... Câu hỏi 6 trang 44 Vật Lí 11: Quan sát Hình 6.3, xác định độ lệch pha của hai điểm A và B trên cùng phương truyền sóng ... Câu hỏi 6 trang 44 Vật Lí 11: Quan sát Hình 6.3, xác định độ lệch pha của hai điểm A và B trên cùng phương truyền sóng ... Câu hỏi 6 trang 44 Vật Lí 11: Quan sát Hình 6.3, xác định độ lệch pha của hai điểm A và B trên cùng phương truyền sóng ... Câu hỏi 6 trang 44 Vật Lí 11: Luyện tập trang 44 Vật Lí 11: Giải thích vì sao ở Hình 6.6a, đường biểu diễn có một đoạn nằm ngang sau vị trí có toạ độ x1 và ở Hình 6.6b.... Luyện tập trang 44 Vật Lí 11: Giải thích vì sao ở Hình 6.6a, đường biểu diễn có một đoạn nằm ngang sau vị trí có toạ độ x1 và ở Hình 6.6b.... Luyện tập trang 44 Vật Lí 11: Giải thích vì sao ở Hình 6.6a, đường biểu diễn có một đoạn nằm ngang sau vị trí có toạ độ x1 và ở Hình 6.6b.... Luyện tập trang 44 Vật Lí 11: Vận dụng trang 44 Vật Lí 11: Đề xuất phương án thí nghiệm và thực hiện thí nghiệm đơn giản để tạo ra sóng truyền trên một sợi dây và xác định các đại lượng đặc trưng của sóng như chu kì, tần số..... Vận dụng trang 44 Vật Lí 11: Đề xuất phương án thí nghiệm và thực hiện thí nghiệm đơn giản để tạo ra sóng truyền trên một sợi dây và xác định các đại lượng đặc trưng của sóng như chu kì, tần số..... Vận dụng trang 44 Vật Lí 11: Đề xuất phương án thí nghiệm và thực hiện thí nghiệm đơn giản để tạo ra sóng truyền trên một sợi dây và xác định các đại lượng đặc trưng của sóng như chu kì, tần số..... Vận dụng trang 44 Vật Lí 11: Bài 1 trang 45 Vật Lí 11: Khi đi biển, các thuỷ thủ trên thuyền có thể sử dụng kĩ thuật sonar (một kĩ thuật phát ra sóng siêu âm) .... Bài 1 trang 45 Vật Lí 11: Khi đi biển, các thuỷ thủ trên thuyền có thể sử dụng kĩ thuật sonar (một kĩ thuật phát ra sóng siêu âm) .... Bài 1 trang 45 Vật Lí 11: Khi đi biển, các thuỷ thủ trên thuyền có thể sử dụng kĩ thuật sonar (một kĩ thuật phát ra sóng siêu âm) .... Bài 1 trang 45 Vật Lí 11: Bài 2 trang 45 Vật Lí 11: Hai điểm gần nhất trên cùng phương truyền sóng dao động lệch pha nhau.... Bài 2 trang 45 Vật Lí 11: Hai điểm gần nhất trên cùng phương truyền sóng dao động lệch pha nhau.... Bài 2 trang 45 Vật Lí 11: Hai điểm gần nhất trên cùng phương truyền sóng dao động lệch pha nhau.... Bài 2 trang 45 Vật Lí 11: Bài 3 trang 45 Vật Lí 11: Một sóng truyền trên một dây rất dài có phương trình: .... Bài 3 trang 45 Vật Lí 11: Một sóng truyền trên một dây rất dài có phương trình: .... Bài 3 trang 45 Vật Lí 11: Một sóng truyền trên một dây rất dài có phương trình: .... Bài 3 trang 45 Vật Lí 11:"
    # text = text.replace("\n","")
    
    text = "Bài 1 trang 53 Vật Lí 10: Một máy bay đang bay ở độ cao 5 km với tốc độ 500 km/h theo phương ngang thì thả rơi một vật. Hỏi người lái máy bay phải vật cách mục tiêu bao xa theo phương ngang để vật rơi trúng mục tiêu? Lấy g = 9,8 m/s2. Bài 1 trang 53 Vật Lí 10: Một máy bay đang bay ở độ cao 5 km với tốc độ 500 km/h theo phương ngang thì thả rơi một vật. Hỏi người lái máy bay phải vật cách mục tiêu bao xa theo phương ngang để vật rơi trúng mục tiêu? Lấy g = 9,8 m/s2. Bài 1 trang 53 Vật Lí 10: 2"
    # text = text.replace("\n"," ")
    t = text.split(".")
    t = t[0:len(t)-1]

    # Gom 3 từ một nhóm
    # t = [" ".join(txt[i:i+3]) for i in range(0, len(txt), 3)]

    # ds_new = []
    # check = "" # Dùng set để kiểm tra nhanh phần tử đã có chưa

    # for i in t:
    #     if i not in check:
    #         check += (" "+ i) # Thêm vào set
    #         ds_new.append(i)
    # print(ds_new)

    path = Path(__file__).parent/"data_practice/bai_tap_11.json"  
    datas = Read_File_Json(path).Read()
    ds_mang = []
    for data in datas:
        ds = {}
        cauhoi = clean_question(data["cau_hoi"])
        ds["title"] = "tu_luan"
        ds["cau_hoi"] = cauhoi
        ds["loi_giai"] = ""
        ds_mang.append(ds)
    
    with open("output.json","w",encoding ="utf-8") as file:
        json.dump(ds_mang ,file, ensure_ascii=False, indent=4)
    
    # text = " Lời giải: Lời giải: Dụng cụ: Dụng cụ: Dụng cụ: - Đệm không khí (1) - Đệm không khí (1) - Hai tấm chắn cổng quang điện (2) - Hai tấm chắn cổng quang điện (2) - Miếng dính (3) - Miếng dính (3) - Hai xe trượt (4) và một số quả nặng để thay đổi khối lượng của xe. - Hai xe trượt (4) và một số quả nặng để thay đổi khối lượng của xe. - Hai cổng quang điện (5) được nối với hai đồng hồ đo thời gian hiện số (6) (có độ chính xác đến 1 ms). - Hai cổng quang điện (5) được nối với hai đồng hồ đo thời gian hiện số (6) (có độ chính xác đến 1 ms). - Thước đo chiều dài có độ chia nhỏ nhất là 1 mm. - Thước đo chiều dài có độ chia nhỏ nhất là 1 mm. - Cân có độ chính xác đến 0,1 g để xác định khối lượng m của mỗi xe và\nΔ\nm\ncủa mỗi quả nặng. - Cân có độ chính xác đến 0,1 g để xác định khối lượng m của mỗi xe và Δ\nm Δ\nm Δ\nm Δ\nm Δ Δ m m của mỗi quả nặng. Tiến hành thí nghiệm Tiến hành thí nghiệm Tiến hành thí nghiệm - Bước 1: Gắn miếng dính vào đầu của xe 1. Gắn 2 tấm chắn cổng quang điện lên mỗi xe. - Bước 1: Gắn miếng dính vào đầu của xe 1. Gắn 2 tấm chắn cổng quang điện lên mỗi xe. - Bước 2: Đo tổng khối lượng của xe 1 và xe 2 sau khi đã gắn miếng dính và tấm chắn cổng quang điện, ghi vào bảng số liệu mẫu. - Bước 2: Đo tổng khối lượng của xe 1 và xe 2 sau khi đã gắn miếng dính và tấm chắn cổng quang điện, ghi vào bảng số liệu mẫu. - Bước 3: Giữ xe 2 đứng yên, đẩy cho xe 1 chuyển động đến va chạm với xe 2. - Bước 3: Giữ xe 2 đứng yên, đẩy cho xe 1 chuyển động đến va chạm với xe 2. - Bước 4: Đo thời gian hai xe đi qua cổng quang điện trước và sau va chạm. - Bước 4: Đo thời gian hai xe đi qua cổng quang điện trước và sau va chạm. - Bước 5: xử lí số liệu và đưa ra kết luận. - Bước 5: xử lí số liệu và đưa ra kết luận."
    # # print(text.replace("\n",""))
    # dapan = clean_answer(text)
    # print(dapan)
    # # clean_answer(text)
  
main()