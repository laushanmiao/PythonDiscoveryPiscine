#!/usr/bin/env python3

print("Enter a number")
num1 = int(input())
num2 = 0
while num2 < 10:
	num3 = num1 * num2
	print(f"{num2} x {num1} = {num3}")
	num2 += 1
