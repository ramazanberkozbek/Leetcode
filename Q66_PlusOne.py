"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example:
    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    Incrementing by one gives 123 + 1 = 124.
    Thus, the result should be [1,2,4].
"""
#Solution 1
def onePlus(digits):
    n = len(digits)    
    digits[-1] += 1
    
    for i in range(n-1,0,-1):
        if digits[i] == 10:
            digits[i] = 0
            digits[i-1] += 1
    if digits[0] == 10:
        digits[0] = 0 
        digits.insert(0,1)
    return digits
        
print(onePlus([1,2,3,4,5,6]))

print("--------")
#Solution 2
def onePlus(arr):
    digits = ""
    for i in arr:
        digits += str(i)
        
    digits = int(digits) + 1

    newList = []

    for i in str(digits):
        newList.append(int(i))
    return newList
    
print(onePlus([1,2,0,9]))

print("--------")

#Solution 3
def onePlus(digits):
    return [int(i) for i in str(int("".join(map(str, digits)))+1)]

print(onePlus([1,2,9,9])) 