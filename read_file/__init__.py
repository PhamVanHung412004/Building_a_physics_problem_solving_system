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
    
    def Read(self)-> pd :
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










