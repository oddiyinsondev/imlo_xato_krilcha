from difflib import get_close_matches
from uzwords import words


def chek_up(word, words=words):
    word = word.lower()

    matches = set(get_close_matches(word, words))
    awailable = False

    if word in matches:
        awailable = True
        matches = word
    elif 'х' in word:
        word = word.replace('х', 'ҳ')
        matches.update(get_close_matches(word, words))
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words))

    return {'awailable': awailable, 'matches':matches}

if __name__ == '__main__':
    print(chek_up("Салом"))
    print(chek_up("Севги"))
    print(chek_up("Сииз"))
    print(chek_up("Олма"))
    print(chek_up("Алма"))
