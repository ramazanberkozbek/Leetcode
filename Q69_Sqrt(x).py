def mySqrt(x):
    left, right = 0, x
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif x < mid * mid:
            right = mid - 1
        else:
            left = mid + 1

print(mySqrt(0))  #Output: 0
print(mySqrt(17)) #Output: 4
print(mySqrt(16)) #Output: 4