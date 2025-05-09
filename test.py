from package import (
    os,
    streamlit as st,
    SentenceTransformer,
    faiss
)

from RAG import (
    Sematic_search,
    Answer_Question_From_Documents,
)

from read_file import Read_File_CSV






def colored_text(text : str, color : str) -> str:
    return f"<span style='color:{color}'>{text}</span>"

def typewriter_effect(text, speed=0.03):
    display_text = ""
    for char in text:
        display_text += char
        placeholder.markdown(f"""
            <div style="
                background-color: #E6F4FF; 
                padding: 15px; 
                border-radius: 10px; 
                margin-bottom: 10px; 
                border-left: 4px solid #4169E1; 
                color: black; 
                font-family: 'Courier New', monospace;
                font-size: 16px;
            ">
                {display_text}
            </div>
        """, unsafe_allow_html=True)
        time.sleep(speed)

# Page configuration
st.set_page_config(
    page_title="Trợ lý Vật lý AI",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_resource
def Vector_Database() -> faiss:
    index : faiss = faiss.read_index("vector_database/vector_database.faiss")
    return index

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()
vector_database = Vector_Database()
# Đảm bảo màu nền và các màu chính được áp dụng mạnh hơn
st.markdown("""
<style>
    /* Thiết lập cụ thể màu sắc không phụ thuộc vào cấu hình theme */
    :root {
        --primary-color: #4169E1;
        --background-color: #F0F8FF;
        --secondary-bg-color: #E6E6FA;
        --text-color: #333333;
    }
    
    /* Màu nền cho toàn bộ ứng dụng */
    body {
        background-color: var(--background-color) !important;
        color: var(--text-color) !important;
    }
    
    /* Màu cho các thành phần chính */
    .stApp {
        background-color: var(--background-color) !important;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: var(--secondary-bg-color) !important;
    }
    
    /* Các nút và widget */
    button, .stButton button, .stTextInput input, .stTextArea textarea {
        border-color: var(--primary-color) !important;
    }
    
    button:hover, .stButton button:hover {
        border-color: var(--primary-color) !important;
        color: var(--primary-color) !important;
    }
    
    /* Header */
    h1, h2, h3, h4, h5, h6 {
        color: var(--primary-color) !important;
    }
</style>
""", unsafe_allow_html=True)

# Custom styling
st.markdown("""
<style>
    /* Kiểu dáng tổng thể */
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Kiểu cho tin nhắn trong chat */
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.75rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .chat-message.user {
        background-color: #E6F4FF;
        border-left: 5px solid #4169E1;
    }
    .chat-message.assistant {
        background-color: #F0F0F0;
        border-left: 5px solid #9370DB;
    }
    .chat-message .message-content {
        margin-left: 0.5rem;
        padding-left: 1rem;
        line-height: 1.6;
    }
    .chat-message:hover {
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    
    /* Kiểu cho sidebar */
    .stSidebar .sidebar-content {
        padding: 1rem;
    }
    .chat-history-item {
        padding: 0.75rem;
        margin-bottom: 0.5rem;
        border-radius: 0.5rem;
        background-color: #F0F0F0;
        font-size: 0.9rem;
        border-left: 3px solid #4169E1;
        transition: all 0.2s ease;
    }
    .chat-history-item:hover {
        background-color: #E6F4FF;
        transform: translateX(3px);
    }
    
    /* Kiểu cho header */
    .app-header {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 2rem;
        background: linear-gradient(to right, #E6F4FF, #F0F8FF);
        padding: 1rem;
        border-radius: 10px;
    }
    .header-title {
        font-size: 1.8rem;
        font-weight: bold;
        color: #4169E1;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .physics-icon {
        height: 3.5rem;
        margin-right: 0.5rem;
        animation: pulse 2s infinite;
    }
    
    /* Kiểu cho câu hỏi gợi ý */
    .suggestion-box {
        background-color: #E6F4FF;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 8px;
        cursor: pointer;
        border-left: 3px solid #4169E1;
        transition: all 0.2s ease;
    }
    .suggestion-box:hover {
        background-color: #D1E6FF;
        transform: translateY(-2px);
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }
    
    /* Hiệu ứng */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .chat-message {
            padding: 1rem;
        }
        .header-title {
            font-size: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Custom styling
st.markdown("""
<style>
    /* Kiểu dáng tổng thể */
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }

    ... (giữ nguyên các style cũ)

    /* Đổi màu viền và nền của ô chat_input */
    div.stChatInputContainer {
        border: 2px solid white !important;
        border-radius: 25px !important;
        background-color: #000 !important;
        padding: 4px !important;
    }

    div.stChatInputContainer input {
        color: white !important;
        background-color: transparent !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)


# Mẫu câu hỏi vật lý đề xuất
sample_questions = [
    "Định luật Newton nói gì về chuyển động?",
    "Công thức E=mc² có ý nghĩa gì?",
    "Tại sao bầu trời có màu xanh?",
    "Ánh sáng có phải là sóng hay hạt?",
    "Định luật Ohm áp dụng như thế nào trong mạch điện?",
    "Thuyết tương đối của Einstein giải thích hiện tượng gì?"
]

# App header với hiệu ứng đẹp
st.markdown('''
<div class="app-header">
    <div>
        <svg class="physics-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#4169E1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(45 12 12)"></ellipse>
            <ellipse cx="12" cy="12" rx="10" ry="4" transform="rotate(-45 12 12)"></ellipse>
            <circle cx="12" cy="12" r="1"></circle>
        </svg>
    </div>
    <div class="header-title">Trợ lý Vật lý AI</div>
</div>
''', unsafe_allow_html=True)

# Hiển thị giới thiệu chính và câu hỏi gợi ý
st.markdown("### Hãy đặt câu hỏi về vật lý và tôi sẽ giúp bạn giải đáp!")

# Hiển thị câu hỏi mẫu trong 2 cột
st.markdown("#### 💡 Một số câu hỏi gợi ý:")
col1, col2 = st.columns(2)
with col1:
    for q in sample_questions[:3]:
        # st.markdown(f"""
        # <div style="background-color: #E6F4FF; padding: 10px; border-radius: 8px; margin-bottom: 8px; cursor: pointer; border-left: 3px solid #4169E1;" 
        #      onclick="document.querySelector('.stChatInputContainer input').value='{q}';document.querySelector('.stChatInputContainer button').click();">
        #     {q}
        # </div>
        # """, unsafe_allow_html=True)
        st.markdown(f"""
        <div style="background-color: #E6F4FF; padding: 10px; border-radius: 8px; margin-bottom: 8px; cursor: pointer; border-left: 3px solid #4169E1; color: black;" 
             onclick="document.querySelector('.stChatInputContainer input').value='{q}';document.querySelector('.stChatInputContainer button').click();">
            {q}
        </div>
        """, unsafe_allow_html=True)
with col2:
    for q in sample_questions[3:]:
        st.markdown(f"""
        <div style="background-color: #E6F4FF; padding: 10px; border-radius: 8px; margin-bottom: 8px; cursor: pointer; border-left: 3px solid #4169E1; color: black;" 
             onclick="document.querySelector('.stChatInputContainer input').value='{q}';document.querySelector('.stChatInputContainer button').click();">
            {q}
        </div>
        """, unsafe_allow_html=True)

# Initialize session state
list_chat_history = []

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": colored_text("Xin chào! Tôi là trợ lý AI chuyên về Vật Lý. Hãy đặt câu hỏi và tôi sẽ cố gắng giải đáp cho bạn.","black")}]
# Lấy nội dung lời chào
# Main content area with chat display
chat_container = st.container()

with chat_container:
    # Display chat messages
    for message in st.session_state.messages:
        print("test: ",message["role"])
        with st.chat_message(message["role"]):
            message_class = "assistant" if message["role"] == "assistant" else "user"
            st.markdown(f'<div class="chat-message {message_class}"><div class="message-content">{message["content"]}</div></div>', unsafe_allow_html=True)

# Sidebar with chat history and information
with st.sidebar:
    # Logo và tiêu đề sidebar 
    st.markdown("""
    <div style="display: flex; align-items: center; margin-bottom: 20px;">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 4.75L19.25 9L12 13.25L4.75 9L12 4.75Z" stroke="#4169E1" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M4.75 14L12 18.25L19.25 14" stroke="#4169E1" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M4.75 9V14" stroke="#4169E1" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M19.25 9V14" stroke="#4169E1" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span style="font-size: 1.3rem; font-weight: bold; margin-left: 10px; color: #4169E1;">Trợ lý Vật lý</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## 📚 Lịch sử trò chuyện")
    st.markdown('<div style="border-top: 2px solid #E6F4FF; margin: 10px 0;"></div>', unsafe_allow_html=True)
    print("context :", st.session_state.messages)
    if len(st.session_state.messages) > 1:  # Skip the initial greeting
        for i, message in enumerate(st.session_state.messages):        
            st.markdown(f"""
            <div class="chat-history-item">
                <div style="font-weight: bold; color: #4169E1; margin-bottom: 5px;">📝 Câu hỏi:</div>
                <div>{message["content"]}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown('<div style="font-style: italic; color: #777;">Chưa có cuộc trò chuyện nào. Hãy bắt đầu đặt câu hỏi!</div>', unsafe_allow_html=True)

# Function for generating LLM response
def generate_response(use_query):
    try:
        list_index = Sematic_search(model, vector_database, use_query,3).run()
        vector_tmp = list_index[0]
        vector = [int(i) for i in vector_tmp]
        datas = Read_File_CSV("dataset.csv").Read()

        list_context = [datas["Dap_an"][i] for i in vector]
        answer = Answer_Question_From_Documents(use_query,list_context).run()
        return answer

    except ZeroDivisionError as e:
        title = e
        return "Lỗi: {}".format(title)

# User input area at the bottom
prompt = st.chat_input("Nhập câu hỏi về vật lý của bạn...")
# Process user input
if prompt:
    try:
        # Format question to end with question mark
        prompt = prompt.replace(".", "?")
        if prompt[-1] != '?':
            if prompt[-1] == '.':
                prompt = prompt[:-1] + '?'
            else:
                prompt += '?'
    
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": prompt})
    
        with st.chat_message("user"):
            st.markdown(f'<div class="chat-message user"><div class="message-content">{prompt}</div></div>', unsafe_allow_html=True)
    
        # Generate a response
        if st.session_state.messages[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Đang suy nghĩ..."):
                    response = generate_response(prompt)
                    st.markdown(f'''
                    <style>
                        .chat-message .message-content {{
                            color: black;
                        }}
                    </style>
                    <div class="chat-message assistant">
                        <div class="message-content">{response}</div>
                    </div>''', unsafe_allow_html=True)
                    message = {"role": "assistant", "content": response}
                    st.session_state.messages.append(message)
                    st.rerun()  # Update the UI to show the new message immediately

    except Exception as e:
        with st.chat_message("assistant"):    
            st.error(f"Lỗi: {str(e)}")

