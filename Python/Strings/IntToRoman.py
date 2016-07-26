class Solution(object):
    def __init__(self):
        self.dict={1:'I',4:'IV',5:'V',9:'IX',10:'X',90:'XC',100:'C',40:'XL',50:'L',1000:'M',500:'D'}
        
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result=""

        # if the number corresponds to a romanLetter
        if(num in self.dict.keys()):
            return self.dict[num]
        keys = sorted(list(self.dict.keys()),reverse=True)
        modulo = num
        for key in keys:
            times=modulo//key
            if(times==modulo and key!=1):
                continue
            else:
                for j in range(0,times):
                    result=result+self.dict[key]
            modulo=modulo%key
            if(modulo==0):
                return result
        
                    
                
            
        
        
        
        # we divide the number untill we find smalle
        
        
