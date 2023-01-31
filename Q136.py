def singleNumber(nums) -> int:
    return (2*sum(set(nums)) - sum(nums))

print(singleNumber([1,2,3,3,2]))

#solution 2 with dict
def singleNumber(nums):
    frequency_dict = {}
    for item in nums:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    for i in nums:
        if frequency_dict.get(i) == 1:
            return i
        
print(singleNumber([1,2,3,3,2]))
