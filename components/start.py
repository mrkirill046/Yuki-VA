# Imports | kazuha046 creator
import os
import threading
import tools.manage_programm

from components.voice_to_text import recognize_voice
from components.intent_recognition import get_intent, prepare_corpus
from components.assistant_window import show_assistant_window
from components.tray_action import create_tray_icon
from components.assistant_voice_play import play_voice_assistant
from tools.execute_command import execute_command_with_intent
from tools.best_logging import create_log


# Method
def main_loop():
    play_voice_assistant('Виртуальный ассистент Юки включена!')

    while tools.manage_programm.start:
        sentence = recognize_voice()

        if os.path.exists('user_audio.wav'):
            os.remove('user_audio.wav')
        else:
            create_log('ERROR: Nothing to delete', 'error')

        create_log(f'\nUSER SENTENCE: {sentence}', 'info')

        voice_input_parts = sentence.split(' ')

        if sentence == '':
            create_log('ERROR: Nothing to do', 'error')
        else:
            if len(voice_input_parts) == 1:
                intent = get_intent(sentence)

                if intent:
                    execute_command_with_intent(intent)
                else:
                    play_voice_assistant('Команда не найдена')
                    create_log('\nERROR: Command not found', 'error')

            if len(voice_input_parts) > 1:
                for guess in range(len(voice_input_parts)):
                    intent = get_intent((' '.join(voice_input_parts[0:guess])).strip())
                    if intent:
                        command_options = [voice_input_parts[guess:len(voice_input_parts)]]
                        execute_command_with_intent(intent, *command_options)
                        break
                    if not intent and guess == len(voice_input_parts) - 1:
                        play_voice_assistant('Команда не найдена')
                        create_log('\nERROR: Command not found', 'error')


def start_assistant():
    prepare_corpus()
    assistant_thread = threading.Thread(target=show_assistant_window, daemon=True)
    trey_thread = threading.Thread(target=create_tray_icon, daemon=True)
    trey_thread.start()
    assistant_thread.start()

    main_loop()
