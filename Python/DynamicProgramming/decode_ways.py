class Solution(object):
    def canBeTogether(self,num):
        if(num[0]=='0'):
            return False
        val=int(num)
        if(val>0 and val<27):
            return True
        return False

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        prev=0
        prev_p=0
        
        s_len=len(s)
        if(s_len<1):
            return 0
        #if(s_len<2):
        #    return 1
        if(self.canBeTogether(s[0]))==True:
            #dp.append(1)
            prev=1
            prev_p=1
        else:
            prev=0
            prev_p=0
            #dp.append(0)
        #if(self.canBeTogether(s[0:2]))==True:
        #    dp.append(2)
        #else:
        #    dp.append(1)
        curr=prev
        for i in range(1,len(s)):
            val=0            
            if self.canBeTogether(s[i-1:i+1])==True:
                val+=prev_p
                #if(len(dp)<2):
                #    val+=dp[0]
                #else:
                #    val+=dp[len(dp)-2]
            if(self.canBeTogether(s[i])):
                val+=prev
               # val+=dp[len(dp)-1]# if dp[len(dp)-1]>0 else 1)
            #print(s[i-1:i+1]+": "+str(val))
            #print(s[i])
            curr=val
            prev_p=prev
            prev=curr
        #print(curr)
        return curr        

s=Solution()
#print(s.numDecodings('1'))
print(s.numDecodings('101'))
print(s.numDecodings('121'))
print(s.numDecodings('1001'))
print(s.numDecodings('11'))



