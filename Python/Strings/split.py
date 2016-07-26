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

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length=len(s)
        minCuts=float("inf")
        mins=[0]
        if length<=1:
            return 0
        prevCut=0
        partitionIndex=[]
        for i in range(1,length):
            if self.isPalindrome(s[prevCut:i+1]):
                if prevCut==0:
                    mins.append(0)
                else:
                    mins.append(mins[i-1])
                #partitionIndex.append(partitionIndex[i-1])
                continue
            else:                
                k=i-1
                temp=float("inf")
                #print(mins)
                while(k>=0):
                    if(self.isPalindrome(s[k:i+1])):
                        if(k==0):
                            temp=0
                            prevCut=0
                        elif(temp>(mins[k-1]+1)):
                            if((i==length-1)):
                                print("k: "+str(k)+" temp "+str(temp)+"mins[k-1]: "+str(mins[k-1]+1))
                                print(" mins:" +str(mins))
                            temp=mins[k-1]+1
                            prevCut=k
                        
                    
                       

                    k-=1
             
                if(temp==float("inf")):
                    mins.append(mins[i-1]+1)
                    prevCut=i
                else:
                    if((mins[i-1]+1)>temp):
                        mins.append(temp)
                    else:
                        mins.append(mins[i-1]+1)
                        prevCut=i
                    #mins.append(temp)
                    #mins.append(min(temp,(mins[i-1]+1)))
                    
       
        return mins[len(mins)-1]




        
    #def minCut(self, s):
    #    """
    #    :type s: str
    #    :rtype: int
    #    """
    #    length=len(s)
    #    minCuts=float("inf")
    #    mins=[0]
    #    if length<=1:
    #        return 0
    #    prevCut=0
    #    partitionIndex=[0]
    #    for i in range(1,length):
    #        print(s[prevCut:i+1])
    #        if self.isPalindrome(s[prevCut:i+1]) and prevCut!=i:
    #            mins.append(mins[i-1])
    #            partitionIndex.append(partitionIndex[i-1])
    #            continue
    #        elif self.isPalindrome(s[prevCut:i+1]):
    #            mins.append(mins[i-1]+1)
    #            partitionIndex.append(i)
    #        else:
    #            k=prevCut
    #            temp=float("inf")
    #            #print(s[k:i+1])
    #            while(k>=0):
    #                if(self.isPalindrome(s[k:i+1]) and self.isPalindrome(s[partitionIndex[k-1]:k])):
    #                    #check if its minimum
    #                    if(temp>mins[k] and partitionIndex[k]==k):
    #                        temp=mins[k]
    #                        prevCut=k
    #                    elif (temp>mins[k]):
    #                        temp=mins[k]+1
    #                        prevCut=k
    #                k-=1
    #            #print(k)
    #            #print(temp)
                
    #            if(k==-1 and temp==float("inf")):
    #                prevCut=i
    #                #partitionIndex.append(i)
    #                mins.append(mins[i-1]+1)
    #            else:
    #                mins.append(temp)
    #            partitionIndex.append(prevCut)
    #            #print(partitionIndex)
    #            #print(mins)
    #            #minCuts=min(temp,minCuts)
    #   # print(mins)
    #    return mins[length-1]
                
                
s=Solution()
#print(s.minCut("ccaacabacb"))
test="fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
#print(len(test))
test1="cbfhhg"
test2="efe"
test3="abbab"
test5="adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"
print(s.minCut(test5))
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