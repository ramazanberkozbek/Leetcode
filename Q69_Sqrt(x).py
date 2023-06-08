"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python."""
def mySqrt(x):
    l,r = 0,x
    while l <= r:
        mid = l + (r-l) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid > x:
            r = mid - 1
        else:
            l = mid + 1

print(mySqrt(0))  #Output: 0
print(mySqrt(17)) #Output: 4
print(mySqrt(16)) #Output: 4