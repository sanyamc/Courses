

def maxProfit(arr):
    if(len(arr)<=1):
        return None;
    #max_val=max(arr[0],arr[1])
    min_val=arr[0]
    #dp[0]=-float("inf")
  
    dp=[-float("inf")]#,max_val-min_val]
    prev_val=0
    for i in range(1,len(arr)):

        if arr[i] < min_val:
            prev_val=min_val
            min_val = arr[i]
        else:
            prev_val=min_val
            #max_val=arr[i]
        dp.append(max(dp[i - 1],arr[i] - min_val))
       # print(dp)
    return dp[len(dp)-1]
    



        

       

class Solution(object):

    def maxProfit(arr):

        

        if(len(arr)<=1):
            return 0;

        max_val=max(arr[0],arr[1])
        min_val=float("inf")
        dp[0]=-float("inf")
        #dp[1]=-float("inf")

        for i in range(1,len(arr)):
            if i>max_val:
                max_val=i
                min_val=i
            elif i<min_val:
                min_val=i
            print(dp)
            dp.append(max(dp[i-1],i-min_val))
        

    
        #min=[arr[0]]
        #for i in range(1,len(arr)):
        #    #print(min)
        #    if(min[i-1]>arr[i]):
        #        min.append(arr[i])
        #    else:
        #        min.append(min[i-1])
        #max_diff=arr[1]-arr[0]

        #for (i,val) in enumerate(arr):
        #    if(val-min[i]>max_diff):
        #        max_diff=val-min[i]
        #print(max_diff)


    #save min for an index in an array

    #grab the max profit



         

arr = [2,3,4,4,5,6,7,7,7,7,8,9,10] #8
print(maxProfit(arr))
arr=[1,2,210,2,12,2,13,7,150] #209
print(maxProfit(arr))
arr=[210,2] # -208
print(maxProfit(arr))

#min=[4]
#4,4,2,2,2
arr=[3,2,6,5,0,3] # 4
arr=[1,2]
#max_diff=11

print(maxProfit(arr))

