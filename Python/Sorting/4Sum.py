class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sets=[]
        length=len(nums)
        nums=sorted(nums)
        for a in range(0,length):
            if (length-a)<3:
                break

            for b in range(a+1,(length)):
                if (length-b)<2:
                    break                
                for c in range(b+1,length):
                    if (length-c)<1:
                        break                

                    for d in range(c+1,length):
                        if (length-d)<0:
                            break                

                        if(nums[a]+nums[b]+nums[c]+nums[d]==target):
                            val=[nums[a],nums[b],nums[c],nums[d]]
                            if val not in sets:
                                sets.append(val)

        return sets
        

s=Solution()
print(s.fourSum([1,0,-1,0,-2,2],0))