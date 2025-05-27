
from read_file import Read_File_CSV 
from package import (
    Path,
    pandas,
    List,
    Dict
    
)

# Convert to datatype list
def conver_datatype(data : pandas) -> List[str | int]:
    return list(data)


# Meger feature
def meger_file_csv(dataset : pandas, data_practice : pandas) -> Dict[str, List[str | float]]:
    data : Dict[str , List[str | float]] = {
        "Cau_hoi" : conver_datatype(dataset["Cau_hoi"]) + conver_datatype(data_practice["Cau_hoi"]),
        "Dap_an" : conver_datatype(dataset["Dap_an"]) + conver_datatype(data_practice["Dap_an"]),
        "Embedding" : conver_datatype(dataset["Embedding"]) + conver_datatype(data_practice["Embedding"]),
    }
    return data

def main() -> None:
    # Read file dataset.csv
    path_dir_dataset : str = str(Path(__file__).parent / "dataset.csv")
    data_new_dataset : pandas = Read_File_CSV(path_dir_dataset).Read()

    # Read file embedding_practice.csv
    path_dir_practice : str = str(Path(__file__).parent / "embedding_practive.csv")
    data_new_pratice : pandas = Read_File_CSV(path_dir_practice).Read()
    
    # Meger two file dataset.csv and embedding_practice.csv
    data_new : Dict[str, List[str, float]] = meger_file_csv(data_new_dataset,data_new_pratice)

    # Diractory save data final
    dir_save_dataset_final : str = str(Path(__file__).parent / "deploy" / "dataset.csv")

    # Convert dict to pandas
    data_final : pandas = pandas.DataFrame(data_new)
    
    # Save data final
    data_final.to_csv(dir_save_dataset_final, index=False, encoding="utf-8")

main()
