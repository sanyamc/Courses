"""
Array Pair Sum
Problem
Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)

 """

 ## Solution from instructor, using set
 def pair_sum_master(arr,k):
    
    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()
    
    # For every number in array
    for num in arr:
        
        # Set target difference
        target = k-num
        
        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        
        else:
            # Add a tuple with the corresponding pair
            # adding it in the form minimum then maximum
            output.add( (min(num,target),  max(num,target)) )
    
    
    # FOR TESTING
    return len(output)
    # Nice one-liner for printing output
    #return '\n'.join(map(str,list(output)))


def pair_sum(nums,k):
    table={}
    pairs=[]
    for i in nums:
        temp = k-i
        if temp in table:
            pairs.append((temp,i)) # change it to add in the form min, max
            if( table[temp]==1):
                table.pop(temp)
            else:
                table[temp]-=1
        else:
            table[i]=1
    #print(pairs)
    return len(pairs)

from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
t.test(pair_sum)

#print(pair_sum([1,3,2,2],4))

        