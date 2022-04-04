'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2021.07.10
Hosung.Kim
---------------------
BOJ 1085
https://www.acmicpc.net/problem/1085
=====================
'''

x, y, w, h = map(int, input().split())
print(min(abs(w-x), abs(h-y), abs(x), abs(y)))