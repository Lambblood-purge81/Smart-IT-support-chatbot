# 🤖 Smart IT Support Chatbot

Welcome to **Smart IT Support Chatbot** — an AI-powered assistant designed to help users with technical issues through voice, text, and image-based interactions.

## 🚀 Features

- 💬 Chat-based IT Support
- 🖼️ Image Upload (OCR to extract text from screenshots)
- 🎤 Voice Input (Speech to Text)
- 🔊 Voice Output (Text to Speech)
- 🧠 AI Responses (Powered by an open-source LLM like Mistral 7B or alternatives)
- 🪜 Step-by-step structured answers for technical problems

---

## 📸 Screenshots

> Add screenshots of your app here using:
> `![Screenshot](screenshots/home.png)`

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Voice Recognition**: `SpeechRecognition`, `PyAudio`
- **OCR**: `pytesseract`, `Pillow`
- **Text-to-Speech**: `pyttsx3` or `gTTS`
- **AI Model**: Hugging Face 🤗 Transformers (e.g., Mistral 7B-Instruct or similar)

---

## 📂 Project Structure


---

## 🧑‍💻 Installation

```bash
# 1. Clone the repository
git clone git@github.com:Lambblood-purge81/Smart-IT-support-chatbot.git
cd Smart-IT-support-chatbot

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
# Login to Hugging Face
huggingface-cli login

# Make sure to use a local model or cached model to avoid API limits
pip freeze > requirements.txt

---

Let me know if you'd like me to generate the `requirements.txt`, upload screenshots, or convert this into a `.md` file directly.
