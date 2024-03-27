""" Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal."""

import math
def plusminus(numberList: list) -> None:
    posCnt = 0;
    negCnt = 0;
    zeroCnt = 0;
    size = len(numberList)

    for number in numberList:
        if(number > 0):
            posCnt += 1;
        elif (number < 0):
            negCnt += 1;
        else:
            zeroCnt += 1;

    # need to print results with 6 digits of precision
    print(f'postive ratio = {posCnt/size:.6f}')
    print(f'negative ration = {negCnt/size:.6f}')
    print(f'zero ration = {zeroCnt/size:.6f}')


plusminus([1,1,0,-1,-1])
plusminus([-4, 3, -9, 0, 4, 1])