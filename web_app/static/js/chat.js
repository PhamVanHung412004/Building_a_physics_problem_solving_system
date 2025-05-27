// Chat functionality for Physics Bot

document.addEventListener('DOMContentLoaded', function() {
    const chatMessages = document.getElementById('chat-messages');
    const chatForm = document.getElementById('chat-form');
    const messageInput = document.getElementById('message-input');
    const micButton = document.getElementById('mic-button');
    const chatHistory = document.getElementById('chat-history');
    const newChatBtn = document.getElementById('new-chat-btn');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const chatSidebar = document.getElementById('chat-sidebar');
    
    // Current chat state
    let currentChatDate = new Date().toISOString().split('T')[0];
    
    // Load chat history
    loadChatHistory();
    
    // Add a welcome message
    addBotMessage("Hello! I'm Physics Bot. Ask me any physics-related question, and I'll do my best to answer.");
    
    // Handle form submission for text messages
    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const message = messageInput.value.trim();
        if (message === '') return;
        
        // Add user message to chat
        addUserMessage(message);
        
        // Clear input field
        messageInput.value = '';
        
        // Send message to server
        sendMessageToServer(message);
    });
    
    // Handle new chat button click
    newChatBtn.addEventListener('click', function() {
        // Clear chat messages
        chatMessages.innerHTML = '';
        
        // Add welcome message
        addBotMessage("Hello! I'm Physics Bot. Ask me any physics-related question, and I'll do my best to answer.");
        
        // Update current chat date
        currentChatDate = new Date().toISOString().split('T')[0];
        
        // Update active chat in sidebar
        updateActiveChatInSidebar(currentChatDate);
    });
    
    // Toggle sidebar on mobile
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function() {
            chatSidebar.classList.toggle('show');
        });
    }
    
    // Function to add user message to chat
    function addUserMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.className = 'message message-user';
        messageElement.textContent = message;
        
        const messageContainer = document.createElement('div');
        messageContainer.className = 'd-flex justify-content-end';
        messageContainer.appendChild(messageElement);
        
        chatMessages.appendChild(messageContainer);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Function to add bot message to chat
    function addBotMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.className = 'message message-bot';
        
        // Handle newlines in the message
        message = message.replace(/\n/g, '<br>');
        messageElement.innerHTML = message;
        
        const messageContainer = document.createElement('div');
        messageContainer.className = 'd-flex justify-content-start';
        messageContainer.appendChild(messageElement);
        
        chatMessages.appendChild(messageContainer);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Function to show a loading indicator
    function showLoadingIndicator() {
        const loadingElement = document.createElement('div');
        loadingElement.className = 'message message-bot loading-indicator';
        loadingElement.innerHTML = 'Physics Bot is thinking<span class="dot-animation">...</span>';
        loadingElement.id = 'loading-indicator';
        
        const messageContainer = document.createElement('div');
        messageContainer.className = 'd-flex justify-content-start';
        messageContainer.appendChild(loadingElement);
        
        chatMessages.appendChild(messageContainer);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Function to remove the loading indicator
    function removeLoadingIndicator() {
        const loadingIndicator = document.getElementById('loading-indicator');
        if (loadingIndicator) {
            loadingIndicator.parentElement.remove();
        }
    }
    
    // Function to send message to server
    function sendMessageToServer(message) {
        // Show loading indicator
        showLoadingIndicator();
        
        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Remove loading indicator
            removeLoadingIndicator();
            
            // Add bot response to chat
            addBotMessage(data.response);
            
            // Update currentChatDate if this is a new conversation
            if (data.timestamp) {
                const messageDate = new Date(data.timestamp).toISOString().split('T')[0];
                currentChatDate = messageDate;
                
                // Refresh chat history
                loadChatHistory();
            }
        })
        .catch(error => {
            console.error('Error:', error);
            
            // Remove loading indicator
            removeLoadingIndicator();
            
            // Show error message
            addBotMessage("Sorry, I'm having trouble connecting. Please try again later.");
        });
    }
    
    // Function to load chat history
    function loadChatHistory() {
        fetch('/api/chat/history')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to load chat history');
            }
            return response.json();
        })
        .then(data => {
            // Clear current history
            chatHistory.innerHTML = '';
            
            // Group chats by date
            const chatsByDate = {};
            data.history.forEach(chat => {
                const date = chat.date;
                if (!chatsByDate[date]) {
                    chatsByDate[date] = [];
                }
                chatsByDate[date].push(chat);
            });
            
            // Add chats to sidebar
            Object.keys(chatsByDate).forEach(date => {
                // Add date header
                const dateHeader = document.createElement('div');
                dateHeader.className = 'chat-history-date';
                
                // Format date for display (e.g., "Today", "Yesterday", or the actual date)
                const formattedDate = formatDate(date);
                dateHeader.textContent = formattedDate;
                chatHistory.appendChild(dateHeader);
                
                // Add chats for this date
                chatsByDate[date].forEach(chat => {
                    const chatItem = document.createElement('div');
                    chatItem.className = 'chat-history-item';
                    chatItem.textContent = chat.preview;
                    chatItem.dataset.timestamp = chat.timestamp;
                    chatItem.dataset.date = chat.date;
                    
                    // Highlight current chat
                    if (chat.date === currentChatDate) {
                        chatItem.classList.add('active');
                    }
                    
                    // Add click handler
                    chatItem.addEventListener('click', function() {
                        // Set as active chat
                        currentChatDate = chat.date;
                        updateActiveChatInSidebar(currentChatDate);
                        
                        // Load chat messages for this date
                        loadChatMessagesByDate(chat.date);
                        
                        // Close sidebar on mobile
                        if (window.innerWidth < 768) {
                            chatSidebar.classList.remove('show');
                        }
                    });
                    
                    chatHistory.appendChild(chatItem);
                });
            });
            
            // If no history, add a message
            if (data.history.length === 0) {
                const noHistory = document.createElement('p');
                noHistory.className = 'text-muted text-center small mt-3';
                noHistory.textContent = 'No chat history yet.';
                chatHistory.appendChild(noHistory);
            }
        })
        .catch(error => {
            console.error('Error loading chat history:', error);
            const errorMsg = document.createElement('p');
            errorMsg.className = 'text-danger text-center small mt-3';
            errorMsg.textContent = 'Failed to load chat history.';
            chatHistory.appendChild(errorMsg);
        });
    }
    
    // Function to update active chat in sidebar
    function updateActiveChatInSidebar(activeDate) {
        // Remove active class from all history items
        const historyItems = document.querySelectorAll('.chat-history-item');
        historyItems.forEach(item => {
            item.classList.remove('active');
            if (item.dataset.date === activeDate) {
                item.classList.add('active');
            }
        });
    }
    
    // Function to load chat messages by date
    function loadChatMessagesByDate(date) {
        // Clear current messages
        chatMessages.innerHTML = '';
        
        // Show loading indicator
        showLoadingIndicator();
        
        fetch(`/api/chat/messages/${date}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to load chat messages');
            }
            return response.json();
        })
        .then(data => {
            // Remove loading indicator
            removeLoadingIndicator();
            
            if (data.messages && data.messages.length > 0) {
                // Add messages to chat
                data.messages.forEach(msg => {
                    if (msg.is_from_user) {
                        addUserMessage(msg.message);
                    } else {
                        addBotMessage(msg.message);
                    }
                });
            } else {
                // No messages found
                addBotMessage("No messages found for this date.");
            }
        })
        .catch(error => {
            console.error('Error loading chat messages:', error);
            
            // Remove loading indicator
            removeLoadingIndicator();
            
            // Show error message
            addBotMessage("Sorry, I couldn't load the conversation history. Please try again.");
        });
    }
    
    // Function to format date
    function formatDate(dateStr) {
        const today = new Date();
        today.setHours(0, 0, 0, 0);
        
        const yesterday = new Date(today);
        yesterday.setDate(yesterday.getDate() - 1);
        
        const chatDate = new Date(dateStr + 'T00:00:00');
        
        if (chatDate.getTime() === today.getTime()) {
            return 'Today';
        } else if (chatDate.getTime() === yesterday.getTime()) {
            return 'Yesterday';
        } else {
            // Format as Month Day, Year (e.g., May 9, 2025)
            return chatDate.toLocaleDateString('en-US', { 
                month: 'short', 
                day: 'numeric', 
                year: 'numeric' 
            });
        }
    }
});
