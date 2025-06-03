# 🗣️ Vernacular Chatbot using Groq + LLaMA 3

This is a multilingual chatbot built with **Streamlit**, powered by **LLaMA 3 via Groq API**, and supports vernacular language conversations. Users can select their preferred language and chat in real-time.

---

## ✨ Features

- 🌍 Vernacular language selection (supports many Indian languages)
- 🤖 LLaMA 3 model via Groq API
- 💬 Persistent in-session chat history
- 🧹 Clear chat button
- 🧪 Simple and interactive Streamlit UI

---

## 📁 Project Structure
vernacular-chatbot/
│
├── vernacularbot/
│   └── main.py
│   └── .env
│
├── .gitignore
├── README.md
└── requirements.txt

 ##⚙️ Setup Instructions
 # 1️⃣ Clone the repository
git clone https://github.com/your-username/vernacular-chatbot.git
cd vernacular-chatbot

# 2️⃣ (Optional but recommended) Create a virtual environment
python -m venv venv

# Activate it:
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Create a .env file inside the vernacularbot/ folder with this content:
# (Replace with your actual Groq API key)
GROQ_API_KEY=your_actual_groq_api_key_here

# 5️⃣ Run the Streamlit chatbot
streamlit run vernacularbot/main.py


