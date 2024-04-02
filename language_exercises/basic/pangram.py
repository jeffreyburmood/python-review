""" A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether
    it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate."""

def is_pangram(s:str) -> str:
    s2 = s.lower()
    basestr = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(0, len(basestr)):
        if s2.find(basestr[i]) == -1:
            return 'not pangram'

    return 'pangram'

print(is_pangram('i am trying this out'))
print(is_pangram('We promptly judged antique ivory buckles for the next prize'))
print(is_pangram('We promptly judged antique ivory buckles for the prize'))