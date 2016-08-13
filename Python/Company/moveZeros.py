class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeros=nums.count(0)

        
        for i in range(0,zeros):
            nums.remove(0)
        for i in range(0,zeros):
            nums.append(0)

        print(nums)


s=Solution()
a=[1,0,4,5,0,8,10]
#a=[0,0,1]
s.moveZeroes(a)
