from add_path import add
add()

from read_file import Read_File_Json
from save_file_json import Save_File_Json
from package import (
    Path,
    re,
    BeautifulSoup
)

from solution_string import (
    solution,
    clean_mathml,
    clean_question,
    fix_spacing_and_comma,
)

def main():
    datas = []
    for i in range(11,13):
        path = Path(__file__).parent/ "500_cau_hoi_trac_nghiem" / "500_trac_nghiem_{}.json".format(i)
        texts = Read_File_Json(path).Read()
        
        for text in texts:
            cauhoi, luachon = clean_question(text["cau_hoi"])
            ts = text["dap_an"]
            cleaned_ds = []
            for t in ts:
                left, right = solution(t)                        
                
                if (left != -1 and right != -1):
                    cleaned_mathml = clean_mathml(t[left : right + 1])
                    cleaned_mathml = fix_spacing_and_comma(cleaned_mathml)
                    cleaned_ds.append(cleaned_mathml)
                else:                
                    cleaned_ds.append(t)
            
            text_answers = "\n".join([i for i in cleaned_ds if (i != "")])
            selection = luachon.split("\n")
            
            if (len(selection) != 1):                        
                ds = {}
                ds["title"] = "trac nghiem"
                ds["cau_hoi"] = cauhoi
                ds["cac_lua_chon"] = selection
                ds["giai_thich"] = text_answers
                datas.append(ds)
    path_save = Path(__file__).parent/ "data_fine_turning" / "data_fine_turning.json"
    Save_File_Json(str(path_save),datas).save()    

main()