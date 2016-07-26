class Solution(object):
    def getPermutation(self, n, kth):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        dp=[[],["1"]]
        if(n<2):
            return dp[n][0]
        for i in range(2,n+1):
            result=[]
            #print(i)
            for k in range(1,i+1):
                temp=dp[i-1]
                if(i!=k):
                    temp=[x.replace(str(k),str(i)) for x in temp]
                for j in temp:
                    result.append(str(k)+j)
                if(i==n and kth<=len(result)):
                    return sorted(result)[kth-1]
            dp.append(sorted(result))
            
        
        #print(len(dp[len(dp)-1]))

s=Solution()
print(s.getPermutation(5,3))

            
