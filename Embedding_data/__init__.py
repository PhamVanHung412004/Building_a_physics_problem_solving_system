class Get_Embedding:
    def __init__(self,model,text):
        '''
        model: model dùng trong quá trình chuyển vecto
        text: dữ liệu đầu vào dưới dạng text
        '''
        self.model = model
        self.text = text

    def use_model(self):
        text_vector = self.model.encode(self.text)
        return text_vector





