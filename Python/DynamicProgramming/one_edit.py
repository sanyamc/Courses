class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len=len(s)
        t_len=len(t)
        edit=0
        
        if(abs(s_len-t_len)>1):
            return False
        if(abs(s_len-t_len)==1):
            temp=s if s_len>t_len else t
            small=s if s_len<t_len else t
            for i in range(len(small)):
                if(small[i]==temp[i] or small[i]==temp[i+1]):
                    continue
                else:
                    return False;
            return True 
        
        for i in range(len(s)):
            if(edit>1):
                return False
            if(s[i]!=t[i]):
                edit+=1
        if(edit==1):
            return True
        return False

s=Solution()
print(s.isOneEditDistance("dab","cab"))

