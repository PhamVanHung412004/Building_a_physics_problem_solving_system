from groq import Groq
client : Groq = Groq(api_key="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")

class Answer_Question_From_Documents:
    def __init__(self, question: str, documents: list[str]) -> None:
        self.question : str = question
        self.documents : list[str] = documents

    def run(self):
        context : str = "\n".join(self.documents)
        prompt : str = f"""Dựa vào thông tin sau, hãy trả lời câu hỏi bằng tiếng Việt tự nhiên.

        Thông tin:
        {context}
        
        Câu hỏi:
        {self.question}
        
        Trả lời:"""

        completion : Groq = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "Bạn là một chuyên gia giải bài tập vật lý bạn hãy giải cho tôi bài tập sau bằng Tiếng Việt."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=2000,
            top_p=1.0,
            stream=False,
            stop=None,
        )

        return completion.choices[0].message.content
