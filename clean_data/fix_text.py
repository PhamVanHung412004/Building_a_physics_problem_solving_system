import sys
import os
# thêm path thủ công 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from package import Dict
import re

def convert(text : str) -> str:
    options = {}
    current_key = None
    current_text = []
    match = re.match(r"^([A-D])\.\s*$", text.strip())  # Chỉ chứa "A.", "B.",...
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
    return " ".join(current_text).strip()


def main():

    text = "Nhiệt dung riêng\nc\n=\nQ\nm\nΔ\nT\ncủa một chất là nhiệt lượng cần thiết để 1 kg chất đó tăng thêm 1K (hoặc 1°C).",
    print(convert(text))
main()
    
