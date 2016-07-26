class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_length=len(nums)
        if total_length<=2:
            return total_length
        count=0
        length=0
        ptr=0
        prev=None
        for i in range(0,total_length):
            #print("ptr: "+str(ptr)+" count:"+str(count))
            if prev==nums[i] and count<2:
                count+=1
                nums[ptr]=nums[i]
                ptr+=1

            elif prev!=nums[i]:
                length+=count
                count=1
                prev=nums[i]
                nums[ptr]=nums[i]
                ptr+=1
                
            if(i==total_length-1):
                #print(str(count)+" count")
                length+=count
        #if(length==0):
        #    length=count
        print(nums[-1])
        return ptr




s=Solution()
print(s.removeDuplicates([4,4,4,4,2,2,2,2,3,3,3,3,3,3,3]))
print(s.removeDuplicates([1,1,2,2,3,3]))
print(s.removeDuplicates([1,2,3,3,3]))

        