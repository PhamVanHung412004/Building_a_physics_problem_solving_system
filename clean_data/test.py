from add_path import add
add()
from package import Path
from read_file import Read_File_Json


def main():
    datas = Read_File_Json("/home/phamvanhung/project/Building_a_physics_problem_solving_system/clean_data/data_fine_turning/data_trac_nghiem_12.json").Read()
    datas1 = Read_File_Json("/home/phamvanhung/project/Building_a_physics_problem_solving_system/clean_data/500_cau_hoi_trac_nghiem/500_trac_nghiem_12.json").Read()

    index = []
    for i in range(len(datas)):
        for j in range(len(datas1)):
            if (datas[i]["cau_hoi"] in datas1[j]["cau_hoi"]):
                index.append(j)
    print(len(index))
    for i in range(len(datas1)):
        if (i not in index):
            print(i)
main()