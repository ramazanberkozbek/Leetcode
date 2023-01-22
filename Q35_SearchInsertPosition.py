"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""
# O(log n)
def search(nums,target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
        
liste = [1,3,5,7]
print(search(liste,6))

"""
O(n)
def searchInsert(nums,target):
    if target in nums:
        return nums.index(target)
    for i in nums:
        if target < i:
            return nums.index(i)
            #liste.insert(nums.index(i),target)
            #break
        elif i == nums[-1]:
            return len(nums) + 1
            #liste.append(target)
            #break
    
liste = [1,3,5,6]
print(searchInsert(liste,5))
"""
