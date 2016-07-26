class Solution(object):
    def nonRepeat(self,s):
        dict={}
        length=len(s)
        mins=length
        for i in range(0,len(s)):
            if(s[i] not in dict):
                dict[s[i]]=1
                if(mins>i):
                    mins=i
            elif(mins!=length and s[mins]==s[i]):
                k=mins+1
                while(k<=i):
                    if(s[k]==1):
                        mins=k
                    k+=1
                if(s[mins]==s[i]):
                    mins=length
            else:
                dict[s[i]]+=1
            
           
            print(mins)
        if(mins==length):
            return None
        else:
            return s[mins]

            



s=Solution()
print(s.nonRepeat("geeksforgeeks"))


 