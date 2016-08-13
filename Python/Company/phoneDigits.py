"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
"""

class Solution(object):
    def __init__(self):
        
        self.dl={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
            '0':[''],
            '1':['']
        }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits)==0:
            return []
        elif len(digits)==1:
            return self.dl[digits]
        else:
            return [a+b for a in self.dl[digits[0]] for b in self.letterCombinations(digits[1:])]


s=Solution()
digits='2034'
print(s.letterCombinations(digits))

