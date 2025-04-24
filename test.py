
from read_file import Read_File_Json

def main():
    data = Read_File_Json("/home/fit/PhamVanHung/project/Building_a_physics_problem_solving_system/500_trac_nghiem_10.json").Read()
    for i in range(len(data)):
        print(i)
main()