
'''
Given an array of integers (positive and negative) find the largest continuous sum.
'''




def large_cont_sum(arr): 

    max_sum= -float("Inf")
    current_sum = arr[0]
    for i in range(1,len(arr)):
        val=arr[i]
        current_sum=max(current_sum+val,val)
        max_sum=max(max_sum,current_sum)

    print(max_sum)
    return max_sum
    pass

from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print('ALL TEST CASES PASSED')
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)