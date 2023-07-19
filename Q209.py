"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""

def minSubArrayLen(target, nums):
    left,total = 0,0
    res = float('inf')
    
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            res = min(right - left + 1,res)
            total -= nums[left]
            left += 1
                    
    return res if res != float('inf') else 0

print(minSubArrayLen( target = 7, nums = [2,3,1,2,4,3]))