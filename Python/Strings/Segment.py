class Solution(object):
    def addIndex(self,min,max):
        for i in range(min,max):
            if(i in self.index.keys()):
                continue
            else:
                self.index[i]=1

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        self.index={}
       # keys=wordDict.keys()
        m=len(s)
        if(m==1):
            return (s[0] in wordDict)
        dp_sub=[0]
        dp_sta=[0]
        prev_index=0
        cur=[0]
        if(s[0] in wordDict):
            dp_sub[0]=1
            dp_sta[0]=1

        cur[0] = dp_sub[0] or dp_sta[0]

        for i in range(1,m):
            dp_sub.append(0)
            dp_sta.append(0)
         
            if(s[i] in wordDict):
                dp_sta[i]=dp_sub[i-1] or dp_sta[i-1]
            else:
                dp_sta[i]=0                
            if(s[prev_index:i+1] in wordDict):
                dp_sub[i]=1
                prev_index=i+1
            else:# check if it is part of any other previous
                
                k=i-1
                while(k>=0):
                    if(k==0):
                        val=1
                    else:
                        val=cur[k-1]
                        
                    #print(s[k:i+1])
                   # print(val)
                   # print(cur[k-1])
                  #  print(dp_sta[k-1] or dp_sub[k-1])
                   # print(cur[k-1])
                    if(s[k:i+1] in wordDict and val==1):
                        prev_index=i+1
                        dp_sub[i]=1
                        
                        break
                    k-=1
            #print(cur)
            #print(dp_sta)
            #print(dp_sub)

            
            cur.append(dp_sub[i] or dp_sta[i])
        return cur[m-1]==1

   
        

       
            
           
            
s=Solution()
print(s.wordBreak("aaaaaaa",set(("aaaa","aa"))))
print(s.wordBreak("aaaaaa",set(("aaaa","aa"))))
print(s.wordBreak("apple",set(("apple","peach"))))
print(s.wordBreak("abcd",set(("a","abc","cd","b"))))
print(s.wordBreak("goalspecial",set(("go","goal","goals","special"))))
