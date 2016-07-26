
def getSq(num):
    l=1
    u=num//2
    output=-1
    while(l<=u):
       # print("l: "+str(l)+" u: "+str(u))
        mid=(u+l)//2
        if(mid*mid < num):
            output=mid
            l=mid+1
        elif(mid*mid==num):
            return mid
        else:
            u=mid-1
    return output

def compare(l,u,factor):
    if(factor<.001):
        return factor
    newF=factor
    #print("l: "+str(l)+" u: "+str(u)+" factor: "+str(newF))
    while(l+newF>=u or u-newF<l):
        
        newF=newF/10
    return newF

def compare(a,b):
    factor=0.0001
    if(a<b and (b-a)>factor):
        return 1
    if(a>b and (a-b)>factor):
        return -1
    return 0



def getRealSq(num):

    l=0.0
    if(num<1):
        u=1.0
    else:
        u=num
    factor=1
    #print(str(u))
    while(compare(l,u)==1):       
        mid=l+(u-l)/2
        #mid=(u+l)/2
        print("l: "+str(l)+" u: "+str(u)+" mid: "+str(mid))
        #print(str(mid))
        if(compare(mid*mid, num)==1):
           # factor=getNewFactor(mid,u,factor)
            l=mid
        elif(compare(mid*mid,num)==0):
            return round(mid,3)
        else:
           # factor=getNewFactor(l,mid,factor)
            u=mid
    return round(l,3)
    

print(getRealSq(0.4))
#print(getRealSq(25))
#print(getRealSq(3))
#print(getRealSq(33))
#print(getRealSq(166))


