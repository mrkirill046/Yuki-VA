# Imports | kazuha046 creator
from gtts import gTTS

import tools.manage_programm
import playsound
import tempfile


# Methods
def play_voice_assistant(text: str):
    tts = gTTS(text=text, lang='ru', slow=False)

    if tools.manage_programm.start:
        with tempfile.NamedTemporaryFile(delete=True) as fp:
            temp_file = f"{fp.name}.mp3"
            tts.save(temp_file)
            playsound.playsound(temp_file)
