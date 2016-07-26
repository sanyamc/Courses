class Solution(object):
    def numWays(self,n,k):
        if(n<1 or k<1):
            return 0
        if(n<=2):
            s=1
            for count in range(0,n):
                s=s*k
            return s            
        if(k<2 and n>2):
            return 0   

             
        dp=[k,k*k]

        for i in range(2,n):
            dp.append(dp[i-1]*(k-1)+(dp[i-2]*(k-1)))
        return dp[len(dp)-1]


        

    # def numWays(self, n, k):
    #     """
    #     :type n: int
    #     :type k: int
    #     :rtype: int
    #     """
    #     if(n<1):
    #         return 0
    #     if(k<2 and n>2):
    #         return 0
    #     dp=[k]
    #     temp=0
    #     for i in range(1,n):
    #         if(temp<2):
    #             dp.append(dp[i-1]*(k))
    #             temp+=1
    #         else:
    #             dp.append(dp[i-1]*(k-1))
    #     return dp[n-1]

s=Solution()
print(s.numWays(2,3))
print(s.numWays(3,3)) # 24
print(s.numWays(3,2)) # 6
print(s.numWays(2,2)) # 4 

#2,2,2
'''
R R 
R B
B B
B R
  f(1) = f(0)*k-1 , f(0)*k
  f(2) = f(1)*k, f(1)*k-1
  f(0)=2
  f(1)=2*1,4 (4)
  f(2)=f(1)*1,f(1)*2 (
  f(3)=f(2)*3 (provided temp<2),f(2)*2
N*N
N*N

R B R
B R B

R R B
B B B
B R R
R R R

f(1)=2
f(2)=4,2
f(3)=6,
2,
'''
