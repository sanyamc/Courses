"""Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9

12 , 8,11,3

0 1 2 3 4 5 6 7 8 9
1 1 2 3 4 5 6 7 8 9
4       1 2 3 4 
9
16



"""


class Solution():
    def numSquares(self,n):
        steps={0:0}
        squares=[]
        for current in range(1,n+1):
            squares.append(current*current)
            if(current in squares):
                steps[current]=1                
            else:
                val=float("inf")
                for j in squares:
                    if(j>current):
                        break
                    else:
                        if(current-j in steps):
                            val=min(val,steps[current-j]+1)
                steps[current]=val
        #print(steps)
        return steps[n]

s=Solution()
print(s.numSquares(7217))




    
