"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""

# for swapping remember to use (a,b)=(b,a)


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        length=len(nums)
        result=[]
        if(length==0):
            return result
        if(length==1):
            return [str(nums[0])]
        start=str(nums[0])
        range_len=1
        for i in range(1,length):
            val=nums[i]
            if(val-(nums[i-1]) ==1):
                range_len+=1
                continue
            else:
                if(range_len==1):
                    result.append(start)
                else:
                    result.append(start+"->"+str(nums[i-1]))
                start=str(val)
                range_len=1

        if(range_len==1):
            result.append(start)
        else:
            if(nums[-1]-nums[-2] == 1):
                result.append(start+"->"+str(nums[-1]))
            else:
                result.append(start+"->"+str(nums[i-1]))            
        return result

s=Solution()
nums = [0,1,2,4,5,7]
#nums = [0,1]
print(s.summaryRanges(nums))





