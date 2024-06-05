# Imports | kazuha046 creator
import webbrowser

from components.assistant_voice_play import play_voice_assistant


# Method
def search_in_google(*args: tuple):
    if not args[0]:
        return

    search_term = ' '.join(args[0])
    url = f'https://www.google.com/search?q={search_term}'
    webbrowser.get().open(url)
    play_voice_assistant('Открываю ваш запрос в google')
