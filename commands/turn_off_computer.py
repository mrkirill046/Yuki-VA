# Imports | kazuha046 creator
import os

from components.assistant_voice_play import play_voice_assistant


# Method
def turn_off_computer(*args):
    play_voice_assistant('Хорошо, выключаю ваш компьютер!')

    if os.name == 'nt':
        os.system('C:/Windows/System32/shutdown.exe /s /t 0')
    if os.name == 'posix':
        os.system('shutdown -h now')
    else:
        print('\nERROR: This OS id does not support this operation')
