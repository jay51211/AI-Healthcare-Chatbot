from flask import Flask, jsonify, request, render_template
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app=Flask(__name__)

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")

    if question != "exit" or question != "Exit" or question != "quit" or question != "Quit":
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a helpful, empathetic, and highly knowledgeable AI healthcare assistant. You provide general information and always advise users to consult a real doctor for medical emergencies."},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=512
        )
        answer = response.choices[0].message.content.strip()
        return jsonify({"response": answer}), 200
    else:
        return jsonify({"response": "Goodbye!"}), 200


if __name__ == "__main__":
    app.run(debug=True)

    