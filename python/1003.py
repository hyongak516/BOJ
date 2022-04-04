'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2021.07.14
Hosung.Kim
---------------------
BOJ 1003
https://www.acmicpc.net/problem/1003
=====================
'''

import sys

repeatCount = int(sys.stdin.readline())
numLst = []

for i in range(repeatCount) :
    numLst.append(int(sys.stdin.readline()))
    
def createFibonacci(num) :
    fibonacci = [1, 0] + [0]*num
    for i in range(num) :
        fibonacci[2+i] = (fibonacci[i] + fibonacci[1+i])
    return fibonacci
        
fibonacciLst = createFibonacci(max(numLst))

for i in numLst :
    print(fibonacciLst[i], fibonacciLst[i+1])