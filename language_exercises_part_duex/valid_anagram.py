
s1 = 'anagram'
s2 = 'grmanaa'

s1_no = 'car'
s2_no = 'cat'

def is_anagram(str1: str, str2:str) -> bool:
    if len(str1) != len(str2):
        return False
    else:
        for i in range(len(str1)):
            if not str1[i] in str2:
                return False
    return True

print(is_anagram(s1, s2))
print(is_anagram(s1_no, s2_no))
