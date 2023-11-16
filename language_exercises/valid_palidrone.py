""" this script will determine if a given string is a palidrone """

s1 = 'L e v e l'
s2 = 'civil'
s3 = 'jeffrey'
s4 = 'civic'

def is_palidrome(s: str) -> bool:
    collapsedStr = s.lower().replace(' ', '')
    reversedStr = ''.join(reversed(collapsedStr))
    return collapsedStr == reversedStr

print(is_palidrome(s1))
print(is_palidrome(s2))
print(is_palidrome(s3))
print(is_palidrome(s4))