""" this script will determine if the two prpvided strings are anagrams of each other """

s1 = 'anagram'
s2 = 'grmanaa'

s1_no = 'car'
s2_no = 'cat'

def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    else:
        for i in range(len(s1)):
            if not s1[i] in s2:
                return False

    return True

print(is_anagram(s1, s2))
print(is_anagram(s1_no, s2_no))

