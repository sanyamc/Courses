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
