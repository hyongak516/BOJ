'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2021.07.09
Hosung.Kim
---------------------
BOJ 1157
https://www.acmicpc.net/problem/1157
=====================
'''

inputStr = input()
inputStr = inputStr.upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = []

for i in range(len(alphabet)) :
    count.append(0)

for i in range(len(inputStr)) :
    for j in range(len(alphabet)) :
        if alphabet[j] == inputStr[i] :
            count[j] += 1

if count.count(max(count)) == 1 :
    print(alphabet[count.index(max(count))])
else :
    print("?")