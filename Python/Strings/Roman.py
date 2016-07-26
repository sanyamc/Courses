def getLiteralValue(romanLetter):
    dict={'I':1,'V':5,'X':10,'C':100,'L':50,'M':1000,'D':500}
    return dict[romanLetter]

def getValue(prev,curr,preceded):
     #print('prev: '+prev+' curr:'+curr)
     prev_val=getLiteralValue(prev)
     curr_val=getLiteralValue(curr)
     if curr_val>prev_val and preceded==False:
         if curr_val==prev_val*5 or curr_val==prev_val*10:
             return (curr_val-prev_val,True)
         else:
             return (-1,preceded)
     elif curr_val>prev_val and preceded==True:
         return (-1,preceded)
     else:
         return (prev_val,False)
     


def isValid(roman):
    roman_list=list(roman)
    result=0
    preceded=False
    if len(roman_list) >0:
        prev=roman_list[0]
        curr=roman_list[0]
        i=1
        while(i<len(roman_list)):
            #print('i: '+str(i) +' result: '+str(result)+' preceded: '+str(preceded))
            prev=roman_list[i-1]
            curr=roman_list[i]
            val,preceded=getValue(prev,curr,preceded)

            if(val!=-1):
                result+=val
            else:
                return None
            if(preceded):
                #print('i: '+str(i))
                i+=1
                #print('i: '+str(i))
            i+=1
            
        print('i: '+str(i)+' length: '+str(len(roman_list)))
        if(preceded==False):
            val,preceded=getValue(prev,curr,preceded)
            if(val!=-1):
                result+=val                
            else:
                return None
        return result

print(isValid('IV'))
print(isValid('V'))
print(isValid('IX'))
print(isValid('X'))
print(isValid('XII'))
print(isValid('XVII'))
print(isValid('IXII'))
print(isValid('XXXXXIIIIIIIII'))
print(isValid('LVIIII'))
print(isValid('LIX'))
print(isValid('CDM'))




