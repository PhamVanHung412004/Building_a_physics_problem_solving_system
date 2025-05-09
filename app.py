import streamlit as st
import base64
from datetime import datetime
import uuid
import os
from PIL import Image
import io
from utils import generate_response

# Configure page
st.set_page_config(
    page_title="ChatGPT Clone",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
    sender = "Bạn" if is_user else "ChatGPT"
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
        
        # Generate bot response
        if st.session_state.user_input:
            bot_response = generate_response(st.session_state.user_input)
        else:
            bot_response = "Tôi đã nhận được file của bạn. Bạn muốn tôi làm gì với file này?"
        
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
        for i, message in enumerate(st.session_state.chat_history):
            # Create a unique identifier for each message
            message_id = f"msg_{i}"
            
            # Determine prefix based on role
            prefix = "👤" if message["role"] == "user" else "🤖"
            
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
    
    st.markdown("---")
    st.markdown('<div class="sidebar-footer">Những câu gợi ý</div>', unsafe_allow_html=True)

# Main chat interface
load_css()

# Display header
st.markdown('<div class="chat-header">ChatGPT</div>', unsafe_allow_html=True)

# Display welcome message if chat is empty
if not st.session_state.chat_history:
    st.markdown('<div class="welcome-container"><h2>Tôi là một chuyên gia giải vật lý bạn có thắc mắc gì về vật lý?</h2></div>', unsafe_allow_html=True)

# Display chat messages
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        is_user = message["role"] == "user"
        st.markdown(convert_to_html(message["content"], is_user), unsafe_allow_html=True)

# Message input area
st.markdown('<div class="input-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 12, 1])

with col1:
    if st.button("Browse file"):
        # Kích hoạt file uploader khi nhấn button
        uploaded_files = st.file_uploader("", type=["jpg", "jpeg", "png", "pdf", "txt"], 
                                        accept_multiple_files=True, key="file_uploader")
    

    if uploaded_files:
        st.session_state.uploaded_files = uploaded_files
    # uploaded_files = st.file_uploader("Browse files", type=["jpg", "jpeg", "png", "pdf", "txt"], accept_multiple_files=True, key="file_uploader", label_visibility="collapsed")
    # if uploaded_files:
    #     st.session_state.uploaded_files = uploaded_files

with col2:
    print("input")
    st.text_input(colored_text("Hỏi bất kỳ điều gì","white"), key="user_input", on_change=process_message, label_visibility="collapsed")

with col3:
    if st.button("📤", help="Gửi tin nhắn"):
        process_message()

st.markdown('</div>', unsafe_allow_html=True)

# Check if we need to rerun the app (for processing messages)
if st.session_state.need_rerun:
    st.session_state.need_rerun = False
    st.rerun()
