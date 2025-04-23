import json
import re
# from read_file import Read_File_Json

# Đầu vào

input_datas =[{
    "cau_hoi": "Câu 6: Cơ chế của các phản ứng hóa học được giải thích dựa trên kiến thức thuộc lĩnh vực nào của Vật lí?\nA. Vật lí nguyên tử và hạt nhân.\nB. Quang học.\nC. Âm học.\nD. Điện học.",
    "dap_an": [
      "Đáp án đúng là: A",
      "Cơ chế của các phản ứng hóa học được giải thích dựa trên kiến thức thuộc lĩnh vực Vật lí nguyên tử và hạt nhân của Vật lí."
    ]
  },
  {
    "cau_hoi": "Câu 7: Nhờ việc khám phá ra hiện tượng nào sau đây của nhà vật lí Faraday mà sau đó các máy phát điện ra đời, mở đầu cho kỉ nguyên sử dụng điện năng của nhân loại?\nA. Hiện tượng hóa hơi.\nB. Hiện tượng biến dạng cơ của vật rắn.\nC. Sự nở vì nhiệt của vật rắn.\nD. Hiện tượng cảm ứng điện từ.",
    "dap_an": [
      "Đáp án đúng là: D",
      "Việc khám phá ra hiện tượng cảm ứng điện từ của nhà Vật lí Faraday đã mở đầu cho kỉ nguyên sử dụng điện năng của nhân loại và là một trong những cơ sở cho sự ra đời của cuộc cách  mạng công nghiệp lần thứ hai vào cuối thế kỉ XIX."
    ]
  },
  {
    "cau_hoi": "Câu 8: Nêu các phương pháp nghiên cứu thường được sử dụng trong Vật lí?\nA. Phương pháp thực nghiệm và phương pháp mô hình.\nB. Phương pháp thực nghiệm, phương pháp mô hình, phương pháp quan sát và suy luận.\nC. Phương pháp thực nghiệm, phương pháp quan sát và suy luận.\nD. Phương pháp mô hình, phương pháp quan sát và suy luận.",
    "dap_an": [
      "Đáp án đúng là: A",
      "Phương pháp nghiên cứu thường được sử dụng trong Vật lí là phương pháp thực nghiệm và phương pháp mô hình."
    ]
  },
  {
    "cau_hoi": "Câu 9: Các loại mô hình nào sau đây là các mô hình thường dùng trong trường phổ thông?\nA. Mô hình vật chất.\nB. Mô hình lí thuyết.\nC. Mô hình toán học.\nD. Cả ba mô hình trên.",
    "dap_an": [
      "Đáp án đúng là: D",
      "Các loại mô hình thường dùng trong trường phổ thông là:",
      "Mô hình vật chất: mô hình thu nhỏ Trái Đất,…",
      "Mô hình lí thuyết: coi chuyển động của vật là chất điểm, mô hình tia sáng,…",
      "Mô hình toán học: các công thức, phương trình, đồ thị, kí hiệu,…"
    ]
  },
  {
    "cau_hoi": "Câu 10: Phương pháp thực nghiệm có các bước thực hiện nào sau đây?\nA. Xác định vấn đề cần nghiên cứu. Quan sát, thu thập thông tin. Đưa ra dự doánd. Thí nghiệm kiểm tra dự đoán. Kết luận\nB. Xác định đối tượng cần được mô hình hóa. Xây dựng mô hình giả thuyết. Kiểm tra sự phù hợp của các mô hình. Điều chỉnh lại mô hình nếu cần. Kết luận.\nC. Quan sát. Lập luận. Kết luận.\nD. Không có đáp án nào trong các đáp án trên.",
    "dap_an": [
      "Đáp án đúng là: A.",
      "A - phương pháp thực nghiệm.",
      "B - phương pháp mô hình.",
      "C - phương pháp quan sát, suy luận.",
      "D - sai."
    ]
  },
  {
    "cau_hoi": "Câu 1: DC hoặc dấu - là kí hiệu mô tả đại lượng nào sau đây?\nA. Dòng điện xoay chiều.\nB. Dòng điện một chiều.\nC. Dòng điện không đổi.\nD. Máy biến áp.",
    "dap_an": [
      "Đáp án đúng là: B.",
      "Dòng điện một chiều có kí hiệu là DC hoặc dấu -."
    ]
  },
  {
    "cau_hoi": "Câu 2: AC hoặc dấu ~ là kí hiệu mô tả đại lượng nào sau đây?\nA. Dòng điện xoay chiều.\nB. Dòng điện một chiều.\nC. Dòng điện không đổi.\nD. Máy biến áp.",
    "dap_an": [
      "Đáp án đúng là: A.",
      "Dòng điện xoay chiều có kí hiệu là AC hoặc dấu ~."
    ]
  },
  {
    "cau_hoi": "Câu 3: Khi sử dụng các thiết bị điện trong phòng thí nghiệm Vật lí chúng ta cần lưu ý điều gì?\nA. Cần quan sát kĩ các kí hiệu và nhãn thông số trên thiết bị để sử dụng đúng chức năng, đúng yêu cầu kĩ thuật.\nB. Khởi động luôn hệ thống và tiến hành thí nghiệm.\nC. Quan sát sơ bộ các kí hiệu rồi khởi động hệ thống để tiến hành thí nghiệm.\nD. Không cần sử dụng đúng chức năng của thiết bị.",
    "dap_an": [
      "Đáp án đúng là: A.",
      "Khi sử dụng các thiết bị điện trong phòng thí nghiệm Vật lí chúng ta cần quan sát kĩ các kí hiệu và nhãn thông số trên thiết bị để sử dụng đúng chức năng, đúng yêu cầu kĩ thuật."
    ]
  },
  {
    "cau_hoi": "Câu 4: Khi sử dụng các thiết bị nhiệt và thủy tinh trong phòng thí nghiệm Vật lí chúng ta cần lưu ý điều gì?\nA. Quan sát kĩ các kí hiệu trên thiết bị, đặc điểm của dụng cụ thí nghiệm, chức năng của dụng cụ.\nB. Tiến hành thí nghiệm không cần quan sát vì tin tưởng vào dụng cụ phòng thí nghiệm.\nC. Quan sát các kí hiệu trên thiết bị, đặc điểm của các dụng cụ thí nghiệm, có thể dùng dụng cụ này thay thế cho dụng cụ khác.\nD. Có thể sử dụng mọi ống thủy tinh trong phòng thí nghiệm vào tất cả các thí nghiệm.",
    "dap_an": [
      "Đáp án đúng là: A.",
      "A - Đúng vì khi sử dụng các thiết bị nhiệt và thủy tinh trong phòng thí nghiệm Vật lí chúng ta cần lưu ý: quan sát kĩ các kí hiệu trên thiết bị, đặc điểm của dụng cụ thí nghiệm, chức năng của dụng cụ.",
      "B - sai vì: dụng cụ phòng thí nghiệm có thể bị lỗi, hoặc hỏng.",
      "C - sai vì: mỗi dụng cụ có chức năng khác nhau.",
      "D - sai vì: ống thủy tinh có nhiều loại, có loại chịu được nhiệt độ cao, có loại không chịu được nhiệt độ cao."
    ]
  },
  {
    "cau_hoi": "Câu 5: Những dụng cụ nào sau đây trong phòng thí nghiệm Vật lí thuộc loại dễ vỡ?\nA.đèn cồn, các hóa chất, những dụng cụ bằng nhựa như ca nhựa,...\nB.ống nghiệm, đũa thủy tinh, nhiệt kế, cốc thủy tinh, kính....\nC. lực kế, các bộ thí nghiệm như là ròng rọc, đòn bẩy....\nD. đèn cồn, hóa chất, ống nghiệm…",
    "dap_an": [
      "Đáp án đúng là: B.",
      "A - sai vì đây là các dụng cụ, hóa chất dễ cháy.",
      "B - đúng vì đây là các dụng cụ dễ vỡ.",
      "C - sai vì đây là các dụng cụ dễ hỏng.",
      "D - sai vì đây là các dụng cụ hóa chất dễ cháy và dễ vỡ."
    ]
  },
  {
    "cau_hoi": "Câu 6: Thao tác nào dưới đây có thể gây mất an toàn khi sử dụng thiết bị thí nghiệm Vật lí?\nA. Chiếu trực tiếp tia laze vào mắt để kiểm tra độ sáng.\nB. Dùng tay kiểm tra mức độ nóng của vật khi đang đun.\nC. Không cầm vào phích điện mà cầm vào dây điện khi rút phích điện khỏi ổ cắm.\nD. Tất cả các phương án trên.",
    "dap_an": [
      "Đáp án đúng là: D.",
      "A- có hại cho mắt.",
      "B- có thể gây bỏng.",
      "C- có thể bị điện giật.",
      "D- đúng."
    ]
  },
  {
    "cau_hoi": "Câu 7: Nếu sử dụng ampe kế để đo dòng điện vượt qua giới hạn đo thì có thể gây ra nguy cơ gì ?\nA. Ampe kế có thể bị chập cháy.\nB. Không có vấn đề gì xảy ra.\nC. Kết quả thí nghiệm không chính xác.\nD. Không hiện kết quả đo.",
    "dap_an": [
      "Đáp án đúng là: A.",
      "Nếu sử dụng ampe kế để đo dòng điện vượt qua giới hạn đo thì ampe kế có thể bị chập cháy."
    ]
  },
  {
    "cau_hoi": "Câu 8: Những hành động nào sau đây là đúng khi làm việc trong phòng thí nghiệm?\nA. Để các kẹp điện gần nhau.\nB. Để chất dễ cháy gần thí nghiệm mạch điện.\nC. Không đeo găng tay cao su chịu nhiệt khi làm thí nghiệm với nhiệt độ cao.\nD. Không có hành động nào đúng trong ba hành động trên.",
    "dap_an": [
      "A- sai vì dễ xảy ra cháy nổ.",
      "B- sai vì dễ xảy ra cháy nổ.",
      "C- sai vì dễ bị bỏng.",
      "D- đúng."
    ]
  },
  {
    "cau_hoi": "Câu 9: Khi có hỏa hoạn trong phòng thực hành cần xử lí theo cách nào sau đây?\nA. Bình tĩnh, sử dụng các biện pháp dập tắt ngọn lửa theo hướng dẫn của phòng thực hành như ngắt toàn bộ hệ thống điện, đưa toàn bộ các hóa chất, các chất dễ cháy ra khu vực an toàn…\nB. Sử dụng nước để dập đám cháy nơi có các thiết bị điện.\nC. Sử dụng bình để dập đám cháy quần áo trên người.\nD. Không cần ngắt hệ thống điện, phải dập đám cháy trước.",
    "dap_an": [
      "Đáp án đúng là: A.",
      "Khi có hỏa hoạn trong phòng thực hành cần bình tĩnh, sử dụng các biện pháp dập tắt ngọn lửa theo hướng dẫn của phòng thực hành như ngắt toàn bộ hệ thống điện, đưa toàn bộ các hóa chất, các chất dễ cháy ra khu vực an toàn…"
    ]
  },
  {
    "cau_hoi": "Câu 10: Kí hiệu cảnh báo khu vực nguy hiểm có đặc điểm nào sau đây?\nA. Hình vuông, viền đen, nền đỏ cam.\nB. Hình tam giác đều, viền đen hoặc viền đỏ, nền vàng.\nC. Hình chữ nhật nền xanh hoặc đỏ.\nD. Hình tròn, viền đỏ, nền trắng.",
    "dap_an": [
      "Đáp án đúng là: B.",
      "A- sai vì đây là kí hiệu cảnh báo nguy hiểm do hóa chất gây ra.",
      "B- đúng vì đây là kí hiệu cảnh báo các khu vực nguy hiểm.",
      "C- sai vì đây là kí hiệu cảnh báo chỉ dẫn thực hiện.",
      "D- sai vì đây là kí hiệu cảnh báo cấm."
    ]
  },
  {
    "cau_hoi": "Câu 1: Vật nào sau đây được coi là chất điểm?\nA. Một xe máy đi từ TP Hồ Chí Minh ra Hà Nội.\nB. Một xe ô tô khách loại 45 chỗ ngồi chuyển động từ giữa sân trường ra cổng trường.\nC. Một bạn học sinh đi từ nhà ra cổng.\nD. Một bạn học sinh đi từ cuối lớp lên bục giảng.",
    "dap_an": [
      "Đáp án đúng là A.",
      "A - đúng vì trường hợp này kích thước của xe máy rất nhỏ so với độ dài của quãng đường.",
      "B - sai vì kích thước của ô tô khách đáng kể so với độ dài quãng đường của nó.",
      "C - sai vì kích thước của bạn học sinh đáng kể so với quãng đường bạn học sinh di chuyển.",
      "D - sai vì kích thước của bạn học sinh đáng kể so với quãng đường bạn học sinh di chuyển."
    ]
  },
  {
    "cau_hoi": "Câu 2: Trường hợp nào dưới đây không thể coi vật là chất điểm?\nA. Viên đạn đang chuyển động trong không khí.\nB. Trái Đất trong chuyển động quay quanh Mặt Trời.\nC. Viên bi trong sự rơi từ tầng thứ năm của một tòa nhà xuống đất.\nD. Trái Đất trong chuyển động tự quay quanh trục của nó.",
    "dap_an": [
      "Đáp án đúng là D.",
      "Trái Đất trong chuyển động tự quay quanh trục có kích thước đáng kể so với quỹ đạo chuyển động nên không được coi là một chất điểm."
    ]
  }]
input_data = {
    "cau_hoi": "Câu 1: Vật nào sau đây được coi là chất điểm?\nA. Một xe máy đi từ TP Hồ Chí Minh ra Hà Nội.\nB. Một xe ô tô khách loại 45 chỗ ngồi chuyển động từ giữa sân trường ra cổng trường.\nC. Một bạn học sinh đi từ nhà ra cổng.\nD. Một bạn học sinh đi từ cuối lớp lên bục giảng.",
    "dap_an": [
      "Đáp án đúng là A.",
      "A - đúng vì trường hợp này kích thước của xe máy rất nhỏ so với độ dài của quãng đường.",
      "B - sai vì kích thước của ô tô khách đáng kể so với độ dài quãng đường của nó.",
      "C - sai vì kích thước của bạn học sinh đáng kể so với quãng đường bạn học sinh di chuyển.",
      "D - sai vì kích thước của bạn học sinh đáng kể so với quãng đường bạn học sinh di chuyển."
    ]
  }
for input_data in input_datas:
    # Xử lý
    lines = input_data["cau_hoi"].split("\n")
    cau_hoi_chinh = lines[0]
    cac_lua_chon = "\n" + "\n".join(lines[1:])  # xuống dòng đầu tiên để đúng định dạng
    chuoi = input_data["dap_an"][0]
    text = re.search(r"\b([A-D])\b", chuoi)
    text = text.group(1)
    
    giai_thich =""
    # print((chuoi[len(chuoi)-2]))
    if len(input_data["dap_an"])>2:
        for i in range (1,len(input_data["dap_an"])):
            dapan = input_data["dap_an"][i]
            if dapan[0] == text:
                giai_thich = "\n".join([
            input_data["dap_an"][0],
            input_data["dap_an"][i]
        ])
    else:
        giai_thich = "\n".join([
            input_data["dap_an"][0],
            input_data["dap_an"][1]])




    # Tạo đầu ra theo đúng định dạng bạn muốn
    output = {
        "cau_hoi": cau_hoi_chinh,
        "cac lua chon": cac_lua_chon,
        "giai thich": giai_thich
    }

    print(output["cau_hoi"])
    print(output["cac lua chon"])
    print(output["giai thich"])
