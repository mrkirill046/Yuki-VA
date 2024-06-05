# Imports | kazuha046 creator
import speech_recognition as sr

# Variables
recognizer = sr.Recognizer()
microphone = sr.Microphone()


# Methods
def record_audio():
    with microphone as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=1)

        try:
            print('\nLOG: Say something...')
            audio = recognizer.listen(mic, 0, 5)

            with open('user_audio.wav', 'wb') as file:
                file.write(audio.get_wav_data())
        except sr.WaitTimeoutError:
            print(f'\nERROR: Check your microphone and try again')
            return None

        return audio


def recognize_voice():
    audio = record_audio()
    if not audio:
        return

    try:
        user_sentence = recognizer.recognize_google(audio, language='ru').lower()
    except sr.UnknownValueError:
        print(f'\nERROR: Unknown value detected')
        return
    except sr.RequestError:
        print(f'\nERROR: Check internet connection')
        return

    return user_sentence
