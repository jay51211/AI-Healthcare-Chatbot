<div align="center">

# 🏥 AI Healthcare Chatbot

### Intelligent Conversational Health Assistant powered by Llama 3.3 70B

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Groq](https://img.shields.io/badge/Groq-LPU%20Inference-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![Llama](https://img.shields.io/badge/Llama_3.3-70B-blueviolet?style=for-the-badge)](https://groq.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

> An AI-powered healthcare assistant that provides empathetic, context-aware health information using state-of-the-art LLM technology. Built with a Flask REST API backend and full conversation memory.

<br/>

> ⚠️ **Medical Disclaimer:** This application provides general health information only and is **not a substitute for professional medical advice**. Always consult a qualified healthcare provider for diagnosis and treatment.

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [API Reference](#-api-reference)
- [How It Works](#-how-it-works)
- [Security](#-security)
- [Future Roadmap](#-future-roadmap)
- [Author](#-author)

---

## 🔍 Overview

The **AI Healthcare Chatbot** is a full-stack conversational AI application that allows users to ask health-related questions and receive intelligent, empathetic responses. Unlike basic chatbots that treat every message independently, this system maintains **full conversation history** — meaning it understands context across the entire session, just like talking to a real doctor who remembers what you said earlier.

The backend is built as a clean **REST API** using Flask, and the LLM inference is powered by **Groq's ultra-fast LPU hardware** running **Llama 3.3 70B** — one of the most capable open-source language models available today.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧠 **Conversation Memory** | Full session history sent with every request — bot remembers context across the entire chat |
| ⚡ **Ultra-fast Inference** | Powered by Groq LPU — responses in milliseconds, not seconds |
| 🏥 **Healthcare-tuned Prompt** | System prompt engineered specifically for empathetic, responsible health responses |
| 🔌 **REST API Backend** | Clean `/ask` endpoint returns structured JSON — easy to integrate with any frontend |
| 🛡️ **Input Validation** | Handles empty inputs, exit commands, and edge cases gracefully |
| 🎨 **Clean Frontend** | Lightweight HTML/CSS/JS chat interface served via Flask templates |

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | Python + Flask | REST API server and routing |
| **LLM** | Llama 3.3 70B | Natural language understanding and generation |
| **Inference** | Groq API | Ultra-fast LPU-based model serving |
| **Frontend** | HTML + CSS + JavaScript | Chat user interface |
| **Config** | python-dotenv | Secure environment variable management |

</div>

---

## 📁 Project Structure

```
AI-Healthcare-Chatbot/
│
├── 📄 main.py                  # Core Flask app — routes, LLM logic, conversation memory
├── 📄 requirements.txt         # Python dependencies
├── 📄 .env                     # API keys — never committed to GitHub
├── 📄 .gitignore               # Excludes .env, __pycache__, etc.
│
├── 📂 templates/
│   └── index.html              # Frontend chat interface
│
└── 📂 static/
    └── style.css               # Chat UI styling
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- A free Groq API key from [console.groq.com](https://console.groq.com)

### Step 1 — Clone the repository

```bash
git clone https://github.com/jay51211/AI-Healthcare-Chatbot.git
cd AI-Healthcare-Chatbot
```

### Step 2 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Configure your API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> 🔑 Get your free API key at [console.groq.com](https://console.groq.com) — no credit card required.

### Step 4 — Run the application

```bash
python main.py
```

### Step 5 — Open in your browser

```
http://localhost:5000
```

---

## 🔌 API Reference

### `POST /ask`

Send a health-related question and receive an AI-generated response.

**Endpoint:** `/ask`  
**Method:** `POST`  
**Content-Type:** `application/x-www-form-urlencoded`

#### Request Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| `question` | `string` | Yes | The health question to ask |

#### Response Examples

**✅ Successful Response** `200 OK`
```json
{
  "response": "Common symptoms of dehydration include dark-coloured urine, dry mouth, dizziness, and fatigue. For mild cases, increase fluid and electrolyte intake. If symptoms are severe or persistent, please consult a doctor immediately."
}
```

**⚠️ Empty Input** `400 Bad Request`
```json
{
  "response": "Please write your question!"
}
```

**👋 Exit Command** (`exit` or `quit`) `200 OK`
```json
{
  "response": "Goodbye! Take care of your health."
}
```

---

## ⚙️ How It Works

```
┌─────────────┐     POST /ask      ┌──────────────────────┐
│   Browser   │ ────────────────►  │   Flask Backend      │
│ (index.html │                    │                      │
│  + JS fetch)│ ◄────────────────  │  1. Validate input   │
└─────────────┘   JSON response    │  2. Append to        │
                                   │     history[]        │
                                   │  3. Send history     │
                                   │     to Groq API      │
                                   └──────────┬───────────┘
                                              │
                                              ▼
                                   ┌──────────────────────┐
                                   │      Groq API        │
                                   │   Llama 3.3 70B      │
                                   │                      │
                                   │  System prompt  +    │
                                   │  Full conversation   │
                                   │  history             │
                                   └──────────────────────┘
```

**Conversation Memory Flow:**

Each time the user sends a message:
1. The message is appended to `conversation_history` as `role: user`
2. The **entire history** is sent to Groq along with the system prompt
3. The LLM responds with full context awareness
4. The response is appended to history as `role: assistant`
5. On the next message, the model sees both sides of the previous conversation

This enables natural follow-up questions like:
> User: *"I have a headache"*  
> Bot: *"Here are some possible causes..."*  
> User: *"Is it serious?"* ← bot knows this refers to the headache

---

## 🔒 Security

- **`.env` is gitignored** — your API key is never pushed to GitHub
- **Never hardcode API keys** in source files — always use environment variables
- If your API key is accidentally exposed, **immediately delete it** at [console.groq.com](https://console.groq.com) and generate a new one
- Input validation prevents empty or malformed requests from reaching the LLM

---

## 🗺️ Future Roadmap

- [ ] **Session-based history with Redis** — separate conversation history per user, supports multiple concurrent users
- [ ] **Token limit management** — automatically trim old history to control API costs
- [ ] **Symptom checker module** — structured input form for specific symptom analysis
- [ ] **User authentication** — login system to save and retrieve past conversations
- [ ] **Docker containerization** — one-command deployment anywhere
- [ ] **Cloud deployment** — host on Render, Railway, or AWS EC2
- [ ] **Rate limiting** — prevent API abuse with Flask-Limiter
- [ ] **Response streaming** — stream tokens in real-time for faster perceived responses

---

## 📦 Dependencies

```txt
flask
groq
python-dotenv
```

```bash
pip install flask groq python-dotenv
```

---

## 👤 Author

<div align="center">

**Jay Kumbhar**

[![GitHub](https://img.shields.io/badge/GitHub-jay51211-181717?style=for-the-badge&logo=github)](https://github.com/jay51211)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-jaykumbhar5121-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/jaykumbhar5121)
[![Email](https://img.shields.io/badge/Email-jaykumbhar518@gmail.com-EA4335?style=for-the-badge&logo=gmail)](mailto:jaykumbhar518@gmail.com)

</div>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

*Built by Jay Kumbhar*

⭐ **If you found this project useful, please give it a star!** ⭐

</div>
