"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(type(nums)!=list):
            return None
        length=len(nums)
        if(length==0):
            return None
        table={}
        max_length=0
        for i in nums:
            
            if i in table:
                continue
            if (i-1) in table and (i+1) in table:
                val=table[i-1].union(table[i+1])
                val.add(i)
                table[i]=val
            else:
                if i-1 in table:
                    val=table[i-1]
                    val.add(i)
                    table[i]=val
                if i+1 in table:
                    val=table[i+1]
                    val.add(i)
                    if i in table:
                        val=val.union(table[i])
                    table[i]=val
                if i not in table:
                    val=set()
                    val.add(i)
                    table[i]=val
            print(table)
        for k in table.keys():
            max_length=max(max_length,len(table[k]))
        return max_length


s=Solution()
print(s.longestConsecutive([0,-1]))
print(s.longestConsecutive([1,3,5,2,4]))

