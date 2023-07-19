"""
Given a string s, find the length of the longest 
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
def lengthOfLongestSubstring(s):
    sSet = set()
    left = 0
    res = 0
    
    for right in range(len(s)):
        while s[right] in sSet:
            sSet.remove(s[left])
            left += 1
            
        sSet.add(s[right])
        res = max(res, right - left + 1)
    return res

print(lengthOfLongestSubstring("abcabcbb"))
"""
#
from collections import defaultdict
def lengthOfLongestSubstring(s):
    longestDict = defaultdict(int)
    longestLength = 0
    i = 0

    for j in range(len(s)):
        if s[j] in longestDict:
            i = max(i, longestDict[s[j]] + 1)
        
        longestDict[s[j]] = j
        longestLength = max(longestLength, j - i + 1)
    return longestLength
            
"""

"""
#çok verimsiz ama ilk aklıma gelen

def lengthOfLongestSubstring(s):
    tempList = []
    longestList = []
    
    for i in range(len(s)):
        while i < len(s) and s[i] not in tempList:
            tempList.append(s[i])
            i += 1
        if len(longestList) < len(tempList):
            longestList = tempList
            
        tempList = []
    return len(longestList)
"""