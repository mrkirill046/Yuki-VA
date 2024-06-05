# Imports | kazuha046 creator
import os
from components.voice_to_text import recognize_voice
from components.intent_recognition import get_intent, prepare_classifier
from components.assistant_image import show_assistant_window
from tools.execute_command import execute_command_with_intent
import threading


# Methods
def main_loop():
    while True:
        sentence = recognize_voice()
        os.remove('user_audio.wav')
        print(f'\nUSER SENTENCE: {sentence}')

        intent = get_intent(sentence)

        if intent:
            execute_command_with_intent(intent)
        else:
            print('ERROR: Command not found')


# Run
if __name__ == '__main__':
    prepare_classifier()
    assistant_thread = threading.Thread(target=show_assistant_window)
    assistant_thread.start()

    main_loop()
