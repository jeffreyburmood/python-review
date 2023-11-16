""" this script will determine if the brackets in a string match correctly """

def bracketMatcher(strparam: str) -> int:
    left_bracket = strparam.count('(')
    right_bracket = strparam.count(')')
    if left_bracket == right_bracket:
        return 1
    else:
        return 0


print(bracketMatcher('(coder)(byte)'))
print(bracketMatcher('(c(oder)(b(yte))'))