'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2022.02.21
Hosung.Kim
---------------------
BOJ 1051
https://www.acmicpc.net/problem/1051
=====================
'''

n, m = map(int, input().split())

numLst = []
for i in range(n) :
    numLst.append(list(input()))
num = min(n, m)

for size in range(num) :
    for i in range(n - num + size) :
        for j in range(m - num + size) :
            if numLst[i][j] == numLst[i+num-size][j] == numLst[i][j+num-size] == numLst[i+num-size][j+num-size] :
                print((num-size+1)**2)
                quit()

print(1)