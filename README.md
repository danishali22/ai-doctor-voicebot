# 🧠 AI Medical Voicebot

An advanced multimodal AI-powered medical voicebot that combines voice, image, and text inputs to generate real-time, professional medical insights.

---

## 📌 Features

* 🎙️ **Voice Input & Transcription**: Converts speech into text using **Whisper-large-v3** via **GROQ API**
* 🖼️ **Image Analysis**: Detects medical conditions using **LLaMA-3.2-90B Vision model**
* 💬 **AI Medical Response**: Generates accurate, professional feedback in 2–3 sentences
* 🔊 **Text-to-Speech (TTS)**: Converts generated text into audio using **ElevenLabs** and **gTTS**
* 🌐 **Multimodal Interface**: Supports voice, image, and text inputs in one seamless UI
* 🖥️ **Gradio UI**: Simple and interactive interface for users

---

## 🛠️ Tech Stack

| Category             | Tools & Services            |
| -------------------- | --------------------------- |
| Programming Language | Python                      |
| UI Framework         | Gradio                      |
| Speech-to-Text       | GROQ API (Whisper-large-v3) |
| Image Analysis       | LLaMA-3.2-90B Vision Model  |
| Text-to-Speech (TTS) | ElevenLabs, gTTS            |
| Environment Handling | python-dotenv               |

---

## 📁 Project Structure

```
ai-doctor-voicebot/
├── app.py                 # Main Gradio interface
├── whisper_utils.py       # Voice transcription logic
├── vision_utils.py        # Image analysis with LLaMA
├── tts_utils.py           # Text-to-Speech functions
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment variables
└── README.md              # Project documentation
```

---

## 🔧 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/danishali22/ai-doctor-voicebot.git
cd ai-doctor-voicebot
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Configure Environment Variables**

```bash
cp .env.example .env
# Fill in your GROQ API key, ElevenLabs key, etc.
```

4. **Run the App**

```bash
python app.py
```

---

## 🤖 How It Works

1. User speaks or uploads a medical image.
2. Voice is transcribed using Whisper via GROQ API.
3. Image is analyzed via LLaMA-3.2-90B Vision model.
4. A short, concise medical insight is generated.
5. Response is read aloud using TTS.

---

## 📚 What I Learned

* Efficient use of **multimodal AI** (text + vision + audio)
* Integration of **GROQ Whisper** and **LLaMA vision models**
* Working with **real-time audio and speech generation APIs**
* Building clean, user-friendly Gradio apps

---

## 🙌 Feedback

If you find this helpful or want to collaborate, feel free to open an issue or connect!

---

**GitHub:** [danishali22](https://github.com/danishali22)

---

> ⚠️ This project is for educational/demo purposes. Not intended for real-world diagnosis or treatment.
