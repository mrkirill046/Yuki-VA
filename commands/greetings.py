# Imports | kazuha046 creator
import random

from components.assistant_voice_play import play_voice_assistant

# Variable
greetings = [
    'Привет',
    'Здравствуй',
    'Добрый день',
    'Добрый вечер',
    'Доброе утро',
    'Приветствую',
    'Приветик',
    'Приветствую тебя',
    'Здравствуйте',
    'Доброго времени суток',
    'Хорошего дня',
    'Отличного настроения',
    'Рада тебя видеть',
    'Давно не виделись',
    'Рада тебя слышать',
    'Хорошего утра',
    'Удачного дня',
    'Прекрасного дня',
    'Рада встрече',
    'Рада видеть',
    'Отличный день',
    'Замечательный день',
    'Счастливого дня',
    'Чудесного вечера',
    'Радостного вечера',
    'Прекрасного вечера',
    'Великолепного дня',
    'Вдохновляющего дня',
    'Рада видеть тебя',
    'Приятного времени суток',
    'Замечательного вечера',
    'Чудесного утра',
    'Доброго дня',
    'Позитивного дня',
    'Светлого вечера',
    'Яркого дня',
    'Радостного утра',
    'Благоприятного дня',
    'Успешного вечера',
    'Приятного дня',
    'Вдохновляющего вечера',
    'Счастливого времени суток',
    'Волшебного дня',
    'Светлого времени суток',
    'Радостного времени суток',
    'Великолепного времени суток',
    'Добрый вечерочек',
    'Приветствую, как настроение?',
    'Привет, чем занимаешься?',
    'Привет, как твои дела?',
    'Добрый день, как ты?',
    'Рада знакомству',
    'Доброе утро, хорошего дня',
    'Привет, как проходит день?',
    'Здравствуй, как жизнь?',
    'Привет, радости тебе',
    'Добрый вечер, как дела?',
    'Рада приветствовать',
    'Привет, как настроение сегодня?',
    'Привет, давно не виделись!',
    'Доброе утро, как ты?',
    'Приветствую, как жизнь?',
    'Привет, хорошего вечера!',
    'Привет, чудесного дня!',
    'Привет, как ты сегодня?',
    'Доброе утро, как настроение?',
    'Здравствуй, что нового?',
    'Привет, как твои дела?',
    'Добрый день, что интересного?',
    'Приветствую, радостного дня!',
    'Доброе утро, хорошего настроения!',
    'Привет, хорошего времени суток!',
    'Привет, как выходные?',
    'Привет, какие планы на день?'
]


# Method
def play_greetings(*args):
    play_voice_assistant(random.choice(greetings))
