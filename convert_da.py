import json

def convert(datas: list):
    result = []
    for data in datas:
        di = {}
        di["title"] = data["title"]
        di["cau_hoi"] = data["cau_hoi"]

        if data["title"] == "trac nghiem":
            di["cac_lua_chon"] = data["cac_lua_chon"]

           
            s = data["giai_thich"].split("\n")
            if "Đáp án đúng" in s[0]:
                s[0], s[-1] = s[-1], s[0]  
            ghep = "\n".join(s).strip()
            di["giai_thich"] = ghep
        else:
            di["giai_thich"] = data["giai_thich"]

        result.append(di)

    return result

def main():
    path = "datas.json"
    with open(path, 'r', encoding='utf-8') as f:
        datas = json.load(f)
    kq = convert(datas)
    with open('data_process.json', 'w', encoding='utf-8') as f:
        json.dump(kq, f, ensure_ascii=False, indent=4)

main()
