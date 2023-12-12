"""Напишите код, который извлекает из строки все слова,
а затем выводит в порядке убывания частоты в этой строке
только те, у которых частота >1. В строке могут быть слова
на английском, знаки пунктуации, пробелы и урлы. Урл словом
не является и должен быть отброшен.
"""

import re
from collections import Counter

def extract_words(text):
    words = re.findall(
        r'\b\w+\b', re.sub(r'\b(?:https?://|www\.)\S+|\b\w+\.(?:org|com|[a-z]{2})\b', '', text.lower())
        )
    word_counts = Counter(words)
    sorted_words = sorted(
        (word for word, count in word_counts.items() if count > 1),
        key=word_counts.get, reverse=True
        )

    return [word for word in sorted_words]
