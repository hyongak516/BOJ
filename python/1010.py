'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2022.02.22
Hosung.Kim
---------------------
BOJ 1010
https://www.acmicpc.net/problem/1010
=====================
'''

import math

count = int(input())
for i in range(count) :
    a, b = map(int, input().split())
    print(math.factorial(b) // math.factorial(a) // math.factorial(b-a))