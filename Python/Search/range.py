
"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

"""

class Solution(object):
    def bs(self,nums,target):

        l=0
        u=len(nums)-1
        while(l<=u):
            mid=(l+u)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                u=mid-1
        if l<len(nums) and nums[l]==target:
            return l
            
    def searchRange(self,nums,target):
        """
        type:nums: List[int]
        type:target: int
        rtype: List[int]
        """
        if not nums:
            return None
        l=len(nums)
        if l==0:
            return [-1,-1]

        index = self.bs(nums,target)
        
        if index==None:
            return [-1,-1]
        
        left=index
        right=index
        while(left>=0 and nums[left]==target):
            left-=1
        while(right<l and nums[right]==target):
            right+=1
        

        return [left+1,right-1]


s=Solution()
print(s.searchRange([1],1))

        
        
