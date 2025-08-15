try:
    import pyttsx3
except ImportError:
    pyttsx3 = None

def get_voice_array():

    pyttsx3_voice_names = []
    if pyttsx3 is not None:
        engine = pyttsx3.init()
        pyttsx3_voices = engine.getProperty('voices')
        for voice in pyttsx3_voices:
            # Fix: use voice.name.lower() instead of voice.lower()
            if voice and hasattr(voice, 'name') and voice.name.lower().startswith('microsoft'):
                pyttsx3_voice_names.append(voice.name.split()[1])
            else:
                pyttsx3_voice_names.append(voice.name)

    return [
        'Basic',
        'Mike',
        'James',
        'Michael',
        'Andrew',
        'Shanaya',
        'Joseph',
        'Faith',
        'Phoebe',
        'Zoe',
        'Emric',
        'Stellan',
        'Lazlo',
        'Davor',
        'Antero',
        'Lucien',
        'Marek',
        'Oskar',
        'Petra',
        'Fiorella',
        'Mireille',
        'Annika',
        'Lilwen',
        'Soraya',
        'Calista',
        'Amelina',
        'Isolde',
        'Violette',
        'Eira',
        'Kaius',
        'Noemi',
        'Soren',
        'Ylva',
    ] + pyttsx3_voice_names

def get_voice_data(voice_name):
    voices = {
        # Male
        'Basic': {
            'name': 'Basic',
            'model': 'gtts',
            'voice_id': 0
        },
        'Mike': {
            'name': 'Mike',
            'model': 'TTS',
            'voice_id': 'p228'
        },
        'James': {
            'name': 'James',
            'model': 'TTS',
            'voice_id': 'p229'
        },
        'Michael': {
            'name': 'Michael',
            'model': 'TTS',
            'voice_id': 'p230'
        },
        'Andrew': {
            'name': 'Andrew',
            'model': 'TTS',
            'voice_id': 'p234'
        },
        'Shanaya': {
            'name': 'Shanaya',
            'model': 'TTS',
            'voice_id': 'p240'
        },
        'Joseph': {
            'name': 'Joseph',
            'model': 'TTS',
            'voice_id': 'p241'
        },
        'David': {
            'name': 'David',
            'model': 'pyttsx3',
            'voice_id': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0'
        },
        'Emric': {
            'name': 'Emric',
            'model': 'TTS',
            'voice_id': 'p251'
        },
        'Stellan': {
            'name': 'Stellan',
            'model': 'TTS',
            'voice_id': 'p256'
        },
        'Lazlo': {
            'name': 'Lazlo',
            'model': 'TTS',
            'voice_id': 'p257'
        },
        'Davor': {
            'name': 'Davor',
            'model': 'TTS',
            'voice_id': 'p264'
        },
        'Antero': {
            'name': 'Antero',
            'model': 'TTS',
            'voice_id': 'p267'
        },
        'Lucien': {
            'name': 'Lucien',
            'model': 'TTS',
            'voice_id': 'p302'
        },
        'Marek': {
            'name': 'Marek',
            'model': 'TTS',
            'voice_id': 'p312'
        },
        'Oskar': {
            'name': 'Oskar',
            'model': 'TTS',
            'voice_id': 'p340'
        },
        # Female
        'Ylva': {
            'name': 'Ylva',
            'model': 'TTS',
            'voice_id': 'p363'
        },
        'Fiorella': {
            'name': 'Fiorella',
            'model': 'TTS',
            'voice_id': 'p335'
        },
        'Petra': {
            'name': 'Petra',
            'model': 'TTS',
            'voice_id': 'p333'
        },
        'Mireille': {
            'name': 'Mireille',
            'model': 'TTS',
            'voice_id': 'p284'
        },
        'Annika': {
            'name': 'Annika',
            'model': 'TTS',
            'voice_id': 'p274'
        },
        'Lilwen': {
            'name': 'Lilwen',
            'model': 'TTS',
            'voice_id': 'p273'
        },
        'Soraya': {
            'name': 'Soraya',
            'model': 'TTS',
            'voice_id': 'p270'
        },
        'Calista': {
            'name': 'Calista',
            'model': 'TTS',
            'voice_id': 'p268'
        },
        'Amelina': {
            'name': 'Amelina',
            'model': 'TTS',
            'voice_id': 'p260'
        },
        'Sunniva': {
            'name': 'Sunniva',
            'model': 'TTS',
            'voice_id': 'p259'
        },
        'Isolde': {
            'name': 'Isolde',
            'model': 'TTS',
            'voice_id': 'p246'
        },
        'Violette': {
            'name': 'Violette',
            'model': 'TTS',
            'voice_id': 'p248'
        },
        'Eira': {
            'name': 'Eira',
            'model': 'TTS',
            'voice_id': 'p250'
        },
        'Faith': {
            'name': 'Faith',
            'model': 'TTS',
            'voice_id': 'p237'
        },
        'Phoebe': {
            'name': 'Phoebe',
            'model': 'TTS',
            'voice_id': 'p243'
        },
        'Zoe': {
            'name': 'Zoe',
            'model': 'TTS',
            'voice_id': 'p245'
        },
        'Hazel': {
            'name': 'Hazel',
            'model': 'pyttsx3',
            'voice_id': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-GB_HAZEL_11.0'
        },
        'Zira': {
            'name': 'Zira',
            'model': 'pyttsx3',
            'voice_id': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'
        },
        # Teen
        'Kaius': {
            'name': 'Kaius',
            'model': 'TTS',
            'voice_id': 'p308'
        },
        'Noemi': {
            'name': 'Noemi',
            'model': 'TTS',
            'voice_id': 'p310'
        },
        'Soren': {
            'name': 'Soren',
            'model': 'TTS',
            'voice_id': 'p329'
        },
    }

    return voices.get(voice_name, None)

if __name__ == "__main__":
    get_voice_array()