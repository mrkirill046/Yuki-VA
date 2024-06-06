# Imports | kazuha046 creator
import speech_recognition as sr

from tools.best_logging import create_log

# Variables
recognizer = sr.Recognizer()
microphone = sr.Microphone()


# Methods
def record_audio():
    with microphone as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=1)

        try:
            create_log('\nLOG: Say something...', 'debug')
            audio = recognizer.listen(mic, 5, 5)

            with open('user_audio.wav', 'wb') as file:
                file.write(audio.get_wav_data())
        except sr.WaitTimeoutError:
            create_log(f'\nERROR: Check your microphone and try again', 'error')
            return None

        return audio


def recognize_voice():
    audio = record_audio()
    if not audio:
        return ''

    try:
        user_sentence = recognizer.recognize_google(audio, language='ru').lower()
    except sr.UnknownValueError:
        create_log(f'\nERROR: Unknown value detected', 'error')
        return ''
    except sr.RequestError:
        create_log(f'\nERROR: Check internet connection', 'error')
        return ''

    return user_sentence
