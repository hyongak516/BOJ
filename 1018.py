'''
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2021.07.11
Hosung.Kim
---------------------
BOJ 1018
https://www.acmicpc.net/problem/1018
=====================
'''

height, width = map(int, input().split())

chessMap = []
chessLst = ["BWBWBWBW", "WBWBWBWB"]

for i in range(height) :
    chessMap.append(input())
result = 64
for k in range(width-7) :
    for l in range(height-7) :
        count = 0
        for i in range(8) :
            for j in range(8) :
                if chessMap[i+l][j+k] != chessLst[i%2][j] :
                    count += 1
        if count > 32 :
            if 64-count < result :
                result = 64-count
        else :
            if count < result :
                result = count
                
print(result)