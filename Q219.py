"""

Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

def containsNearbyDuplicate(nums,k):
        numsDict = {}
        for i in range(len(nums)):
            if nums[i] in numsDict and abs(numsDict[nums[i]] - i) <= k:
                return True
            numsDict[nums[i]] = i
        return False
        
print(containsNearbyDuplicate(nums = [1,2,3,1], k = 3))

#ilk deneme
"""def containsNearbyDuplicate(nums,k) -> bool:
    numsDict = {}
    for i in range(len(nums)):
        if nums[i] not in numsDict:
            numsDict[nums[i]] = i
        else:
            if abs(numsDict[nums[i]] - i) <= k:
                return True
            else:
                numsDict[nums[i]] = i
    return False    

print(containsNearbyDuplicate(nums = [1,0,1,1], k = 1))"""