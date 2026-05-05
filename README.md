# 🏥 AI Healthcare Chatbot

An AI-powered healthcare assistant built with **Flask**, **Groq API**, and **Llama 3.3 70B**. Ask any health-related question and get instant, empathetic responses — with full conversation memory so the bot understands context across the entire chat.

> ⚠️ **Disclaimer:** This chatbot provides general health information only. Always consult a qualified doctor for medical diagnosis or emergencies.

---

## 🚀 Features

- **Conversational memory** — the bot remembers everything said in the session, so follow-up questions work naturally
- **Powered by Llama 3.3 70B** — one of the most capable open LLMs available via Groq's ultra-fast inference API
- **Healthcare-focused system prompt** — responses are empathetic, informative, and always recommend professional consultation for serious issues
- **REST API backend** — built with Flask, returns clean JSON responses
- **Input validation** — handles empty inputs and exit commands gracefully
- **Lightweight frontend** — simple HTML/CSS/JS interface served via Flask templates

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| LLM | Llama 3.3 70B (via Groq API) |
| API Client | `groq` Python SDK |
| Frontend | HTML, CSS, JavaScript |
| Config | `python-dotenv` |

---

## 📁 Project Structure

```
AI-Healthcare-Chatbot/
│
├── main.py              # Flask app — routes and LLM logic
├── .env                 # API keys (never commit this)
├── .gitignore           # Excludes .env and __pycache__
├── requirements.txt     # Python dependencies
│
├── templates/
│   └── index.html       # Frontend chat interface
│
└── static/
    ├── style.css        # Styling
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/jay51211/AI-Healthcare-Chatbot.git
cd AI-Healthcare-Chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get your free Groq API key
- Go to [console.groq.com](https://console.groq.com)
- Sign up for free
- Create a new API key

### 4. Create your `.env` file
```bash
# Create a .env file in the project root
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the app
```bash
python main.py
```

### 6. Open in browser
```
http://localhost:5000
```

---

## 🔌 API Reference

### `POST /ask`

Send a health question and receive an AI response.

**Request:**
```
Content-Type: application/x-www-form-urlencoded

question=What are symptoms of dehydration?
```

**Success Response:**
```json
{
  "response": "Common symptoms of dehydration include dark urine, dry mouth, dizziness, and fatigue. For mild cases, increase fluid intake. If symptoms are severe, please consult a doctor immediately."
}
```

**Empty input Response:**
```json
{
  "response": "Please write your question!"
}
```

**Exit command** (`exit` or `quit`):
```json
{
  "response": "Goodbye! Take care of your health."
}
```

---

## 💡 How It Works

1. User types a health question in the frontend
2. JavaScript sends a `POST` request to `/ask`
3. Flask validates the input and checks for exit commands
4. The question is added to `conversation_history`
5. The full history is sent to Groq's API along with a healthcare system prompt
6. Llama 3.3 70B generates a response with full conversation context
7. The response is appended to history and returned as JSON
8. The frontend displays the response in the chat window

```
User Input → Flask /ask → conversation_history → Groq API (Llama 3.3 70B) → JSON Response → UI
```

---

## 🔒 Security Notes

- **Never commit your `.env` file** — it contains your API key
- The `.gitignore` file is configured to exclude `.env`
- If you accidentally expose your API key, immediately delete it at [console.groq.com](https://console.groq.com) and generate a new one

---

## 🚧 Future Improvements

- Session-based conversation history using Redis (so multiple users have separate histories)
- Maximum history length to control token usage and API costs
- User authentication system
- Symptom checker with structured input form
- Docker containerization for easy deployment
- Deployment on Render / Railway / AWS

---

## 📦 Requirements

```
flask
groq
python-dotenv
```

Install all at once:
```bash
pip install flask groq python-dotenv
```

---

## 👤 Author

**Jay Kumbhar**
- GitHub: [@jay51211](https://github.com/jay51211)
- LinkedIn: [linkedin.com/in/jaykumbhar5121](https://linkedin.com/in/jaykumbhar5121)
- Email: jaykumbhar518@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
