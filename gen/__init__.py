import os
from groq import Groq

client = Groq(api_key="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")

class Answer_Question_From_Documents:
    def __init__(self,question : str, documents : list[str]) -> None:
        self.question = question
        self.documents = documents

    def run(self) :
        context = "\n".join(self.documents)  # Tạo chuỗi context bên ngoài f-string
        input_text = f"""Question: {self.question}
        Context: {context}
        Answer:"""
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", 
                 "content": "Bạn luôn phải trả lời bằng tiếng Việt, không dùng tiếng Anh."
                },
                {
                    "role": "user",
                    "content": self.question
                },
                {
                    "role": "assistant",
                    "content": input_text
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        return completion.choices[0].message.content
