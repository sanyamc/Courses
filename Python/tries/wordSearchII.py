"""Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
"""



class Trie(object):

    def __init__(self):
        self.root = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr=self.root
        for letter in word:
            if(letter not in curr.keys()):
                curr[letter]={}
            curr=curr[letter]
        curr["_end_"]=True
       

        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr=self.root
        for letter in word:
            if(letter in curr):
                curr=curr[letter]
            else:
                return False
        if "_end_" in curr:
            return True
        return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr=self.root
        for letter in prefix:
            if(letter in curr):
                curr=curr[letter]
            else:
                return False
        return True



class Solution:
    def __init__(self):
        self.trie=Trie()
        self.resultSet=set()

    def checkWords(self,trie,neighbours,word,covered):
        #print(neighbours)
        for x,y in neighbours:
            #print('checkWords')
            i = self.board[x][y]
            if i in trie.keys():
                if("_end_" in trie[i].keys()):
                    #print("adding "+i)
                    self.resultSet.add(word+i)
                covered.append((x,y))
                new_neighbours=self.getNeighbours(self.board,x,y,covered)
                self.checkWords(trie[i],new_neighbours,word+i,covered)                     
        #print(self.resultSet)


    def getNeighbours(self,board,x,y,covered=[]):
        neighbours=[]
        if(len(board)==0):
            return neighbours
        y_len=len(board[x])
        x_len=len(board)
        
        if(x-1 >=0):
            if((x-1,y) not in covered):
                neighbours.append((x-1,y))
            # if(y+1<y_len):
            #     if((x-1,y+1) not in covered):
            #         neighbours.append((x-1,y+1))
            # if(y-1>=0):
            #     if((x-1,y-1) not in covered):
            #         neighbours.append((x-1,y-1))
        if(x+1 < x_len):
            if((x+1,y) not in covered):
                neighbours.append((x+1,y))
            # if(y+1<y_len):
            #     if((x+1,y+1) not in covered):
            #         neighbours.append((x+1,y+1))
            # if(y-1>=0):
            #     if((x+1,y-1) not in covered):
            #         neighbours.append((x+1,y-1))
        if(y-1>=0):
            if((x,y-1) not in covered):
                neighbours.append((x,y-1))
        if(y+1<y_len):
            if((x,y+1) not in covered):
                neighbours.append((x,y+1))
        return neighbours

    def findWords(self, board, words):
        self.board=board
        for word in words:
            self.trie.insert(word)
        print(self.trie.root)
               
        for i,val1 in enumerate(board):            
            for j,val2 in enumerate(board[i]):
                letter = board[i][j]
                covered=[(i,j)]
                #print(letter)
                if letter in self.trie.root.keys():
                    if("_end_" in self.trie.root[letter].keys()):                        
                        self.resultSet.add(letter)
                    neighbours=self.getNeighbours(board,i,j)
                    #print(neighbours)
                    
                    #print([self.board[x][y] for x,y in neighbours])
                    self.checkWords(self.trie.root[letter],neighbours,letter,covered)
        return list(self.resultSet)
                
   
        

            




b=[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words=["oath","pea","eat","rain"] 

a=["baabab","abaaaa","abaaab","ababba","aabbab","aabbba","aabaab"]
b=[list(val) for val in a]
print(b)
words=["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]

words=["aabbbbabbaababaaaabababbaaba"]
# b=[
#   ['b','a','a','b','a','b'],
#   ['b','a','a','b','a','b'],
#   ['b','a','a','b','a','b'],
#   ['b','a','a','b','a','b'],
#   ['b','a','a','b','a','b'],
#   ['b','a','a','b','a','b']
# ]
# b=[
#     ["a","b"],
#     ["c","d"]
# ]
# words=["abcd"]
s=Solution()
print(s.findWords(b,words))
#print([b[x][y] for x,y in s.getNeighbours(b,1,3)])

"""
["baabab","abaaaa","abaaab","ababba","aabbab","aabbba","aabaab"]
["aabbbbabbaababaaaabababbaaba","abaabbbaaaaababbbaaaaabbbaab","ababaababaaabbabbaabbaabbaba"]

["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]
"""


