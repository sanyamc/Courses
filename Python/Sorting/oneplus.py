class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=len(digits)-1
        while(i>=0):
            val=digits[i]+1
            if(val%10==val):
                digits[i]=val
                return digits
            elif(i==0 and digits[i]==9):
                digits[i]=1
                digits.append(0)
                return digits
            else:
                digits[i]=0
            i-=1
        
        
s=Solution()
print(s.plusOne([9,9,9]))