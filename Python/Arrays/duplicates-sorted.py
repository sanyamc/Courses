def removeDupes(array):
    i=0
    j=1
    while(j<len(array)):
        #print("i: "+str(i) +"j: "+str(j))
        print("i: "+str(i))
        while(j<len(array) and array[j]==array[i]):
            print("j: "+str(j))
            j+=1
        if j!=i+1 and j<len(array):
            array[i+1]=array[j]
        i=i+1
        j=j+1
    while(i<len(array)):
        array[i]=0
        i+=1

    print(array)

def removeDupes2(array):
    i=0
    j=1
    for i in range(0,len(array)):
        #print("i: "+str(i) +"j: "+str(j))
        if array[j-1]!=array[i]:
            array[j]=array[i]
            j+=1
            
        #j=j+1
    while(j<len(array)):
        array[j]=0
        j+=1

    print(array)

arr = [2,3,4,4,5,6,7,7,7,7,8,9,10]
removeDupes(arr)

