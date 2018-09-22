#!/bin/python3

import sys

n = int(input().strip())

binary = bin(n)[2:] # bin(n) inbuilt python funtion
print(binary)
ones_only = binary.replace('0', ' ') #ones_only is string type
print(ones_only)
as_array = ones_only.split() #as_array is list wit string elemenst
print(as_array)
longest = max(as_array) # longest is string type
print(longest)

