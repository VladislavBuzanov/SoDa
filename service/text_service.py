import nltk
import pymorphy2

from service import tokenizer, spellchecker


def handle_text(text):
    keywords = get_response(text)
    list = []
    for word in keywords:
        list.append(spellchecker.correct(word))
    return list


def get_response(message):
    lst = tokenizer.tokenize(message)
    keywords = []
    for word in lst:
        lemma = pymorphy2.MorphAnalyzer().parse(word)[0].normal_form
        keywords.append(lemma)
    print(keywords)
    return set(keywords)
