# 💬 AI Girlfriend

An interactive AI companion named **Nicole** that leverages speech-to-text, natural language processing, and text-to-speech technologies to engage in real-time voice conversations.

## 🧠 Features

- **Speech Recognition (ASR)** Converts user speech to text using OpenAI's Whisper mode.
- **Natural Language Processing (NLP)** Generates context-aware responses using Google's Gemini AI.
- **Speech Synthesis (TTS)** Transforms AI-generated text responses into human-like speech using Kokoro TT.
- **Interactive Chat** Engage in seamless voice conversations with Nicole AI Girlfriend.

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or hiher
- Access to Google's Gemini AI API

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/meowyboii/ai-girlfriend.git
   cd ai-girlfriend
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API keys**:

   Create a `.env` file in the root directory and add your API credentials:

   ```dotenv
   API_KEY=your_gemini_api_key
   ```

4. **Run the application**:

   ```bash
   python app.py
   ```

## 🗣️ Usage

- Upon running the application, speak into your micropone.
- Nicole will process your speech, generate a response, and reply with synthesized speech.
- Engage in continuous, real-time conversatons.

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork the repository**.
2. **Create a new branch**:

```bash
git checkout -b feature/YourFeature
```

3. **Make your changes**.
4. **Commit your changes**:

```bash
git commit -m "Add your feature"
```

5. **Push to the branch**:

```bash
git push origin feature/YourFeature
```

6. **Open a Pull Request**.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
