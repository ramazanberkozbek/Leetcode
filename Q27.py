"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.    
"""

#First Solution without optimization
def merge(nums1,nums2,m,n):
    if n == 0:
        pass
    else:
        for i in range(n):
            nums1[m + i] = nums2[i]
    nums1.sort()
    
    
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1,nums2,m,n)


#Second Solution with optimization
def merge(nums1,nums2,m,n):
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:     #eğer nums1'in en büyüğü nums2'nin en büyüğünden büyükse
            nums1[m+n-1] = nums1[m-1]   #nums1'in en büyüğünü nums1'in en sonuna koy
            m -= 1                      #nums1 i azalttığın için m den 1 çıkar
        else:                           #eğer üstteki koşul sağlanmıyorsa(yani nums2'nin en büyüğü nums1'in en büyüğünden büyükse)
            nums1[m+n-1] = nums2[n-1]   #nums1'in sonuna nums2'nin en büyüğünü koy
            n -= 1                      #nums2 i azalttığın için n den 1 çıkar
    # Eğer nums2'de hala eleman varsa, bunları nums1'e ekleyin
    if n > 0:
        nums1[:n] = nums2[:n]
     
    
nums1 = [1,2,7,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1,nums2,m,n)
print(nums1)
print(nums2)