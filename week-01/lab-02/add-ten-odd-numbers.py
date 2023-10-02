#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
j = int(input())

abc = a * (a % 2) + b * (b % 2) + c * (c % 2)
ddf = d * (d % 2) + e * (e % 2) + f * (f % 2)
ghi = g * (g % 2) + h * (h % 2) + i * (i % 2) + j * (j % 2)
print(abc + ddf + ghi)
