# Imports | kazuha046 creator
import random

from components.assistant_voice_play import play_voice_assistant

# Variable
partings = [
    'Пока',
    'До свидания',
    'До скорой встречи',
    'Удачи',
    'Всего доброго',
    'Счастливо',
    'До новых встреч',
    'До встречи',
    'До скорого',
    'Береги себя',
    'Будь здоров',
    'До свидания, дорогой друг',
    'Будьте осторожны',
    'Пока-пока',
    'До вечера',
    'Пока, увидимся',
    'Удачи вам',
    'До завтра',
    'Приятно было пообщаться',
    'До следующего раза',
    'Жду встречи с нетерпением',
    'Пусть всегда сопутствует удача',
    'Счастливого дня',
    'До скорого свидания',
    'До встречи позже',
    'Пока, не скучайте',
    'Удачи в делах',
    'Пока, дорогие друзья',
    'До новых встреч, мой друг',
    'До скорой встречи, дорогие',
    'Всего хорошего',
    'Пусть у вас всегда будет счастливый день',
    'Счастливого пути вам',
    'Возвращайтесь скорее',
    'Счастливо оставаться',
    'До свидания, желаю успехов',
    'До новых встреч, уважаемые',
    'Пока, не забывайте о нас',
    'До скорой встречи, хорошего дня',
    'Берегите себя, до скорого',
    'До новых встреч, всего доброго',
    'Пока, хорошего настроения',
    'До новых встреч, пока',
    'До свидания, будьте здоровы',
    'Удачи вам на пути к успеху',
    'До скорой встречи, счастливо',
    'До свидания, не забудьте вернуться',
    'Счастливого дня, до скорого',
    'До встречи, не пропадайте',
    'Удачи, пока',
    'До скорого, хорошего дня',
    'Будьте осторожны на дороге',
    'Пока, хорошего вам дня',
    'Успешного дня, пока',
    'До свидания, всего хорошего',
    'Счастливого дня, до скорого',
    'Пока, не забудьте вернуться',
    'До свидания, до скорого',
    'До скорой встречи, пока',
    'До встречи, удачи',
    'Приятного дня, пока',
    'До свидания, ждем вас снова',
    'Счастливого дня, до встречи',
    'До новых встреч, будьте здоровы',
    'Успешного дня, до свидания',
    'Пока, хорошего настроения вам',
    'Счастливо, до скорого',
    'До скорого, не пропадайте',
    'Счастливо, пока',
    'До новых встреч, до скорого',
    'Удачи вам, пока',
    'До встречи, не пропадайте',
    'Пока, хорошего дня вам',
    'Счастливо, до свидания',
    'До скорой встречи, будьте здоровы',
    'До новых встреч, удачи',
    'Пока, до встречи',
    'До свидания, желаю успехов'
]


# Method
def play_partings(*args):
    play_voice_assistant(random.choice(partings))
