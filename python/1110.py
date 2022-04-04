'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2021.07.11
Hosung.Kim
---------------------
BOJ 1110
https://www.acmicpc.net/problem/1110
=====================
'''

inputNum = int(input())

def countCycle(num) :
    pNum = num//10 + num%10
    pNum2 = num%10*10 + pNum%10
    if pNum2 == inputNum :
        return 1
    else :
        return 1 + countCycle(pNum2)
    
print(countCycle(inputNum))