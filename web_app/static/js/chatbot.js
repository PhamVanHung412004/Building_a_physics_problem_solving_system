document.addEventListener('DOMContentLoaded', function() {
    const chatContainer = document.getElementById('chat-container');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');
    let isWaitingForResponse = false;

    // Initialize with a welcome message
    addBotMessage("Hello! I'm the Physics Bot. Ask me any physics-related question!");

    // Handle send button click
    sendButton.addEventListener('click', sendMessage);

    // Handle enter key press in input field
    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Function to send user message to the bot
    function sendMessage() {
        if (isWaitingForResponse) return;
        
        const message = messageInput.value.trim();
        if (message === '') return;

        // Add user message to chat
        addUserMessage(message);
        
        // Clear input field
        messageInput.value = '';
        
        // Show loading animation
        showLoading();
        
        // Set waiting flag
        isWaitingForResponse = true;
        
        // Send message to server
        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message }),
        })
        .then(response => response.json())
        .then(data => {
            // Hide loading animation
            hideLoading();
            
            // Add bot response to chat
            addBotMessage(data.response);
            
            // Reset waiting flag
            isWaitingForResponse = false;
        })
        .catch(error => {
            console.error('Error:', error);
            hideLoading();
            addBotMessage("Sorry, I encountered an error. Please try again.");
            isWaitingForResponse = false;
        });
    }

    // Function to add user message to chat
    function addUserMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.className = 'chat-bubble user-bubble';
        messageElement.textContent = message;
        
        const messageContainer = document.createElement('div');
        messageContainer.className = 'd-flex justify-content-end mb-3';
        messageContainer.appendChild(messageElement);
        
        chatContainer.appendChild(messageContainer);
        scrollToBottom();
    }

    // Function to add bot message to chat
    function addBotMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.className = 'chat-bubble bot-bubble';
        messageElement.textContent = message;
        
        const messageContainer = document.createElement('div');
        messageContainer.className = 'd-flex justify-content-start mb-3';
        messageContainer.appendChild(messageElement);
        
        chatContainer.appendChild(messageContainer);
        scrollToBottom();
    }

    // Function to show loading animation
    function showLoading() {
        const loaderElement = document.createElement('div');
        loaderElement.className = 'atom-loader';
        loaderElement.id = 'loading-animation';
        
        const loaderContainer = document.createElement('div');
        loaderContainer.className = 'd-flex justify-content-center mb-3';
        loaderContainer.appendChild(loaderElement);
        
        chatContainer.appendChild(loaderContainer);
        scrollToBottom();
    }

    // Function to hide loading animation
    function hideLoading() {
        const loader = document.getElementById('loading-animation');
        if (loader && loader.parentElement) {
            loader.parentElement.remove();
        }
    }

    // Function to scroll chat to bottom
    function scrollToBottom() {
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    // Sample physics formulas for quick access (could be expanded)
    const quickFormulas = [
        "F = ma",
        "E = mc²",
        "F = G(m₁m₂)/r²",
        "E = hf",
        "PV = nRT"
    ];

    // Create quick formula buttons
    const formulaContainer = document.getElementById('formula-container');
    if (formulaContainer) {
        quickFormulas.forEach(formula => {
            const button = document.createElement('button');
            button.className = 'btn btn-sm btn-outline-info me-2 mb-2';
            button.textContent = formula;
            button.addEventListener('click', () => {
                messageInput.value = `Tell me about the formula: ${formula}`;
            });
            formulaContainer.appendChild(button);
        });
    }
});
