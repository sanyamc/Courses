class Solution(object):

    def maxProfit(arr):

        if(len(arr)<=1):
            return None;
    
        min=[arr[0]]
        for i in range(1,len(arr)):
            #print(min)
            if(min[i-1]>arr[i]):
                min.append(arr[i])
            else:
                min.append(min[i-1])
        max_diff=arr[1]-arr[0]

        for (i,val) in enumerate(arr):
            if(val-min[i]>max_diff):
                max_diff=val-min[i]
        print(max_diff)


    #save min for an index in an array

    #grab the max profit



         

#arr = [2,3,4,4,5,6,7,7,7,7,8,9,10]
arr=[210,2,12,2,13,7,150]
arr=[210,2]

#min=[4]
#4,4,2,2,2

#max_diff=11

maxProfit(arr)

