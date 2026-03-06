# Mental Health Support Assistant

A Flask-based web application that provides mental health support through conversational AI. The assistant can detect crisis situations and provide appropriate resources.

## Features

- **Sentiment Analysis**: Identifies user emotional states (stress, sadness, anxiety, etc.)
- **Crisis Detection**: Recognizes crisis keywords and provides emergency helpline information
- **Strategy Recommendations**: Offers coping strategies based on detected sentiment
- **Responsive UI**: Modern, accessible web interface

## Supported Helplines

- Emergency Services (112 in India, 911 in US)
- Kiran Mental Health Helpline (India)
- AASRA (India)
- Sneha Foundation (India)
- 988 Suicide & Crisis Lifeline (US)

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Vercel (Serverless)

## Local Development

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mohamedsaif21/Mental-Health-Support-Assistant.git
cd Mental-Health-Support-Assistant
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The app will be available at `http://localhost:5000`

## Deployment to Vercel

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Deploy:
```bash
vercel
```

3. Configure environment variables if needed in Vercel dashboard

## Project Structure

```
├── api/
│   └── index.py          # Vercel serverless function entry point
├── static/
│   ├── css/
│   │   └── style.css     # Stylesheet
│   └── js/
│       └── script.js     # Frontend logic
├── templates/
│   └── index.html        # Main HTML template
├── app.py                # Flask application (local development)
├── crisis_keywords.json  # Crisis detection keywords
├── strategies.json       # Coping strategies database
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
└── README.md            # This file
```

## Configuration Files

### crisis_keywords.json
Contains keywords that trigger crisis response with helpline information.

### strategies.json
Contains coping strategies organized by emotion category:
- stress
- anxiety
- sadness
- general

## API Endpoints

### POST /chat
Send a message to the assistant.

**Request:**
```json
{
  "message": "I'm feeling stressed about exams"
}
```

**Response:**
```json
{
  "response": "I hear you...",
  "category": "stress",
  "emergency": false,
  "is_crisis": false
}
```

### POST /api/chat
Alternative endpoint for API calls.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is open source and available under the MIT License.

## Support

For mental health emergencies, please contact your local emergency services or the helplines listed in the Features section.

---

**Important**: This assistant is not a replacement for professional mental health services. If you're experiencing a mental health crisis, please reach out to qualified professionals immediately.
