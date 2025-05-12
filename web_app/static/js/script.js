document.addEventListener('DOMContentLoaded', function() {
    // Initialize the chat interface
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatMessages = document.getElementById('chat-messages');
    
    if (chatForm) {
        chatForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const message = chatInput.value.trim();
            if (!message) return;
            
            // Add user message to chat
            addMessage(message, 'user');
            
            // Clear input
            chatInput.value = '';
            
            // Simulate typing indicator
            addTypingIndicator();
            
            // Send message to backend
            fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message }),
            })
            .then(response => {
                if (response.status === 401) {
                    // Authentication error
                    removeTypingIndicator();
                    addMessage('Please sign in to use the chatbot.', 'bot');
                    // Optional: redirect to login page after a delay
                    setTimeout(() => {
                        window.location.href = '/login?next=/';
                    }, 3000);
                    throw new Error('Authentication required');
                }
                return response.json();
            })
            .then(data => {
                // Remove typing indicator
                removeTypingIndicator();
                
                // Add bot response
                if (data.error) {
                    addMessage('Sorry, I encountered an error: ' + data.error, 'bot');
                } else {
                    addMessage(data.response, 'bot');
                }
                
                // Scroll to bottom
                scrollToBottom();
            })
            .catch(error => {
                if (error.message === 'Authentication required') {
                    // Already handled above
                    return;
                }
                console.error('Error:', error);
                removeTypingIndicator();
                addMessage('Sorry, there was an error communicating with the server.', 'bot');
                scrollToBottom();
            });
        });
    }
    
    // Add welcome message when chat interface loads
    if (chatMessages && chatMessages.children.length === 0) {
        setTimeout(() => {
            addMessage("Hello! I'm your physics chatbot assistant. Ask me anything about physics concepts, equations, or theories!", 'bot');
        }, 500);
    }
    
    // Function to add a message to the chat
    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender + '-message');
        
        const contentDiv = document.createElement('div');
        contentDiv.classList.add('message-content');
        
        // Create paragraph for the text
        const paragraph = document.createElement('p');
        paragraph.innerHTML = text; // Use innerHTML to support HTML formatting
        contentDiv.appendChild(paragraph);
        
        messageDiv.appendChild(contentDiv);
        chatMessages.appendChild(messageDiv);
        scrollToBottom();
    }
    
    // Function to add typing indicator
    function addTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.classList.add('message', 'bot-message', 'typing-indicator');
        typingDiv.innerHTML = '<span class="dot"></span><span class="dot"></span><span class="dot"></span>';
        chatMessages.appendChild(typingDiv);
        scrollToBottom();
    }
    
    // Function to remove typing indicator
    function removeTypingIndicator() {
        const typingIndicator = chatMessages.querySelector('.typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
    
    // Function to scroll chat to bottom
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Animations for physics elements
    const equationElements = document.querySelectorAll('.equation');
    if (equationElements.length > 0) {
        equationElements.forEach((element, index) => {
            element.style.animationDelay = (index * 0.5) + 's';
        });
    }
    
    // Initialize popovers and tooltips (Bootstrap)
    const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');
    if (popoverTriggerList.length > 0) {
        const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));
    }
    
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    if (tooltipTriggerList.length > 0) {
        const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
    }
    
    // Add smooth scrolling for navigation links
    document.querySelectorAll('a.nav-link[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70,
                    behavior: 'smooth'
                });
            }
        });
    });
});
