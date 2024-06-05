# Imports | kazuha046 creator
import webbrowser

from components.assistant_voice_play import play_voice_assistant


# Method
def play_youtube_video(*args: tuple):
    if not args[0]:
        return

    search_term = ' '.join(args[0])
    url = f'https://www.youtube.com/results?search_query={search_term}'
    webbrowser.get().open(url)
    play_voice_assistant('Открываю страницу поиска ютуба')

