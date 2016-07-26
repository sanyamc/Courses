
def swap(array,i,j):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp

def DNF(array,index):
    part = array[index];
    pivot=index

    length=len(array)
   
    smallIndex=-1
    bigIndex=-1

    for counter in range(length):
         i=counter
         #j=length-1
         while(i <length):
            if(array[i]>=array[pivot]):
                swap(array,i,pivot)
                i+=1
    

    print(array)