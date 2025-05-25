// Voice recording functionality for Physics Bot

document.addEventListener('DOMContentLoaded', function() {
    const micButton = document.getElementById('mic-button');
    const micIcon = document.getElementById('mic-icon');
    const messageInput = document.getElementById('message-input');
    
    // Variables for recording state
    let isRecording = false;
    let recognition = null;
    
    // Initialize speech recognition if available
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
        // Create speech recognition object
        recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        
        // Configure recognition
        recognition.continuous = false;
        recognition.interimResults = false;
        recognition.lang = 'en-US';
        
        // Handle recognition results
        recognition.onresult = function(event) {
            const transcript = event.results[0][0].transcript;
            messageInput.value = transcript;
            
            // Log for debugging
            console.log('Voice recognized:', transcript);
        };
        
        // Handle recognition end
        recognition.onend = function() {
            stopRecording();
        };
        
        // Handle recognition errors
        recognition.onerror = function(event) {
            console.error('Recognition error:', event.error);
            stopRecording();
            
            // Show error message
            if (event.error === 'no-speech') {
                alert('No speech was detected. Please try again.');
            } else if (event.error === 'audio-capture') {
                alert('No microphone was found. Ensure that a microphone is installed and the microphone settings are configured correctly.');
            } else if (event.error === 'not-allowed') {
                alert('Permission to use microphone was denied. Please allow microphone access to use voice input.');
            } else {
                alert('Error occurred in speech recognition: ' + event.error);
            }
        };
        
        // Attach click event to mic button
        micButton.addEventListener('click', toggleRecording);
    } else {
        // Speech recognition not supported
        micButton.addEventListener('click', function() {
            alert('Speech recognition is not supported in this browser. Please try using Chrome or Edge.');
        });
        console.warn('Speech recognition not supported');
    }
    
    // Function to toggle recording state
    function toggleRecording() {
        if (isRecording) {
            stopRecording();
        } else {
            startRecording();
        }
    }
    
    // Function to start recording
    function startRecording() {
        if (!recognition) return;
        
        try {
            recognition.start();
            isRecording = true;
            
            // Update UI to show recording state
            micButton.classList.add('mic-active');
            micIcon.classList.remove('bi-mic');
            micIcon.classList.add('bi-mic-fill');
            
            // Log for debugging
            console.log('Recording started...');
        } catch (error) {
            console.error('Failed to start recording:', error);
            stopRecording();
        }
    }
    
    // Function to stop recording
    function stopRecording() {
        if (!recognition) return;
        
        try {
            recognition.stop();
        } catch (error) {
            console.error('Error stopping recognition:', error);
        }
        
        isRecording = false;
        
        // Update UI to show stopped state
        micButton.classList.remove('mic-active');
        micIcon.classList.remove('bi-mic-fill');
        micIcon.classList.add('bi-mic');
        
        // Log for debugging
        console.log('Recording stopped.');
    }
});
