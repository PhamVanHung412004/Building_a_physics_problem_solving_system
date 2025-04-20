import re
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)

list_url = ['https://www.vietjack.com/vat-li-11-kn/index.jsp',  # doi link
            'https://www.vietjack.com/vat-li-11-ct/index.jsp',
            'https://www.vietjack.com/vat-li-11-cd/index.jsp']

ds_cau_hoi = []
for url in list_url:
    driver.get(url)

    menu = driver.find_element(By.CSS_SELECTOR, "ul.nav.nav-list.primary.left-menu")
    items = menu.find_elements(By.TAG_NAME, "li")

    data = []
    pattern = re.compile(r"^Bài\s*")

    for item in items:
        try:
            a = item.find_element(By.TAG_NAME, "a")
            ten_bai = a.text.strip()
            link_bai = a.get_attribute("href")

            if pattern.search(ten_bai):
                data.append({
                    "ten_bai": ten_bai,
                    "link": link_bai
                })
        except:
            continue

    print(f"Số lượng bài: {len(data)}")

    for link in data:
        driver.get(link["link"])
        print(f"Đang mở: {link['ten_bai']}")

        content = driver.find_element(By.CSS_SELECTOR, "div.col-md-7.middle-col")
        links = content.find_elements(By.TAG_NAME, "a")

        for a in links:
            text = a.text.strip()
            href = a.get_attribute("href")
            if href and "Vật Lí 11:" in text:  # sua lop
                match = re.search(r'/vat-li-11-[^/]+/', href)  # sua lop
                if match:
                    ds_cau_hoi.append({
                        "text": text,
                        "link": href
                    })

with open("danh_sach_cau_hoi_vat_li_11.json", "w", encoding="utf-8") as f:  # sua lop
    json.dump(ds_cau_hoi, f, ensure_ascii=False, indent=2)

with open("danh_sach_cau_hoi_vat_li_11.json", "r", encoding="utf-8") as f:  # sua lop
    danh_sach = json.load(f)

ket_qua = []

for i, cau in enumerate(danh_sach):
    driver.get(cau["link"])
    print(f"Đang mở: {cau['text']} ({i + 1}/{len(danh_sach)})")

    try:
        questions_div = driver.find_element(By.CSS_SELECTOR, "div.col-md-7.middle-col")
        all_elements = questions_div.find_elements(By.XPATH, ".//*")

        question_found = False
        solution_found = False
        question_text = ""
        solution_text = ""

        for element in all_elements:
            text = element.text.strip()

            if not question_found and text[:30] == cau["text"][:30]:
                question_found = True
                question_text = text

            if question_found and not solution_found:
                if "Lời giải:" in text:
                    solution_found = True
                elif text:
                    question_text += " " + text

            if solution_found:
                if "chi tiết khác:" in text:
                    break
                elif text:
                    solution_text += " " + text

        if question_text and solution_text:
            ket_qua.append({
                "cau_hoi": question_text,
                "loi_giai": solution_text
            })

    except Exception as e:
        print(f"Không thể mở trang {cau['link']} hoặc gặp lỗi: {e}")

driver.quit()

with open("cau_hoi_11.json", "w", encoding="utf-8") as f:  # sua lop
  json.dump(ket_qua, f, ensure_ascii=False, indent=2)
