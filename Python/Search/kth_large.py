import math
class Solution(object):
    def getIndexOfMin(self,nums):
        min=float("inf")
        max=-min
        index=-1
        for (i,val) in enumerate(nums):
            if val<min:
                min=val
                index=i
        return index,min

    def getIndexOfMax(self,nums):
        min=float("inf")
        max=-min
        index=-1
        for (i,val) in enumerate(nums):
            if val>max:
                max=val
                index=i
        return index,max

    def shift(self,arr,fro,to):
        temp=arr[to]
        start=fro
        while(fro<=to):
            arr[fro]=arr[fro+1]
            fro+=1
        arr[start]=temp
    
    def findKthLargest(self,nums,k):
        n=len(nums)
        start=0
        end=n-1
        u_count=0
        while(True):
            u_count=0
            pivotIndex=start
           
            while(start<end):
                if nums[start]>nums[pivotIndex]:
                    u_count+=1
                    
                if nums[start]<nums[pivotIndex]:
                    self.shift(nums,pivotIndex,start)
                start+=1
            print("start: "+str(start)+ " end: "+str(end) +" pivot: "+str(nums[pivotIndex]) +"u_count: "+str(u_count))
            if(u_count<(k-1)):
                end=pivotIndex
            if(u_count>(k-1)):
                start=pivotIndex
            if(u_count==k-1):
                return nums[pivotIndex]



            


    def findKthLargestSelection(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # instead of sorting the entire array, we sort only last k elements

        #print(max)
        copy=nums
        last=len(nums)-1
        for i in range(0,k):
            index,max=self.getIndexOfMax(copy[0:last+1])
            # swap with last element
            temp=copy[last]
            copy[last]=max
            last-=1
            copy[index]=temp
        return copy[last+1]
        
    def findKthLargestOld(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # instead of sorting the entire array, we sort only last k elements
        val=sorted(nums,reverse=True)
        return val[k-1]
        min=-float("inf")
        max=-float("inf")
        #print(max)
        copy=nums
        for i in range(0,k):
            index,max=self.getIndexOfMax(copy)
            copy[index]=min
        return max

arr=[-1,2,0]
s=Solution()
s.findKthLargest([3,1,6,98,13],2)

