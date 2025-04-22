import re
import json
def remove_duplicates(text):
    # Tách theo câu, loại trùng lặp
    sentences = re.split(r'(?<=[.!?])\s+', text)
    seen = set()
    unique = [s for s in sentences if not (s in seen or seen.add(s))]
    return ' '.join(unique)

def normalize_math_expression(text):
    """
    Biến các công thức LaTeX hoặc lỗi định dạng về dạng dễ hiểu như:
    m = k * Δl / g
    """
    text = text.replace("·", "*")
    text = re.sub(r'\\frac{(.+?)}{(.+?)}', r'\1 / \2', text)
    text = re.sub(r'\\cdot', '*', text)
    text = re.sub(r'\\Delta', 'Δ', text)
    text = re.sub(r'\\(.*?\\)', '', text)  # loại bỏ toàn bộ LaTeX nếu còn
    return text

def clean_text_for_embedding(text):
    # 1. Xóa dấu xuống dòng, ký tự thừa
    text = re.sub(r'\s+', ' ', text).strip()

    # 2. Xử lý ký hiệu đặc biệt (nếu có)
    text = text.replace("⇔", "<=>")
    text = text.replace("–", "-")

    # 3. Chuẩn hóa công thức toán học cơ bản
    text = re.sub(r'a\^2\s*\+\s*b\^2\s*=\s*c\^2', 'a^2 + b^2 = c^2', text)  # Định lý Pythagoras
    text = re.sub(r'E\s*=\s*mc\^2', 'E = m * c^2', text)  # Công thức năng lượng Einstein
    text = re.sub(r'm\s*=\s*k\s*\|\s*Δ\s*l\s*\|\s*/\s*g', 'm = k * Δl / g', text)  # Công thức vật lý
    text = re.sub(r'k\s*\|\s*Δ\s*l\s*\|', 'k * Δl', text)  # Công thức vật lý
    text = re.sub(r's\s*=\s*v\s*\.?\s*t', 's = v * t', text)  # Công thức quãng đường
    text = re.sub(r'v\s*=\s*s\s*/\s*t', 'v = s / t', text)  # Công thức vận tốc

    # 4. Thêm công thức vật lý khác
    text = re.sub(r'F\s*=\s*m\s*a', 'F = m * a', text)  # Công thức lực (Newton's Second Law)
    text = re.sub(r'W\s*=\s*F\s*·\s*d', 'W = F * d', text)  # Công thức công (Work)
    text = re.sub(r'P\s*=\s*F\s*/\s*A', 'P = F / A', text)  # Công thức áp suất (Pressure)
    text = re.sub(r'v\s*=\s*v_0\s*+\s*a\s*t', 'v = v_0 + a * t', text)  # Vận tốc sau một thời gian (Motion)
    
    # 5. Công thức vật lý bổ sung
    text = re.sub(r'U\s*=\s*I\s*·\s*R', 'U = I * R', text)  # Công thức điện áp (Ohm's Law)
    text = re.sub(r'P\s*=\s*I\s*·\s*U', 'P = I * U', text)  # Công thức công suất điện (Power)
    text = re.sub(r'E\s*=\s*q\s*·\s*V', 'E = q * V', text)  # Công thức năng lượng điện (Energy)
    text = re.sub(r'F\s*=\s*q\s*·\s*E', 'F = q * E', text)  # Lực tác dụng lên điện tích trong điện trường
    text = re.sub(r'λ\s*=\s*h\s*/\s*p', 'λ = h / p', text)  # Công thức sóng de Broglie (wavelength)
    text = re.sub(r'v\s*=\s*λ\s*·\s*f', 'v = λ * f', text)  # Công thức sóng (speed of wave)
    text = re.sub(r'K.E.\s*=\s*0.5\s*m\s*v\^2', 'K.E. = 0.5 * m * v^2', text)  # Công thức động năng (Kinetic Energy)
    text = re.sub(r'P\s*=\s*ΔE\s*/\s*Δt', 'P = ΔE / Δt', text)  # Công thức công suất (Power)

    # 6. Chuẩn hóa công thức LaTeX nếu còn
    text = normalize_math_expression(text)

    # 7. Loại câu trùng lặp
    text = remove_duplicates(text)

    return text



def main():
    data = clean_text_for_embedding(" Lời giải: Lời giải: Lò xo bị nén là do trọng lượng của vật nén xuống. Lò xo bị nén là do trọng lượng của vật nén xuống. Khi vật nằm tại vị trí cân bằng, độ lớn lực đàn hồi của lò xo bằng với trọng lượng của vật khi đó: Khi vật nằm tại vị trí cân bằng, độ lớn lực đàn hồi của lò xo bằng với trọng lượng của vật khi đó: F\nd\nh\n=\nP\n⇔\nk\n|\nΔ\nl\n|\n=\nm\ng\n⇔\nm\n=\nk\n|\nΔ\nl\n|\ng\n=\n25.0\n,\n04\n9\n,\n8\n=\n0\n,\n102\nk\ng F\nd\nh\n=\nP\n⇔\nk\n|\nΔ\nl\n|\n=\nm\ng\n⇔\nm\n=\nk\n|\nΔ\nl\n|\ng\n=\n25.0\n,\n04\n9\n,\n8\n=\n0\n,\n102\nk\ng F\nd\nh\n=\nP\n⇔\nk\n|\nΔ\nl\n|\n=\nm\ng\n⇔\nm\n=\nk\n|\nΔ\nl\n|\ng\n=\n25.0\n,\n04\n9\n,\n8\n=\n0\n,\n102\nk\ng F\nd\nh\n=\nP\n⇔\nk\n|\nΔ\nl\n|\n=\nm\ng\n⇔\nm\n=\nk\n|\nΔ\nl\n|\ng\n=\n25.0\n,\n04\n9\n,\n8\n=\n0\n,\n102\nk\ng F\nd\nh\n=\nP\n⇔\nk\n|\nΔ\nl\n|\n=\nm\ng\n⇔\nm\n=\nk\n|\nΔ\nl\n|\ng\n=\n25.0\n,\n04\n9\n,\n8\n=\n0\n,\n102\nk\ng F\nd\nh F F F d\nh d\nh d d h h = = P P ⇔ ⇔ k k |\nΔ\nl\n| | | Δ\nl Δ Δ l l | | = = m m g g ⇔ ⇔ m m = = k\n|\nΔ\nl\n|\ng k\n|\nΔ\nl\n|\ng k\n|\nΔ\nl\n| k\n|\nΔ\nl\n| k k |\nΔ\nl\n| | | Δ\nl Δ Δ l l | | g g g = = 25.0\n,\n04\n9\n,\n8 25.0\n,\n04\n9\n,\n8 25.0\n,\n04 25.0\n,\n04 25.0 25.0 , , 04 04 9\n,\n8 9\n,\n8 9 9 , , 8 8 = = 0 0 , , 102 102 k k g g")
    print(data)

main()