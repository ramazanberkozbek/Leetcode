"""

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


def longestConsecutive(nums):
    nums = set(nums)
    longest = 0
    for i in nums:
        longes = 1
        if (i-1) not in nums:
            while (i+longes in nums):
                longes +=1
        longest = max(longes,longest)
    return longest                

print(longestConsecutive([100,4,200,1,3,2]))