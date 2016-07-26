class Solution(object):
    def isPalindrome(self, s):
        length=len(s)
        #print(s)
        if len(s)==1:
            return True
        for i in range(0,length//2):
            if(s[i]!=s[length-(i+1)]):
                return False
        return True
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        length=len(s)
        if length<1:
            return []
        
        dp=[]
        #print(result)
        for i in range(0,length):
            #newResult=list()
            #for j in range(0,len(result)):
            #   # print(type(result[j]))
            #    if(type(result[j])==list):
            #        #print('here')
            #        result[j].append(s[i])
            k=i
            #print(dp)
            result=[]
            while(k>=0):
                if k==0:
                    if self.isPalindrome(s[k:i+1]):
                        result.append([s[k:i+1]])
                else:
                    
                    if self.isPalindrome(s[k:i+1]):
                        temp=dp[k-1][:]
                        for t in temp:
                            #print(len(temp))
                            val=t[:]
                            val.append(s[k:i+1])
                            result.append(val)
                        #result.append([s[0:k],s[k:i+1]])
                    #if(i==3):
                    #    print(s[k:i+1])
                    #    print(s[0:k])
                    #    print(result)
                k-=1
            dp.append(result)

            
            

        return result


            


s=Solution()
#print(s.minCut("ccaacabacb"))
test="fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
#print(len(test))
test1="cbfhhg"
test2="efe"
test3="abba"
test4="aab"
test5="adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"
print(s.partition(test3))
#print(s.isPalindrome("ccaac"))
#print(s.isPalindrome("aabb"))
#print(s.isPalindrome("abba"))


# ccaacabacb
# partIndex [0, 0,2,2,
# min
#cbfhhg
#c,b,f,hh,g,f,ii,e,c
##c,b,f,hh,g,f,ii,e,c
#min=[0,1]
#part=[0,1,2,3,3,5,6,7,7,8,9]
#fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi