import json
import random
import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_folder='../static', template_folder='../templates')

# Load strategies from JSON
def load_strategies():
    try:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(base_path, 'strategies.json'), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "general": ["Take a deep breath and stay calm."]
        }

def load_crisis_keywords():
    DEFAULT_CRISIS_KEYWORDS = [
        "suicide",
        "hurt myself",
        "want to die",
        "kill myself",
        "end it all",
        "self-harm",
        "self harm",
        "cutting",
        "overdose",
    ]
    try:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(base_path, "crisis_keywords.json"), "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return DEFAULT_CRISIS_KEYWORDS

strategies_data = load_strategies()
CRISIS_KEYWORDS = load_crisis_keywords()

def analyze_sentiment(message):
    message = message.lower()
    
    # Simple rule-based sentiment/category detection
    if any(word in message for word in ["stress", "overwhelmed", "work", "exam", "busy"]):
        return "stress"
    elif any(word in message for word in ["sad", "unhappy", "cry", "lonely", "broken", "depressed"]):
        return "sad"
    elif any(word in message for word in ["anxious", "worry", "panic", "scared", "fear", "nervous"]):
        return "anxiety"
    else:
        return "general"

def is_crisis(message):
    message = message.lower()
    return any(keyword in message for keyword in CRISIS_KEYWORDS)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({"response": "I'm sorry, I didn't receive a message."})
    
    # Check for crisis keywords
    if is_crisis(user_message):
        helplines = [
            {"name": "Emergency Services", "phone": "112 (India) / 911 (US)", "region": "Local"},
            {"name": "Kiran Mental Health Helpline", "phone": "1800-599-0019", "region": "India"},
            {"name": "AASRA", "phone": "+91-22-27546669", "region": "India"},
            {"name": "Sneha Foundation", "phone": "044-24640050", "region": "India"},
            {"name": "988 Suicide & Crisis Lifeline", "phone": "988", "region": "US"},
        ]
        return jsonify({
            "response": (
                "I'm really sorry you're going through this. You deserve support right now. "
                "If you might hurt yourself or feel unsafe, please reach out for immediate help—"
                "call local emergency services or a crisis helpline."
            ),
            "emergency": True,
            "is_crisis": True,
            "helplines": helplines,
        })
    
    # Analyze sentiment and get strategy
    sentiment = analyze_sentiment(user_message)
    strategies = strategies_data.get(sentiment, strategies_data['general'])
    response_strategy = random.choice(strategies)
    
    # Basic conversational context
    responses = [
        f"I hear you. It sounds like you're feeling {sentiment}. Here is something that might help: {response_strategy}",
        f"I'm here for you. Dealing with {sentiment} can be tough. Why don't you try this? {response_strategy}",
        f"It's completely okay to feel this way. For {sentiment}, I often recommend: {response_strategy}"
    ]
    
    if sentiment == "general":
        responses = [
            f"Thank you for sharing. {random.choice(strategies)}",
            f"I'm listening. {random.choice(strategies)}",
            f"I'm here to support you. {random.choice(strategies)}"
        ]

    return jsonify({"response": random.choice(responses), "category": sentiment, "emergency": False, "is_crisis": False})

# Route for local chat endpoint (for backward compatibility)
@app.route('/chat', methods=['POST'])
def chat_legacy():
    return chat()
