"""Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?"""


class Solution(object):
    # def wiggleHelper(self,nums):
    #     length=len(nums)
    #     for i in range(1,length):
    #         val=nums[i]
    #         if(i==1 and val<nums[0]):
    #             nums[i]=nums[0]
    #             nums[0]=val
    #         if(i%2==0):                
    #             if(i+1 < length):
    #                 #print("val: "+str(val)+" nums[i-1] "+str(nums[i-1])+" nums[i+1] "+str(nums[i+1]))
    #                 min_val = min(val,nums[i-1],nums[i+1])
    #                 if( val==min_val):
    #                     #val < nums[i-1] and val < nums[i+1]):
    #                     #print("continuing")
    #                     continue
    #                 elif(min_val==nums[i-1]):
    #                         temp = nums[i-1]
    #                         nums[i-1]=nums[i]
    #                         nums[i]=temp
    #                 else:
    #                         temp = nums[i+1]
    #                         nums[i+1]=nums[i]
    #                         nums[i]=temp

    #             else:                    
    #                 if(val>nums[i-1]):                        
    #                     nums[i]=nums[i-1]
    #                     nums[i-1]=val
        
    # def wiggleSort(self,nums):
    #     """ assuming every input has a Solution
    #         rtype: None, modify in place
    #         type:nums: list[int]

    #     """
    #     length=len(nums)
    #     if length==0 or length==1:
    #         return
    #     # even should be less than neighbours, odd should be greater than neighbours
    #     self.wiggleHelper(nums)

    #     print(nums)
    #     hasdupes=False
    #     for i in range(1,length):
    #         val=nums[i-1]
    #         if val==nums[i]:
    #             temp=nums[i:]+nums[:i]
    #             nums=[1,2,3,4]
    #             print(nums)
        #         hasdupes=True
        #         if(i-3>=0):
        #             temp=nums[i-3]
        #             nums[i-3]=val
        #             nums[i-1]=temp
        #         if(i+2 < length):
        #             temp=nums[i+2]
        #             nums[i+2]=nums[i]
        #             nums[i]=temp
        # print(nums)
        # if(hasdupes):
        #     self.wiggleHelper(nums)

    def wiggleSort(self,nums):
        flag = True
        for i in range(0,len(nums)-1):
            if (flag and nums[i] > nums[i+1]) or (not flag and nums[i] < nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
            i += 1
            flag = not flag

            




s= Solution()
nums = [1, 5, 1, 1, 6, 4]
nums = [1, 3, 2, 2, 3, 1]
nums = [1,2,3,3,4,4,5,5]
#nums=[1,2,3,4,5]
#nums=[5,4,3,2,1]
#nums=[4,5,5,2]
nums=sorted(nums)#[1, 3, 2, 2, 3, 1]
nums=[1,2,2,1,2,1,1,1,1,2,2,2]
nums=[4,5,5,6]
s.wiggleSort(nums)
print(nums)


                    

                     

