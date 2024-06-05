# Imports | kazuha046 creator
import os
from components.voice_to_text import recognize_voice
from components.intent_recognition import get_intent, prepare_corpus
from components.assistant_window import show_assistant_window
from tools.execute_command import execute_command_with_intent
import threading


# Methods
def main_loop():
    while True:
        sentence = recognize_voice()
        os.remove('user_audio.wav')
        print(f'\nUSER SENTENCE: {sentence}')

        voice_input_parts = sentence.split(' ')

        if len(voice_input_parts) == 1:
            intent = get_intent(sentence)

            if intent:
                execute_command_with_intent(intent)
            else:
                print('ERROR: Command not found')

        if len(voice_input_parts) > 1:
            for guess in range(len(voice_input_parts)):
                intent = get_intent((' '.join(voice_input_parts[0:guess])).strip())
                if intent:
                    command_options = [voice_input_parts[guess:len(voice_input_parts)]]
                    execute_command_with_intent(intent, *command_options)
                    break
                if not intent and guess == len(voice_input_parts) - 1:
                    print('ERROR: Command not found')


# Run
if __name__ == '__main__':
    prepare_corpus()
    assistant_thread = threading.Thread(target=show_assistant_window)
    assistant_thread.start()

    main_loop()
