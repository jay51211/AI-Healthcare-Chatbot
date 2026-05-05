from flask import Flask, jsonify, request, render_template
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
conversation_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")

    if not question or not question.strip():
        return jsonify({"response": "Please write your question!"}), 400

    if question.strip().lower() in ["exit", "quit"]:
        conversation_history.clear()
        return jsonify({"response": "Goodbye! Take care of your health."}), 200

    conversation_history.append({"role": "user", "content": question})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[                          
            {"role": "system", "content": "You are a helpful, empathetic, and highly knowledgeable AI healthcare assistant. You provide general information and always advise users to consult a real doctor for medical emergencies."},
            *conversation_history
        ],
        temperature=0.7,
        max_tokens=512
    )

    answer = response.choices[0].message.content.strip()
    conversation_history.append({"role": "assistant", "content": answer})
    return jsonify({"response": answer}), 200

if __name__ == "__main__":
    app.run(debug=False)
