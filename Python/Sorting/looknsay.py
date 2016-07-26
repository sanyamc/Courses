class Solution(object):
    def getNumber(self,val):
        temp=""
        count=1
        #    print(val)
        prev=val[0]
        for j in range(1,len(val)):
            if val[j]==prev:
                count+=1
            else:
                temp+=str(count)+str(prev)
                count=1
                prev=val[j]
        #if(temp==""):
        #    temp+=str(count)+str(prev)
        #elif(prev==val[-1]):
        temp+=str(count)+str(prev)


        return temp


    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==0:
            return None
        if n==1:
            return "1"
        val="1"
        for i in range(1,n):
            val=self.getNumber(val)
            #print(val)
        return val

s=Solution()
s.countAndSay(7)
                

