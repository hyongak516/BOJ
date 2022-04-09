'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2022.04.04
Hosung.Kim
---------------------
BOJ 1297
https://www.acmicpc.net/problem/1297
=====================
'''

import math

d, h, w = map(int, input().split())
ratio = d/math.sqrt(h**2 + w**2)
print(math.floor(h * ratio))
print(math.floor(w * ratio))