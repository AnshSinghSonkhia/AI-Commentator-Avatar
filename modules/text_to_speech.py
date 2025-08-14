#import openai
#from config import OPENAI_API_KEY

#openai.api_key = OPENAI_API_KEY


#def text_to_speech(news_text, voice="alloy"):
    #"""Converts given text into speech using OpenAI's text-to-speech API."""
    #response = openai.audio.speech.create(
     #   model="tts-1",
      #  voice=voice,
       # input=news_text
    #)

    # Save the audio file
    #audio_path = "news_audio.mp3"
    #with open(audio_path, "wb") as f:
     #   f.write(response.content)

    #print(f"✅ Speech generated and saved as {audio_path}")
    #return audio_path


# Test the function
#if __name__ == "__main__":
 #   sample_news = "Breaking news! AI-powered virtual anchors are revolutionizing the media industry."
  #  text_to_speech(sample_news)

import os
from gtts import gTTS

# Optional: pyttsx3 for offline TTS
try:
    import pyttsx3
except ImportError:
    pyttsx3 = None

def text_to_speech(news_text, method="gtts", voice_id=None):
    """
    Converts text to speech using either gTTS (online) or pyttsx3 (offline).
    method: 'gtts' or 'pyttsx3'
    voice_id: pyttsx3 voice id (optional)
    """
    audio_path = "output.mp3"
    if method == "pyttsx3":
        if pyttsx3 is None:
            raise ImportError("pyttsx3 is not installed. Install it with 'pip install pyttsx3'.")
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if voice_id is not None:
            engine.setProperty('voice', voice_id)
        else:
            engine.setProperty('voice', voices[0].id)  # Default voice
        engine.save_to_file(news_text, audio_path)
        engine.runAndWait()
        print(f"	Audio generated: {audio_path} (pyttsx3)")
    else:
        tts = gTTS(text=news_text, lang="en")
        tts.save(audio_path)
        print(f"	Audio generated: {audio_path} (gTTS)")

    # Play the generated audio
    os.system(f"start {audio_path}")  # For Windows
    return audio_path

def list_pyttsx3_voices():
    """Lists available voices for pyttsx3."""
    if pyttsx3 is None:
        print("pyttsx3 is not installed.")
        return
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(f"Voice ID: {voice.id} - {voice.name}")

if __name__ == "__main__":
    sample_news = "Breaking news! AI-powered virtual anchors are revolutionizing the media industry."
    print("Available pyttsx3 voices:")
    list_pyttsx3_voices()
    # Example usage:
    # text_to_speech(sample_news, method="pyttsx3", voice_id=None)
    # text_to_speech(sample_news, method="gtts")



