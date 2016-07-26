
def getSq(num):
    l=1
    u=num//2
    output=-1
    while(l<=u):
       # print("l: "+str(l)+" u: "+str(u))
        mid=(u+l)//2
        if(mid*mid < num):
            output=mid
            l=mid+1
        elif(mid*mid==num):
            return mid
        else:
            u=mid-1
    return output

def isPerfect(num):
    val=getSq(num)
    if(val*val == num):
        return (True,num)
    return (False,None)


import math
class Solution(object):
    def __init__(self):
        self.perfect=0
        self.squares=[]
        self.dp=[1]
        self.lastK=1

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #for k in range(len(self.squares),n+1):
        #    self.dp.append(float("inf"))
        #    #(isPer,val)=isPerfect(k)
        #    sq=math.sqrt(k)
        #    if(sq-round(sq)==0):
        #        self.squares.append(k)
        
        k=self.lastK
        
        while(k<=n):
            sq=math.sqrt(k)
            if(round(sq)-sq==0):
                self.dp.append(1)
                k+=1
                continue
            else:
                self.dp.append(k)
            i=1
            #print("k: "+str(k)+ " self.dp[k]: "+str(self.dp[k]))
            while(i<=k):                
                #print("i: "+str(i)+ " self.dp[i]: "+str(self.dp[i]))
                if(self.dp[i]==1):
                    self.dp[k]=min(self.dp[k-i]+1,self.dp[k])

                i+=1
            #print("k: "+str(k)+ " self.dp[k]: "+str(self.dp[k]))
            k+=1
        
            

            
            # go through the squares array and find minimu
            #for i in self.squares:
            #    if(i<k):
            #        self.dp[k]=min(self.dp[k-i]+1,self.dp[k])
            #    elif(i==k):
            #        self.dp[k]=1
            #    else:
            #        break
            ##print("k: "+str(k)+ " self.dp[k]: "+str(self.dp[k]))
            #k+=1
        #print(self.dp)
        self.lastK=k
        return self.dp[n]


            

        

        #self.perfect=float(math.inf)
        #i=0
        #while(i<len(self.squares)):
        #    currMin=0
        #    currVal=n
        #    #j=currVal
        #    squares=self.squares[0:len(self.squares)-i]
        #    j=len(squares)-1
        #    while(currVal>0):
                
        #        #currMin+=1
        #        val=self.squares[j]
        #        #print("currVal: "+str(currVal)+" val: "+str(val))
        #        while(currVal>=val):
        #            currVal=currVal-val
        #            currMin+=1
        #        j-=1
        #    self.perfect=min(self.perfect,currMin)
        #    i+=1
        #return self.perfect

s=Solution()
print(s.numSquares(2))
print(s.numSquares(3))
print(s.numSquares(4))
print(s.numSquares(9))
print(s.numSquares(8))
print(s.numSquares(11))
print(s.numSquares(12))
print(s.numSquares(13))
print(s.numSquares(3102))


        

def compare(l,u,factor):
    if(factor<.001):
        return factor
    newF=factor
    #print("l: "+str(l)+" u: "+str(u)+" factor: "+str(newF))
    while(l+newF>=u or u-newF<l):
        
        newF=newF/10
    return newF

def compare(a,b):
    factor=0.0001
    if(a<b and (b-a)>factor):
        return 1
    if(a>b and (a-b)>factor):
        return -1
    return 0



def getRealSq(num):

    l=0.0
    if(num<1):
        u=1.0
    else:
        u=num
    factor=1
    #print(str(u))
    while(compare(l,u)==1):       
        mid=l+(u-l)/2
        #mid=(u+l)/2
        print("l: "+str(l)+" u: "+str(u)+" mid: "+str(mid))
        #print(str(mid))
        if(compare(mid*mid, num)==1):
           # factor=getNewFactor(mid,u,factor)
            l=mid
        elif(compare(mid*mid,num)==0):
            return round(mid,3)
        else:
           # factor=getNewFactor(l,mid,factor)
            u=mid
    return round(l,3)
    

#print(getRealSq(0.4))
#print(getRealSq(25))
#print(getRealSq(3))
#print(getRealSq(33))
#print(getRealSq(166))


