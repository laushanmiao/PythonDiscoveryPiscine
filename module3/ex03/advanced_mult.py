#!/usr/bin/env python3

num1 = 0

while num1 <= 10:
	num2 = 0
	print(f"Table of {num1}: ", end=" ")
	while num2 <= 10:
		num3 = num1 * num2
		print(num3, end=" ")
		num2 += 1
	num1 += 1
	print( )
