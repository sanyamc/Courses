def removeKey(arr,key):
    writeIndex=0
    for index,val in enumerate(arr):
        if(val!=key):
            arr[writeIndex]=arr[index]
            writeIndex+=1
    #        if(writeIndex==-1):
    #            writeIndex=index
    #i=writeIndex+1
    #while(i<len(arr) and writeIndex!=-1):
    #    if(arr[i]==None):
    #        i+=1
    #        continue
    #    arr[writeIndex]=arr[i]
    #    writeIndex+=1
    #    i+=1
    

    while(writeIndex<len(arr)):
        arr[writeIndex]=None
        writeIndex+=1
    print(arr)


         

arr = [2,3,4,4,5,6,7,7,7,7,8,9,10]
removeKey(arr,7)

