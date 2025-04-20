import json

# Đọc file gốc có mã hóa Unicode escape
with open("/home/fit/Building_a_physics_problem_solving_system/output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Ghi lại dữ liệu vào file mới với định dạng tiếng Việt dễ đọc
new_file_path = "cau_hoi_vat_ly_tieng_viet.json"
with open(new_file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

new_file_path
