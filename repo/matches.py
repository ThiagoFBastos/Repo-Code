from unidecode import unidecode
from random import randrange

def find_patterns(words, text):
    S = list(reversed(sorted(words, key = lambda s: len(s))))
    pat = set()

    hi = 0

    def check(a, b, k):
        if k + len(a) > len(b):
            return False
        return b[k : k + len(a)] == a

    for i in range(len(text)):
        for w in S:
            if check(w, text, i) and hi < i + len(w):
                hi = i + len(w)
                pat.add(w)
                break
    
    return list(pat)
