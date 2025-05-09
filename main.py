import os

# import pyttsx3
from datetime import datetime
from faster_whisper import WhisperModel
from ollama import chat, ChatResponse

# import sounddevice as sd
# import soundfile as sf


# Optional: import coqui-tts if available
# try:
#     from TTS.api import TTS

#     coqui_available = True
# except ImportError:
#     coqui_available = False

# # Audio file to use
AUDIO_FILE = "hindi-test.mp3"
# Initialize TTS
# if coqui_available:
#     tts = TTS(
#         model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False
#     )
# else:
#     tts = pyttsx3.init()


def get_audio_file():
    print(f"[INFO] Using audio file: {AUDIO_FILE}")
    return AUDIO_FILE


def transcribe_audio(filename):
    print("[INFO] Transcribing audio with faster-whisper...")
    model = WhisperModel("base", device="cpu", compute_type="int8")
    segments, info = model.transcribe(filename)
    text = " ".join([seg.text for seg in segments])
    print("Detected Language: ", info)
    print(f"[INFO] Transcription: {text}")
    return text


def query_llm(text):
    print(f"[INFO] Querying LLM with: {text}")
    languageName = "Hindi"
    # prompt = f"""Please be polite and respectful while providing your feedback. language should be question's language.question: {text}"""
    prompt = f"""Please be polite and respectful while providing your feedback. language should be {languageName}. question: {text}"""
    t1 = datetime.now()
    response: ChatResponse = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
        stream=True,
    )
    full_response = ""
    for chunk in response:
        content = chunk["message"]["content"]
        full_response += content
        print(content, end="", flush=True)
    t2 = datetime.now()
    print(f"\nTime taken: {t2 - t1}")
    return full_response


# def speak_text(text):
#     print(f"[INFO] Speaking: {text}")
#     if coqui_available:
#         tts.tts_to_file(text=text, file_path="output.wav")
#         # Play output.wav

#         data, samplerate = sf.read("output.wav")
#         sd.play(data, samplerate)
#         sd.wait()
#         os.remove("output.wav")
#     else:
#         tts.say(text)
#         tts.runAndWait()


def main():
    print("\n=== Offline AI Voice Assistant ===\n")
    while True:
        input("Press Enter to process test.mp3 (or Ctrl+C to exit)...")
        audio_file = get_audio_file()
        user_text = transcribe_audio(audio_file)
        if not user_text.strip():
            print("[WARN] No speech detected. Try again.")
            continue
        response = query_llm(user_text)
        print(response, "response")
        # speak_text(response)
        print("\n---\n")


if __name__ == "__main__":
    main()
