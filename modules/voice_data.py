try:
    import pyttsx3
except ImportError:
    pyttsx3 = None

def get_voice_array():

    if pyttsx3 is not None:
        engine = pyttsx3.init()
        pyttsx3_voices = engine.getProperty('voices')

        pyttsx3_voice_names = [voice.name.split()[1] for voice in pyttsx3_voices]

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
            'voice_id': '0'
        },
        # Female
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
            'voice_id': '1'
        },
        'Zira': {
            'name': 'Zira',
            'model': 'pyttsx3',
            'voice_id': '2'
        }
    }

    return voices.get(voice_name, None)

if __name__ == "__main__":
    get_voice_array()