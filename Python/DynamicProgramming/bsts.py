class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[1,1]
        if(n==2):
            return n
        elif n<2:
            return 1
        for i in range(2,n+1):
            sum=0
            for k in range (1,i+1):
                sum+=dp[k-1]*dp[i-k]
            dp.append(sum)
            #print(dp)
        return dp[len(dp)-1]

s=Solution()
s.numTrees(6)