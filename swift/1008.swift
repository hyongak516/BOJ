/*
Copyright (c) 2022 by Hosung.Kim <hyongak516@mail.hongik.ac.kr>
=====================
2022.04.04
Hosung.Kim
---------------------
BOJ 1008
https://www.acmicpc.net/problem/1008
=====================
*/

let num = readLine()!.split(separator: " ").map{Double(String($0))!}

print(num[0] / num[1])
