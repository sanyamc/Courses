class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        j=1
        n=len(nums)
        if(n==0):
            return 0
        i=0
        start_index=0
        end_index=n
        sum=nums[i]
        while(j<n):
            #sum=sum+nums[i]
            #print("sum: "+str(sum))
            while(sum<s and j<n):                
                sum=sum+nums[j]
                j+=1
          
            j-=1
            #print(sum)
            #print(nums[i:j+1])
            #print("st: "+str(start_index)+" ed: "+str(end_index))
            #print("i: "+str(i)+" j: "+str(j))

           
            if (sum>=s and end_index-start_index>(j-i)):
                start_index=i
                end_index=j
            sum=sum-nums[i]
            i+=1
            while(sum>=s and i<=j):
                val=sum-nums[i]
                if(val>=s):
                    sum=val
                else:
                    #i-=1
                    break
                i+=1
            #i-=1
            

            
            if(i>j):                
                j+=1
                sum=sum+nums[j]
            
                #i-=1
            #if(i>j):
            #    i=j
            if (sum>=s and (end_index-start_index>(j-i))):
                start_index=i
                end_index=j
            #print(sum)
            #print(nums[i:j+1])
            #print("st: "+str(start_index)+" ed: "+str(end_index))
            #print("i: "+str(i)+" j: "+str(j))
            #print(nums[start_index:end_index])
            #i+=1
            j+=1

        if(end_index<=n):
            val=0
            for i in nums[start_index:(end_index+1)]:
                val+=i
            if(val<s):
                return 0
            return len(nums[start_index:(end_index+1)])


s=Solution()
print(s.minSubArrayLen(7,[2,3,1,2,4,3]))
print(s.minSubArrayLen(100,[]))
            
        