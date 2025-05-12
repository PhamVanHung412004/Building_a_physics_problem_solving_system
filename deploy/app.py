from package import (
    SentenceTransformer,
    streamlit as st,
    os,
    Image,
    io,
    uuid,
    faiss
)
from huggingface_hub import hf_hub_download
from datetime import datetime

from read_file import Read_File_CSV

from RAG import (
    Sematic_search,
    Answer_Question_From_Documents
)


import time
# Configure page
st.set_page_config(
    page_title="ChatGPT Clone",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")
model = load_model()

@st.cache_resource
def load_vector_database():
    faiss_path = hf_hub_download(
        repo_id="PVH412004/Model_vectorDB",    # Thay bằng tên repo của bạn
        filename="vector_database.faiss" # Tên file trên Huggingface
    )
    # Load FAISS index
    index = faiss.read_index(faiss_path)
    return index

index = load_vector_database()

def typewriter_effect(text, placeholder, chunk_size=3, speed=0.03):
    """Hiệu ứng gõ chữ từ từ giống ChatGPT."""
    typed_text = ""
    for i in range(0, len(text), chunk_size):
        typed_text += text[i:i + chunk_size]
        placeholder.markdown(f"<p style='font-size:18px; line-height:1.5;'>{typed_text}</p>", unsafe_allow_html=True)
        time.sleep(speed)

def generate_response(use_query):
    try:
        list_index = Sematic_search(model, index, use_query,3).run()
        vector_tmp = list_index[0]
        vector = [int(i) for i in vector_tmp]
        datas = Read_File_CSV("dataset.csv").Read()

        list_context = [datas["Dap_an"][i] for i in vector]
        answer = Answer_Question_From_Documents(use_query,list_context).run()

        return answer

    except ZeroDivisionError as e:     
        return "Lỗi: {}".format(e)


def send_message():
    user_input = st.session_state["user_input"]
    if user_input:
        process_message()
        st.session_state["user_input"] = ""  # Xóa nội dung sau khi gửi

def colored_text(text : str, color : str) -> str:
    return f"<span style='color:{color}'>{text}</span>"



# Load custom CSS
def load_css():
    with open("static/custom.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "is_sidebar_expanded" not in st.session_state:
    st.session_state.is_sidebar_expanded = True
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []
if "need_rerun" not in st.session_state:
    st.session_state.need_rerun = False
    
# Function to toggle sidebar sections
def toggle_section(section_name):
    if section_name not in st.session_state:
        st.session_state[section_name] = False
    st.session_state[section_name] = not st.session_state[section_name]

def convert_to_html(content, is_user):
    class_name = "user-message" if is_user else "bot-message"
    sender = "Bạn " if is_user else "Chatbot "
    timestamp = datetime.now().strftime("%H:%M")
    
    return f"""
    <div class="{class_name}-container">
        <div class="{class_name}">
            <div class="message-header">
                <span class="message-sender">{sender}</span>
                <span class="message-time">{timestamp}</span>
            </div>
            <div class="message-content">
                {content}
            </div>
        </div>
    </div>
    """

def display_file(file_data, file_type, file_name):
    if file_type.startswith('image/'):
        encoded = base64.b64encode(file_data).decode()
        return f"""
        <div class="uploaded-file">
            <p>{file_name}</p>
            <img src="data:{file_type};base64,{encoded}" width="300">
        </div>
        """
    else:
        # For text, pdf, or other files just show a link-like display
        return f"""
        <div class="uploaded-file">
            <p>{file_name}</p>
            <div class="file-icon">📄</div>
        </div>
        """

def process_message():
    if st.session_state.user_input or st.session_state.uploaded_files:
        # First add user message
        user_content = ""
        
        # Add text message if any
        if st.session_state.user_input:
            user_content += f"<p>{st.session_state.user_input}</p>"
        
        # Add any uploaded files
        for file in st.session_state.uploaded_files:
            file_content = file.read()
            file_html = display_file(file_content, file.type, file.name)
            user_content += file_html
        
        # Add to chat history
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_content,
            "time": datetime.now().strftime("%H:%M")
        })
        placeholder = st.empty()
        # Generate bot response
        if st.session_state.user_input != "":
            # if (st.session_state.user_input != ""):
            bot_response = generate_response(st.session_state.user_input)
        else:
            bot_response = "Tôi đã nhận được file của bạn. Bạn muốn tôi làm gì với file này?"
        

        # Tạo một placeholder để update nội dung liên tục
        placeholder = st.empty()
        typewriter_effect(bot_response, placeholder)
        # Add bot response to history
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": f"<p>{bot_response}</p>",
            "time": datetime.now().strftime("%H:%M")
        })
        
        # Clear input fields
        st.session_state.user_input = ""
        st.session_state.uploaded_files = []
        
        # Set a flag to indicate we need to rerun
        st.session_state.need_rerun = True

# Sidebar content
with st.sidebar:
    # st.markdown('<div class="sidebar-header">Chatbot</div>', unsafe_allow_html=True)

    # New Chat button
    if st.button("➕ New chat"):
        st.session_state.chat_history = []
        st.rerun()
    
    # Sections
    st.markdown("## Lịch sử trò chuyện")
    
    # Display chat history in sidebar if available
    if st.session_state.chat_history:
        for i, message in enumerate(reversed(st.session_state.chat_history)):
            # Create a unique identifier for each message
            message_id = f"msg_{i}"
            
            # Determine prefix based on role
            prefix = " " if message["role"] == "user" else " "
            
            # Get the text content (extract from HTML if needed)
            content = message["content"]
            # Simple approach to extract text - might need refinement for complex HTML
            if "<p>" in content and "</p>" in content:
                text_preview = content.split("<p>")[1].split("</p>")[0]
                if len(text_preview) > 30:
                    text_preview = text_preview[:30] + "..."
            else:
                text_preview = "Media message"
                
            # Display the message in sidebar
            st.button(f"{prefix} {text_preview}", key=message_id)
    

# Main chat interface
load_css()

# Display header
# st.markdown('<div class="chat-header">Chatbot</div>', unsafe_allow_html=True)

# Display welcome message if chat is empty
if not st.session_state.chat_history:
    st.markdown('<div class="welcome-container"><h2>Tôi là một chuyên gia giải vật lý bạn có thắc mắc gì về vật lý?</h2></div>', unsafe_allow_html=True)

# Display chat messages
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        is_user = message["role"] == "user"
        st.markdown(convert_to_html(message["content"], is_user), unsafe_allow_html=True)
    # for i in range(len(st.session_state.chat_history) - 1, -1, -2):
    #     user_message = st.session_state.chat_history[i - 1] if i - 1 >= 0 else None
    #     bot_message = st.session_state.chat_history[i]

    #     if user_message:
    #         st.markdown(convert_to_html(user_message["content"], True), unsafe_allow_html=True)
    #     if bot_message:
    #         st.markdown(convert_to_html(bot_message["content"], False), unsafe_allow_html=True)
    # for message in reversed(st.session_state.chat_history):
    #     is_user = message["role"] == "user"
    #     st.markdown(convert_to_html(message["content"], is_user), unsafe_allow_html=True)

# Message input area
st.markdown('<div class="input-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 12, 1])

st.markdown("""
    <style>
    /* Tùy chỉnh placeholder */
    ::placeholder {
        color: white !important;
        opacity: 0.7;
    }
    
    /* Tùy chỉnh ô input */
    input {
        color: white !important;
        background-color: #2b2b2b !important;
        height: 38px !important; /* Đặt chiều cao cố định cho đồng đều */
        border-radius: 5px;
    }
    
    /* Tùy chỉnh button để đồng bộ chiều cao */
    button {
        height: 38px !important; /* Cùng chiều cao với input */
        margin-left: 5px;
    }

    /* Tạo layout hàng ngang (flex) */
    .stTextInput {
        display: flex;
        align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)



with col2:
    user_input = st.text_input("", key="user_input", placeholder="Nhập câu hỏi của bạn...",on_change=send_message)
    
with col3:
    try:
        if st.button("Gửi"):
            send_message()
    except:
        print("Error")
st.markdown('</div>', unsafe_allow_html=True)

# Tự động scroll xuống dưới cùng khi có tin nhắn mới
st.markdown("""
<script>
    const chatContainer = window.parent.document.querySelector('.stApp main');
    chatContainer.scrollTop = chatContainer.scrollHeight;
</script>
""", unsafe_allow_html=True)

# Check if we need to rerun the app (for processing messages)
if st.session_state.need_rerun:
    st.session_state.need_rerun = False
    st.rerun()
