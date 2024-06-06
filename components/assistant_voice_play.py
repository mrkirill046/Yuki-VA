# Imports | kazuha046 creator
from gtts import gTTS

import pygame
import os
import tempfile


# Methods
def play_voice_assistant(text: str):
    tts = gTTS(text=text, lang='ru', slow=False)

    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
        temp_file = fp.name
        tts.save(temp_file)

    pygame.mixer.init()
    pygame.mixer.music.load(temp_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()
    pygame.mixer.quit()

    os.remove(temp_file)
