#!/usr/bin/env python3

num1 = float(input("Give me a number: "))
if num1%1 != 0:
    num1 = int(num1)+1
    print(num1)
else:
    num1 = int(num1)
    print(num1)

