import os
from gtts import gTTS     # Google Text-to-Speech (online, requires internet)

try:
    import pyttsx3        # (offline TTS library)
except ImportError:
    pyttsx3 = None
    
try:
    from TTS.api import TTS    # Coqui TTS (advanced TTS with multiple voices and models)
except ImportError:
    TTS = None

def text_to_speech(news_text: str, method: str = "gtts", voice_id: str = None) -> str:
    """
    Converts text to speech using either gTTS (online) or pyttsx3 (offline).
    method: 'gtts' or 'pyttsx3' or 'TTS'
    voice_id: pyttsx3 voice id (optional)
    """
    audio_path = "temp/output.mp3"
    
    import os

    # Ensure output directory exists
    if not os.path.exists("temp/"):
        os.makedirs("temp")

    match method:
        case 'pyttsx3':
            # Check if pyttsx3 is available
            if pyttsx3 is None:
                raise ImportError("pyttsx3 is not installed. Install it with 'pip install pyttsx3'.")
            
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')

            # Select voice based on provided voice_id or default to first voice
            if voice_id:
                engine.setProperty('voice', voice_id)
            else:
                engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0')

            # Save speech to file (offline)
            engine.save_to_file(news_text, audio_path)
            engine.runAndWait()
        case 'TTS':
            # Check if Coqui TTS is available
            if TTS is None:
                raise ImportError("TTS is not installed. Install it with 'pip install coqui-tts'.")

            # Load pretrained voice model (vits = high quality neural TTS)
            tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=True)

            # Use GPU if available
            import torch
            if torch.cuda.is_available():
                tts.to('cuda')

            # Default speaker if none provided
            if not voice_id:
                voice_id = 'p244'

            # Generate speech to file
            tts.tts_to_file(text=news_text, speaker=voice_id, file_path=audio_path)
        case _:
            # Default to Google TTS (online)
            tts = gTTS(text=news_text, lang="en")
            tts.save(audio_path)

    print(f"c✅ Audio generated: {audio_path} - {method}")
            
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

    text_to_speech(sample_news, method="TTS")
    
    # Example usage:
    # text_to_speech(sample_news, method="pyttsx3", voice_id=None)
    # text_to_speech(sample_news, method="gtts")

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
