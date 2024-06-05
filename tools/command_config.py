# Variable | kazuha046 creator
from components.assistant_window import reshow_assistant_window, close_assistant_window
from commands.greetings import play_greetings
from commands.turn_off_computer import turn_off_computer
from commands.parting import play_partings
from commands.search_in_google import search_in_google
from commands.youtube import play_youtube_video

# Assistant config
commands_config = {
    'greetings': play_greetings,
    'farewell': play_partings,
    'youtube': play_youtube_video,
    'window_off': close_assistant_window,
    'window_on': reshow_assistant_window,
    'google': search_in_google,
    'computer_off': turn_off_computer
}
