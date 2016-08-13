"""Given two strings, check to see if they are anagrams. 
An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

For example:

"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"
"""

"""
 One solution is to use some form of dictionary with frequency and from second array we reduce the frequency untill it reaches 0
 finally either we check for dictionary for 
"""

def anagram(s1,s2):
    table={}

    for i in s1:
        if(i!=" "):
            if i in table:
                table[i]= table[i]+1
            else:
                table[i]=1

    for i in s2:
        if i==" ":
            continue
        if i in table:
            table[i]= table[i]-1
        else:
            return False

    for i in table:
        if table[i]!=0:
            return False
    return True

from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        assert_equal(sol('dog','god'),True)
        assert_equal(sol('clint eastwood','old west action'),True)
        print("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagram)
