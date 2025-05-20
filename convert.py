import os
import json
import csv

output_file = 'bai.csv'
write_header = not os.path.exists(output_file)

with open(r"D:\Building_a_physics_problem_solving_system\dataset_clean_pratice\dap_an_lop12_cleaned.json", 'r', encoding="utf-8") as file:
    data = json.load(file)

with open(output_file, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    if write_header:
        writer.writerow(['Cau_hoi', 'Dap_an', 'Embedding'])  # Ghi header nếu file chưa tồn tại

    for item in data:
        writer.writerow([item.get('Cau_hoi', ''), item.get('Dap_an', ''), 'embedding'])


