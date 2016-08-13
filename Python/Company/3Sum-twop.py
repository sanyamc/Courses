"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


"""
Solution: easiest is to do an inner loop but that will increase the complexity, more optimal solution would be 
to create a hashtable with two sums, that will be O(n2) and have index as values"

" finally search for the missing values and have global "
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        find two values whose sum is target
        :rtype: List[List[int]]
        """
        result=[]
        length=len(nums)

        for i in range(0,len(nums)):
            val=nums[i]
            
            if target-val in nums[i+1:]:
                # print(target-val)
                #print(nums[i:])
                temp = [val,target-val]
                result.append(temp)
                #print(result)
            while(i+1 <length and nums[i]==nums[i+1]):
                i+=1
        #print(result)
        return result


    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length=len(nums)
        if length==0:
            return []
        nums=sorted(nums)
        result=[]
        for i in range(0,length):
            val=nums[i]
            twoSums=self.twoSum(nums[i+1:],-nums[i])
            if len(twoSums)>0:
                for j,value in enumerate(twoSums):
                    #print(value)
                    temp=[]
                    temp+=value
                    temp.append(val)
                    if temp not in result:
                        result.append(temp)
            while((i+1) < length and nums[i]==nums[i+1]):
                i+=1
                
                    #twoSums[j].append(val)
#            result += twoSums

        #print(result)
        return result


        



a = [-1, 0, 1, 2, -1, -4]
#a= [-1,0,1,2,-1,-4]
s=Solution()
s.threeSum(a)



