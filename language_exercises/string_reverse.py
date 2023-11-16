""" this script will reverse the characters in a striing and return the result """

s1 = 'having fun'
s2 = 'enjoy your life'

def firstReverse(s: str) -> str:
 return ''.join(reversed(s))


print(firstReverse(s1))
print(firstReverse(s2))

