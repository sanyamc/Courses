"""
find square root of a given number, can return integer
"""
# this is not really bst as we are not checking mid value for condition but instead i, check mid value for condition like below
def int_sqRoot(num):

    end=num
    start=1
    output=None
    while(start<=end):
        i=start        
        mid=start+(end-start)//2
        val=i*i
        print("start: "+str(start)+" end: "+str(end))
        if(val==num):
            return i
        if(val<num):
            start=mid            
        elif(val>num):
            end=mid
            start=start//2
    return start-1

def getSq(num):
    l=1
    u=num//2
    output=-1
    while(l<=u):
        print("l: "+str(l)+" u: "+str(u))
        mid=(u+l)//2
        if(mid*mid < num):
            output=mid
            l=mid+1
        elif(mid*mid==num):
            return mid
        else:
            u=mid-1
    return output


print("value is: "+str(int_sqRoot(256)))

#print("value is: "+str(getSq(256)))




