'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2021.07.11
Hosung.Kim
---------------------
BOJ 1193
https://www.acmicpc.net/problem/1193
=====================
'''

fractionNum = int(input())

num = 2
while num*(num-1)/2 < fractionNum :
    num += 1
    
temp = int(num*(num-1)/2 - fractionNum)

if num%2 == 0 :
    print(temp+1, num-1-temp, sep="/")
else :
    print(num-temp-1, temp+1, sep="/")