'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2022.04.04
Hosung.Kim
---------------------
BOJ 1252
https://www.acmicpc.net/problem/1252
=====================
'''

bNum1, bNum2 = input().split()

bNum1 = bNum1[::-1]
bNum2 = bNum2[::-1]

num1 = 0
for i in range(len(bNum1)) :
    num1 += 2**i * int(bNum1[i])

num2 = 0
for i in range(len(bNum2)) :
    num2 += 2**i * int(bNum2[i])

sumNum = num1 + num2

print(bin(sumNum)[2:])