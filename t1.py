import re

a = "em ơi A"
match = re.search(r"\b([A-D])\b", a)

if match:
    text = match.group(1)  # Lấy chữ cái A-D
    print(text)            # In ra: A
    if text == "A":
        print("AAAAAAAAAAAAAAAAAAAAAA")
else:
    print("Không tìm thấy ký tự A-D")