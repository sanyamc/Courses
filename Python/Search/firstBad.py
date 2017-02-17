# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

"""
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""

"""
- we will test if n is bad or not, if it is then we will check for half its value.
- if half is bad then it lies less than half else it lies between half and n 
- we reduce the space to n/2 and n
"""

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n<=0:
            return 0
        if not isBadVersion(n):
            return None
        l=1
        u=n
        while(l<=u):
            mid = (l+u)//2
            if isBadVersion(mid):
                u=mid-1
            else:
                l=mid+1
        if isBadVersion(l) and l<=n:
            return l
            

