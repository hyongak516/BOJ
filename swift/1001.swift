/*
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2022.04.04
Hosung.Kim
---------------------
BOJ 1001
https://www.acmicpc.net/problem/1001
=====================
*/

let num = readLine()!.split(separator: " ").map{Int(String($0))!}

print(num[0] - num[1])