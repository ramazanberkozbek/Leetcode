"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

"""

def findMaxAvarage(nums,k):
    left = 0
    toplam = sum(nums[0:k])
    res = 0
    
    for right in nums[k:]:
        toplam = toplam - nums[left] + right
        left += 1
        res = max(res,toplam)
    return  res/k
        
        
print(findMaxAvarage(nums = [9,7,3,5,6,2,0,8,1,9], k = 6))