
# thêm path thủ công 
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from package import (
#     pandas as pd,
#     PdfReader,
#     Document
# )

# 2 chú thích trên nếu dùng bị lỗi ImportError: cannot import name 'Get_Path' from partially initialized module 'read_file' (most likely due to a circular import) (C:\Users\DELL\Documents\Project LLM\Building_a_physics_problem_solving_system\read_file\__init__.py)

import pandas as pd
from pypdf import PdfReader
from docx import Document



class Get_Path:
    def __init__(self,path:str)->None:
        '''
        path: Đường dẫn đầu vào
        '''
        self.path = path

class Read_File_CSV(Get_Path):
    def __init__(self, path):
        super().__init__(path)
        '''
        Kế thừa đường dẫn từ class Get_Path
        '''
    
    def Read(self)-> pd:
        return pd.read_csv(self.path)
    
class Read_File_PDF(Get_Path):
    def __init__(self, path):
        super().__init__(path)
        '''
        Kế thừa đường dẫn từ class Get_Path
        '''
    
    def Read(self):
        reads = PdfReader(self.path)
        texts = ""
        for read in reads.pages:
            texts += read.extract_text() or ''
        return texts
        

class Read_File_WORD(Get_Path):
    def __init__(self, path):
        super().__init__(path)
        '''
        Kế thừa đường dẫn từ class Get_Path
        '''
    
    def Read(self):
        texts = ""
        docs = Document(self.path)
        
        for doc in docs.paragraphs:
            texts += doc.text
        return texts










