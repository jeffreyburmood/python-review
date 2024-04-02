"""Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings."""

def strings_xor(s1: str, s2: str) -> str:
    result = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            result = result + '0'
        else:
            result = result + '1'

    return str(result)

print(strings_xor("10101", "00101"))