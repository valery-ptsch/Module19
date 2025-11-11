from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

# Список нецензурных слов для фильтрации
CENSORED_WORDS = [
    'редиска', 'негодяй', 'подлец', 'мерзавец', 'скотина'
]


@register.filter
@stringfilter
def censor(value):
    if not isinstance(value, str):
        return value

    result = value
    for word in CENSORED_WORDS:
        # Заменяем все вхождения слова (с учетом регистра первой буквы)
        lower_word = word.lower()
        capitalized_word = word.capitalize()

        # Заменяем слово в нижнем регистре
        result = result.replace(lower_word, lower_word[0] + '*' * (len(word) - 1))
        # Заменяем слово с заглавной буквы
        result = result.replace(capitalized_word, capitalized_word[0] + '*' * (len(word) - 1))

    return result