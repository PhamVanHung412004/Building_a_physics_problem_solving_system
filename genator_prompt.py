from transformers import AutoTokenizer

# Khởi tạo tokenizer từ mô hình pre-trained
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

def generate_prompt_general(question_theory=None, question_practice=None, question_mcq=None, choices=None, explanation=None):
    """
    Tạo prompt linh hoạt tùy theo loại câu hỏi có: lý thuyết, bài tập tự luận, hoặc trắc nghiệm.

    Args:
    - question_theory: (str or None) Câu hỏi lý thuyết
    - question_practice: (str or None) Bài tập thực hành (tự luận)
    - question_mcq: (str or None) Câu hỏi trắc nghiệm
    - choices: (str or None) Các lựa chọn trắc nghiệm
    - explanation: (str) Lời giải, lời giải thích hoặc đáp án
    
    Returns:
    - prompt: (str) Prompt đầu vào cho fine-tuning hoặc mô hình
    """

    system_prompt = """
    <|im_start|>system
    Bạn là một chuyên gia vật lý. Bạn sẽ nhận các câu hỏi bao gồm lý thuyết, bài tập thực hành và câu hỏi trắc nghiệm. 
    Bạn cần giải thích lý thuyết, giải bài tập một cách chi tiết và chọn phương án đúng cho câu hỏi trắc nghiệm.
    """.strip()

    user_prompt = "<|im_start|>user\n"
    
    if question_theory:
        user_prompt += f"### Câu hỏi lý thuyết:\n{question_theory}\n\n"

    if question_practice:
        user_prompt += f"### Bài tập thực hành:\n{question_practice}\n\n"

    if question_mcq:
        user_prompt += f"### Câu hỏi trắc nghiệm:\n{question_mcq}\n"
        if choices:
            user_prompt += f"### Các lựa chọn:\n{choices}\n\n"

    assistant_prompt = f"<|im_start|>assistant\n{explanation.strip() if explanation else ''}"

    full_prompt = f"{system_prompt}\n\n{user_prompt}{assistant_prompt}"

    return full_prompt.strip()



def generate_and_tokenize_prompt(question_theory, question_practice, choices, explanation):
    """
    Tạo và token hóa prompt cho việc fine-tuning.

    Args:
    - question_theory: Câu hỏi lý thuyết
    - question_practice: Bài tập thực hành
    - choices: Các lựa chọn trắc nghiệm
    - explanation: Giải thích câu trả lời

    Returns:
    - tokenized_full_prompt: Prompt đã được token hóa
    """
    # Tạo full prompt
    full_prompt = generate_prompt(question_theory, question_practice, choices, explanation)
    
    # Tokenize prompt
    tokenized_full_prompt = tokenizer(
        full_prompt,
        padding=True,       # Đệm các câu ngắn lại để có chiều dài đồng nhất
        truncation=True,    # Cắt bớt văn bản nếu nó dài quá chiều dài tối đa của mô hình
        return_tensors='pt' # Trả về tensor cho PyTorch (hoặc 'tf' nếu dùng TensorFlow)
    )
    
    return tokenized_full_prompt


# Ví dụ sử dụng:
question_theory = "Giải thích định lý bảo toàn năng lượng trong cơ học."
question_practice = "Một vật nặng 5kg rơi từ độ cao 10m. Tính tốc độ của vật khi chạm đất (giả sử không có ma sát)."
choices = "A. 10 m/s\nB. 14 m/s\nC. 15 m/s\nD. 20 m/s"
explanation = """
1. Lý thuyết: Định lý bảo toàn năng lượng cho biết trong một hệ cô lập không có lực bên ngoài, tổng năng lượng cơ học (năng lượng động học + năng lượng thế) luôn được bảo toàn.
2. Bài tập:
   - Năng lượng thế ban đầu: E_p = mgh = 5 * 9.8 * 10 = 490 J
   - Năng lượng động học khi chạm đất: E_k = (1/2) * m * v^2
   - Vì bảo toàn năng lượng, E_p = E_k, nên:
     490 = (1/2) * 5 * v^2
     Giải ra: v = 14 m/s
"""

# Gọi hàm để tạo và token hóa prompt
tokenized_prompt = generate_and_tokenize_prompt(question_theory, question_practice, choices, explanation)

# In kết quả tokenized prompt
print(tokenized_prompt)
