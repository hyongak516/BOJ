'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2022.02.25
Hosung.Kim
---------------------
BOJ 1094
https://www.acmicpc.net/problem/1094
=====================
'''

length = int(input())
num = 64
count = 0

while length % num != 0 :
    count += length // num
    length = length % num
    num = num // 2

print(count + 1)