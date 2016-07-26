"""Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""

from tries import Trie
import pprint
pp=pprint.PrettyPrinter(indent=6)
print=pp.pprint



class Solution:
    def __init__(self):
        self.indices=[]
        self.trie=Trie()

    def isPalindrom(self,str):
        i=0
        j=len(str)-1
        if(len(str)==0):
            return False
        for i in range(0,len(str)//2):
            if(str[i]!=str[j]):
                return False
            j-=1
        return True
    
    def palindromPairsSlow(self,words):

        i=0
        length=len(words)
        for i in range(0,length):
            for j in range(0,length):
                if(i==j):
                    continue
                else:
                    if(self.isPalindrom(words[i]+words[j])):
                        self.indices.append([i,j])
        return self.indices
    
    # def palindromPairs(self,words):
    #     i=0
    #     length=len(words)
    #     if(length==0):
    #         return self.indices
    #     table={}
    #     for index,word in enumerate(words):
    #         table[word]=index
    #     for index,word in enumerate(words):
    #     return self.indices

    def palindromePairsTrie(self,words):
        i=0
        length=len(words)
        if(length==0):
            return self.indices
               
        for index,word in enumerate(words):
            self.trie.insertP(word,index)
        print(self.trie.root)

        # for word in words:
        #     self.trie.search(word[::-1])

                


s=Solution()
words=["bat", "tab", "cat"]
words=["abcd", "dcba", "lls", "s", "sssll"]

t=Trie()
[t.insertP(word,index) for index,word in enumerate(words)]
#print(t.root)
print(t.allWordsWithPrefix("s"))

#s.palindromePairs(words)
#print([words[i]+words[j] for i,j in s.palindromePairs(words)])









