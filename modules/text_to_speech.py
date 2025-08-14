import os
from gtts import gTTS

try:
    import pyttsx3
    pyttsx3 = 1
except ImportError:
    pyttsx3 = None
    
try:
    from TTS.api import TTS
    tts = 1
except ImportError:
    tts = None

def text_to_speech(news_text: str, method: str = "gtts", voice_id: str = None) -> str:
    """
    Converts text to speech using either gTTS (online) or pyttsx3 (offline).
    method: 'gtts' or 'pyttsx3' or 'TTS'
    voice_id: pyttsx3 voice id (optional)
    """
    audio_path = "temp/output.mp3"
    
    import os

    if not os.path.exists("temp/"):
        os.makedirs("temp")

    match method:
        case 'pyttsx3':
            if pyttsx3 is None:
                raise ImportError("pyttsx3 is not installed. Install it with 'pip install pyttsx3'.")
            
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            
            if voice_id:
                engine.setProperty('voice', voice_id)
            else:
                engine.setProperty('voice', voices[0].id)
                
            engine.save_to_file(news_text, audio_path)
            engine.runAndWait()
        case 'TTS':            
            tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=True)
            tts.to('cuda')
            
            if not voice_id:
                voice_id = 'p244'
            
            tts.tts_to_file(text=news_text, speaker=voice_id, file_path=audio_path)
        case _:
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