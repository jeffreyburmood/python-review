""" this script will determine the longest word in an input string comprised of multiple words """

def returnLongest(input: str) -> str:
 splitter = list(input.split(' '))
 max = 0
 for string in splitter:
     if len(string) > max:
         max = len(string)
         max_str = string

 return max_str


print(returnLongest('fun$!! times'))
print(returnLongest('supercalifragolistic morefun time!'))