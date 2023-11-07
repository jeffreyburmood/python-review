
s1 = 'L e v e l'
s2 = 'civil'
s3 = 'jeffrey'
s4 = 'civic'

def isPalidrome(input:str) -> bool:
    s = input.lower().replace(' ', '')
    s_reverse = ''.join(reversed(s))  # this is how you iteratively make a new string
    return s == s_reverse


print(isPalidrome(s1))
print(isPalidrome(s2))
print(isPalidrome(s3))
print(isPalidrome(s4))