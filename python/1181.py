'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2021.07.15
Hosung.Kim
---------------------
BOJ 1181
https://www.acmicpc.net/problem/1181
=====================
'''

import sys

repeatCount = int(sys.stdin.readline())

wordLst = []

for i in range(repeatCount) :
    wordLst.append(sys.stdin.readline().strip())

wordSet = set(wordLst)
wordLst = list(wordSet)
wordLst.sort()

lenLst = tuple(map(len, wordLst))

for i in range(50) :
    word = []
    for j in range(len(wordLst)) :
        if i+1 == lenLst[j] :
            word.append(wordLst[j])
    for j in word :
        print(j)