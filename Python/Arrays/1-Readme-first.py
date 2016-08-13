""" 
- python has a deep copy function in copy module
- list has extend method which adds elements to end of another list, but they are really references

- there is a sys module which has a method getSizeOf which returns size in bytes

"""

# lets try out the above statements

def extendExample(nums):
    '''

    '''
    result=['a','b','c']
    nums.extend(result)
    return nums

# nums=[1,2,3]
# nums=extendExample([1,2,3])
# print(nums)


def testSizeInBytes():
    nums=[]

    import sys
    print(str(sys.getsizeof(nums))+" bytes")
    print(str(sys.getsizeof([1]))+" bytes")
    print(str(sys.getsizeof([1,2,3]))+" bytes")

testSizeInBytes()