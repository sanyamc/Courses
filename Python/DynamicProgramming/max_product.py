#Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

#For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
#the contiguous subarray [4,−1,2,1] has the largest sum = 6

# at any given moment f(n) = max(f(n), current_max+(elements from last max....n),current_max
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        if(l<1):
            return 0
        m=nums[0]
        max_index=0
        prev_max=m
        prev_min=m
        i=1
        while(i<l):
            m=max(m,prev_min*nums[i],prev_max*nums[i],nums[i])
            temp1=max(nums[i]*prev_max,nums[i],nums[i]*prev_min)
            temp2=min(nums[i]*prev_min,nums[i],nums[i]*prev_max)
            prev_max=temp1
            prev_min=temp2
            
            #temp=prev_max
            #curr_max=nums[i]*prev_max
            #curr_min=nums[i]*prev_min
            #if(curr_max>nums[i]):
            #    prev_max=curr_max
            #else:
            #    prev_max=nums[i]
            
            ##prev_max=max(nums[i]*prev_max,nums[i])
            #m=max(m,prev_max,curr_min)
            #prev_min=min(curr_min,nums[i],nums[i]*temp)
            #if(nums[i]*prev_min<prev_min):
            #    prev_min=nums[i]*prev_min
            #else:
            #    prev_min=nums[i]
            
            
            #if(m<prev_max):
            #    m=prev_max

                #j=max_index+1
                #temp=m
                #while(j<=i):
                #    temp+=nums[j]
                #    j+=1
                #if(nums[i]>temp and nums[i]>m):
                #    m=nums[i]
                #    max_index=i
                #elif(temp>m):
                #    m=temp
                #    max_index=i
                
                #if(temp>m):
                #    m=temp
                #    max_index=i
                #elif(temp>nums[i]):
                #    m=temp
                #    max_index=i
                #else:
                #    m=nums[i]
            print("max: "+str(m)+" prev max: "+str(prev_max)+" prev min: "+str(prev_min))
                
            i+=1
        m=max(m,prev_min,prev_max)
        print(m)
            
        #return m
        

s=Solution()

arr=[-2,1,-3,4,-1,2,1,-5,4]
arr=[-2,-1]
arr=[8,-19,5,3,20] #300
s.maxSubArray(arr)
prev = [8,-11,5,3,21]

arr=[2,3,4,-13,8,2,3] # 48
s.maxSubArray(arr)
arr=[-1,-2,-9,-6] # 108
s.maxSubArray(arr)
prev_max = [-1,2,]
#prev_min=[-1,-2,-9,-6] 
arr=[1,-2,3,4,5,3,-4]

s.maxSubArray(arr)

arr=[2,-5,-2,-4,3]
s.maxSubArray(arr)

arr=[-4,-3,-2]
s.maxSubArray(arr)

# find min value , is it previous val or is prev val* current value, 
#prev_pos=-inf
#prev_neg=inf
#if(num[0]<0)
#prev_neg=num[0]
#else:
#prev_pos=num[0]
#prev_pos=
#prev_neg=-6
#arr=[1,-2,3,4,5,3,-4]
#[-2,3,-4]
#prev_pos = [1,-2,3,12,60,180,180]
#prev_neg=[1,-2,-6,-24,-120,-260,1040]
#prev_pos = [-2,3,-4]
#prev_min= [ -2,-6,-6]

#[-2,-6,]
#[-2,-6,24]
#[1,-2,3,4,5,3,-4]
            


