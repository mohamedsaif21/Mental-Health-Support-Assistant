document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const chatArea = document.getElementById('chat-area');
    const clearBtn = document.getElementById('clear-chat');
    const emergencyModal = document.getElementById('emergency-modal');
    const helplineList = document.getElementById('helpline-list');
    const emergencyClose = document.getElementById('emergency-close');
    const emergencyOk = document.getElementById('emergency-ok');

    // Auto-resize textarea
    userInput.addEventListener('input', () => {
        userInput.style.height = 'auto';
        userInput.style.height = userInput.scrollHeight + 'px';
        sendBtn.disabled = userInput.value.trim() === '';
    });

    const openEmergencyModal = (helplines = []) => {
        if (!emergencyModal || !helplineList) return;

        const list = Array.isArray(helplines) ? helplines : [];
        if (list.length === 0) {
            helplineList.innerHTML = `
                <div class="helpline-item">
                    <div class="name">Crisis support</div>
                    <div class="meta">Please contact local emergency services or a trusted person right now.</div>
                </div>
            `;
        } else {
            helplineList.innerHTML = list.map(h => {
                const name = (h && h.name) ? String(h.name) : 'Helpline';
                const phone = (h && h.phone) ? String(h.phone) : '';
                const region = (h && h.region) ? String(h.region) : '';
                const meta = region ? `<div class="meta">${region}</div>` : '';
                const phoneLine = phone ? `<div class="phone">${phone}</div>` : '';
                return `
                    <div class="helpline-item">
                        <div class="name">${name}</div>
                        ${meta}
                        ${phoneLine}
                    </div>
                `;
            }).join('');
        }

        emergencyModal.classList.add('is-open');
        emergencyModal.setAttribute('aria-hidden', 'false');
    };

    const closeEmergencyModal = () => {
        if (!emergencyModal) return;
        emergencyModal.classList.remove('is-open');
        emergencyModal.setAttribute('aria-hidden', 'true');
    };

    if (emergencyClose) emergencyClose.addEventListener('click', closeEmergencyModal);
    if (emergencyOk) emergencyOk.addEventListener('click', closeEmergencyModal);
    if (emergencyModal) {
        emergencyModal.addEventListener('click', (e) => {
            if (e.target === emergencyModal) closeEmergencyModal();
        });
    }
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeEmergencyModal();
    });

    const addMessage = (text, sender, isCrisis = false) => {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', `${sender}-message`);
        if (isCrisis) messageDiv.classList.add('crisis-alert');

        const now = new Date();
        const timeStr = now.getHours().toString().padStart(2, '0') + ':' + now.getMinutes().toString().padStart(2, '0');

        messageDiv.innerHTML = `
            <div class="message-content">${text}</div>
            <div class="message-time">${timeStr}</div>
        `;

        chatArea.appendChild(messageDiv);
        chatArea.scrollTop = chatArea.scrollHeight;
    };

    const addTypingIndicator = () => {
        const indicator = document.createElement('div');
        indicator.id = 'typing-indicator';
        indicator.classList.add('typing-indicator');
        indicator.innerHTML = '<span></span><span></span><span></span>';
        chatArea.appendChild(indicator);
        chatArea.scrollTop = chatArea.scrollHeight;
        return indicator;
    };

    const sendMessage = async () => {
        const text = userInput.value.trim();
        if (!text) return;

        // Add user message
        addMessage(text, 'user');
        
        // Reset input
        userInput.value = '';
        userInput.style.height = 'auto';
        sendBtn.disabled = true;

        // Add typing indicator
        const indicator = addTypingIndicator();

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: text })
            });

            const data = await response.json();
            
            // Remove typing indicator
            indicator.remove();

            if (data && (data.emergency || data.is_crisis)) {
                openEmergencyModal(data.helplines);
            }

            // Add bot message
            addMessage(data.response, 'bot', data.is_crisis);
        } catch (error) {
            indicator.remove();
            addMessage("I'm sorry, I'm having trouble connecting to my brain. Please try again later.", 'bot');
        }
    };

    sendBtn.addEventListener('click', sendMessage);

    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    clearBtn.addEventListener('click', () => {
        chatArea.innerHTML = `
            <div class="message bot-message">
                <div class="message-content">Conversation cleared. How can I help you now?</div>
                <div class="message-time">Just now</div>
            </div>
        `;
    });
});
