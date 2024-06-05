# Imports | kazuha046 creator
from gtts import gTTS
import playsound
import tempfile


# Methods
def play_voice_assistant(text: str):
    tts = gTTS(text=text, lang='ru', slow=False)
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        temp_file = f"{fp.name}.mp3"
        tts.save(temp_file)
        playsound.playsound(temp_file)
