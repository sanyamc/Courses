class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length=len(nums)
        if(length==0):
            return []
        if(length==1):
            return [[],[nums[0]]]
        nums=sorted(nums)
        records=[[[]],[[],[nums[0]]]]
        prev=0
        for i in range(1,length):
            prev=len(records)
            val=records[prev-1][:]
            print(val)
            for k in range(0,len(val)):
                temp = val[k][:]
                temp.append(nums[i])
                if(temp not in val):
                    val.append(temp)
            if([nums[i]] not in val):
                val.append([nums[i]])
            records.append(val)
        #print(records)

        return records[len(records)-1]

s=Solution()
print(s.subsetsWithDup([4,1,0]))


 