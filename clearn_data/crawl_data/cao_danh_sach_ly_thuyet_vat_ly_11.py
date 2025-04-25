import json
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import re

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

list_url = [
    "https://www.vietjack.com/vat-li-11-kn/ly-thuyet-vat-li-lop-11.jsp",
    "https://www.vietjack.com/vat-li-11-ct/ly-thuyet-vat-li-lop-11.jsp",
    "https://www.vietjack.com/vat-li-11-cd/ly-thuyet-vat-li-lop-11.jsp"
]

driver = webdriver.Chrome(options=chrome_options)

data = []

for url in list_url:
    driver.get(url)
    time.sleep(2)

    links = driver.find_elements(By.CSS_SELECTOR, "ul.left-menu a")

    pattern = re.compile(r'\bBài\b\s*\d+\s*:', re.IGNORECASE)
    for link in links:
        title = link.text.strip()
        href = link.get_attribute("href")
        if title and href and pattern.search(title):
            data.append({"title": title, "url": href})

with open("danh_sach_ly_thuyet_vat_li_11.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# ---------------------------------------------------------------------------------------------------------------------
json_path = "danh_sach_ly_thuyet_vat_li_11.json"

with open(json_path, "r", encoding="utf-8") as f:
    lessons = json.load(f)


def clean_heading(text):
    return re.sub(r"^([IVXLCDM]+\.)|^(\d+\.)|^([a-z]\))", "", text).strip()


all_lessons = []

for i, lesson in enumerate(lessons, start=1):
    driver.get(lesson["url"])
    print(f"Đang mở: {lesson['title']} ({i}/{len(lessons)})")
    time.sleep(2)

    main_content = driver.find_element(By.CLASS_NAME, "col-md-7.middle-col")
    paragraphs = main_content.find_elements(By.XPATH, ".//p")

    theory_dict = {}
    current_key = None

    for el in paragraphs:
        text = el.text.strip()
        if not text:
            continue

        bold_tags = el.find_elements(By.TAG_NAME, "b") + el.find_elements(By.TAG_NAME, "strong")

        if bold_tags:
            candidate_key = bold_tags[0].text.strip()

            if len(candidate_key) <= 1 or candidate_key in ["-", "–", "•"]:
                if current_key:
                    theory_dict[current_key] += text + "\n"
                continue

            current_key = candidate_key
            theory_dict[current_key] = ""
        elif current_key:
            theory_dict[current_key] += text + "\n"

    for key in theory_dict:
        theory_dict[key] = theory_dict[key].strip()

    invalid_keywords_in_key = ["Lý thuyết Vật Lí 11 Bài"]
    invalid_keywords_in_value = ["VietJack"]

    for key in list(theory_dict.keys()):
        content = theory_dict[key].strip()

        if not content or any(kw in key for kw in invalid_keywords_in_key) or any(kw in content for kw in invalid_keywords_in_value):
            del theory_dict[key]
            continue

        theory_dict[key] = content

    cleaned_theory_dict = {}
    for key, value in theory_dict.items():
        new_key = clean_heading(key)
        cleaned_theory_dict[new_key] = value

    all_lessons.append({
        "title": lesson["title"],
        "url": lesson["url"],
        "content": cleaned_theory_dict
    })

with open("ly_thuyet_11.json", "w", encoding="utf-8") as f:
    json.dump(all_lessons, f, ensure_ascii=False, indent=2)

driver.quit()
