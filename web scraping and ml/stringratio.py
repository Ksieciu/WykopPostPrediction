from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


print(similar("bocian", "bocianek"))
# koło 0.8 ratio ustawić do rozpoznawania słów?
# raczej nieco powyżej 0.8
