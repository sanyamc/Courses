#Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

#For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
#the contiguous subarray [4,−1,2,1] has the largest sum = 6

# at any given moment f(n) = max(f(n), current_max+(elements from last max....n),current_max


############## solution for max subarray of even non-contiguous
# class Solution(object):
#     def maxSubArray(self,nums):
#         l=len(nums)
#         if(l<1):
#             return 0
#         m=nums[0]
#         prev_max=m
#         indexes=[0]
#         i=1
#         while(i<l):
#             if(nums[i]+prev_max>nums[i] and nums[i]+prev_max>prev_max):
#                 prev_max=prev_max+nums[i]
#             elif(nums[i]+prev_max<nums[i]):
#                 prev_max=nums[i]
#             if(m<prev_max):
#                 m=prev_max
#                 indexes.append(i)
            
#             i+=1
#         print(indexes)
#         return m

# below is the solution to CONTIGIOUS subarray, not max sum subarray
# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         l=len(nums)
#         if(l<1):
#             return 0
#         m=nums[0]
#         max_index=0
#         prev_max=m
#         i=1
#         while(i<l):
#             if(nums[i]+prev_max>nums[i]):
#                 prev_max=nums[i]+prev_max
#             else:
#                 prev_max=nums[i]
#             if(m<prev_max):
#                 m=prev_max

#                 #j=max_index+1
#                 #temp=m
#                 #while(j<=i):
#                 #    temp+=nums[j]
#                 #    j+=1
#                 #if(nums[i]>temp and nums[i]>m):
#                 #    m=nums[i]
#                 #    max_index=i
#                 #elif(temp>m):
#                 #    m=temp
#                 #    max_index=i
                
#                 #if(temp>m):
#                 #    m=temp
#                 #    max_index=i
#                 #elif(temp>nums[i]):
#                 #    m=temp
#                 #    max_index=i
#                 #else:
#                 #    m=nums[i]
#             print("max: "+str(m)+" prev max: "+str(prev_max))
                
#             i+=1
            
#             #return max
        

s=Solution()

#arr=[-2,1,-3,4,-1,2,1,-5,4]
#arr=[-2,-1]
arr=[8,-19,5,3,20]
prev = [8,-11,5,3,21]
print(s.maxSubArray(arr))

            


