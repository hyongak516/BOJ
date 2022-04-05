'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2022.04.05
Hosung.Kim
---------------------
BOJ 1259
https://www.acmicpc.net/problem/1259
=====================
'''

num = input()
while num != "0" :
    if num == num[::-1] :
        print("yes")
    else :
        print("no")
    num = input()