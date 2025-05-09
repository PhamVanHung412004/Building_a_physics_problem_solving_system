import streamlit as st
import random


def generate_response(prompt):
    """
    Function to generate a response for the chat
    In a real application, this would connect to an AI model
    For this demo, it returns predefined Vietnamese responses
    """
    responses = [
        "Xin chào! Tôi có thể giúp gì cho bạn?",
        "Tôi đang xử lý yêu cầu của bạn.",
        "Câu hỏi thật thú vị. Hãy để tôi trả lời.",
        "Tôi là một trợ lý AI được tạo ra để hỗ trợ bạn.",
        "Rất vui được trò chuyện với bạn!",
        "Tôi có thể giúp bạn tìm kiếm thông tin hoặc trả lời các câu hỏi.",
        "Vui lòng cho tôi biết nếu bạn cần thêm thông tin.",
        "Cảm ơn bạn đã đặt câu hỏi này.",
        "Đây là một chủ đề thú vị để thảo luận.",
        "Tôi đang học hỏi và cải thiện mỗi ngày."
    ]

    # For a simple demo, just return a random response
    # In a real implementation, this would call an actual AI model
    return random.choice(responses)
