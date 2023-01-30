"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""
#Recursive Solution #1
def tribonacci(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else: return tribonacci(x-1) + tribonacci(x-2) + tribonacci(x-3)
print(tribonacci(30))

#Solution 2
def tribonacci(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        a, b, c = 0, 1, 1
        for i in range(3, x+1):
            a, b, c = b, c, a+b+c
        return c
print(tribonacci(30))