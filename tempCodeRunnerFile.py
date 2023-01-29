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