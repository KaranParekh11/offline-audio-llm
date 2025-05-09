# Offline AI Voice Assistant 🎙️🧠

**Built an Offline AI Voice Assistant — No Cloud, No GPU, No API. Just Python + Local AI Models.**

We rely heavily on cloud-based voice assistants. But what if you could build your own — one that works fully offline, runs on a CPU, and keeps your data private?

So I did it.
A full voice-to-voice AI pipeline, running on a modest laptop — no GPU required.

---

## ⚙️ How It Works (On CPU):

- **🗣️ Voice Input:**  
  Uses a pre-recorded audio file (`test.mp3`) for input.

- **🧠 Speech-to-Text (STT):**  
  Used `faster-whisper` (CPU-optimized version of OpenAI's Whisper)  
  → Translates voice into text locally and fast, even on CPUs

- **💬 Text Understanding (LLM):**  
  Powered by Ollama (using the `llama3.2` model)  
  → Provides local, privacy-focused text understanding

- **🔊 Text-to-Speech (TTS):**  
  Converted response into speech using `Coqui TTS` or `pyttsx3`  
  → Lightweight, real-time voice response

- **📶 No internet. No cloud API. Just one machine, running everything locally.**

---

## 💡 Why This Setup Is Powerful:

- ✅ **Offline-First** – Ideal for rural, secure, or remote use
- ✅ **No GPU Needed** – Runs on any modern CPU with 8GB+ RAM
- ✅ **Privacy Focused** – No data leaves your system
- ✅ **Flexible** – Add custom commands, automate local tasks, or expand into robotics

---

## 💻 Tech Stack

- Python
- Faster-Whisper (CPU)
- Ollama (Local LLM)
- Coqui TTS / pyttsx3
- No external APIs

---

## 🛠️ Setup Guide

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd offline-audio-llm
```

### 2. Set Up Python Environment

It is recommended to use a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install System Dependencies

**On macOS:**

```sh
brew install ffmpeg pkg-config portaudio
```

**On Ubuntu/Debian:**

```sh
sudo apt-get update
sudo apt-get install ffmpeg pkg-config portaudio19-dev
```

### 4. Install Ollama

Follow the instructions on the [Ollama website](https://ollama.ai/) to install Ollama on your system.

### 5. Install Python Dependencies

```sh
pip install -r requirements.txt
```

If you encounter errors with `av` or `faster-whisper`, make sure `ffmpeg` and `pkg-config` are installed as above.

### 6. Download Local LLM and TTS Models

- Download a quantized LLM (e.g., GPT4All, Mistral GGUF) and place it in the appropriate directory.
- Download or set up a TTS model (Coqui TTS or use pyttsx3 for built-in voices).

### 7. Run the Assistant

```sh
python main.py
```

---

## 📦 Example Usage

Press Enter to process the pre-recorded audio file (`test.mp3`) and get a spoken response — all processed locally!

---

## 🗂️ Project Structure

- `main.py` — Main entry point
- `requirements.txt` — Python dependencies
- `venv/` — Virtual environment (not included in repo)
- `models/` — Place your LLM and TTS models here

---

## 📝 Notes

- No internet required after setup.
- All processing is local; your voice and data never leave your machine.
- You can extend this project with custom commands, automations, or even robotics integrations.

---

## 📣 Want More?

If you want the architecture diagram, setup guide, or full source code — just drop a "Voice" in the comments or DM me.

Offline AI is not just possible — it's practical, and it's here. 💥

---

#EdgeAI #OfflineAI #VoiceAssistant #PythonDeveloper #LocalLLM #OpenSourceAI #Whisper #TTS #GPT4All #AIonCPU #PrivacyTech
