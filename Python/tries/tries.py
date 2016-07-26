
"""
concept is pretty simple, create a dictionary at every level
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
    
    def insertP(self, word,index):
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
        curr["_end_"]=(word,index)        

    def allWordsWithPrefix(self,prefix):
        """
        Returns all the words with a given prefix
        does a BFS and returns words of increasing length
        """

        curr=self.root
        for letter in prefix:
            if(letter in curr):
                curr=curr[letter]
        words=[]
        queue=[{key:curr[key]} for key in curr.keys()]
        while(len(queue)>0):
            #print(queue)
            node=queue.pop(0)
            if("_end_" in node):
                words.append(node["_end_"])
            else:
                newQ=[node[key] for key in node.keys()]
                queue=queue+newQ
            
        return words
                    

        




       

        

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
    def search(self,expr):
        curr=self.root
        for letter in expr:            
            if letter==".":
                res={}
                for key in curr.keys():
                    res.update(curr[key])
                curr=res                
            elif letter in curr.keys():
                curr=curr[letter]
            else:
                return False
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("pad")
# trie.insert("bad")
# addWord("ran"),addWord("rune"),addWord("runner"),addWord("runs"),addWord("add"),addWord("adds"),addWord("adder"),addWord("addee"),search("r.n"),search("ru.n.e"),search("add"),search("add."),search("adde."),search(".an."),search("...s"),search("....e."),search("......."),search("..n.r")
# print(trie.search(".ad"))
# print(trie.search("pad"))
# print(trie.search("bad"))
# print(trie.search("..."))
# print(trie.search("b.ding"))
#print(trie.root)

"""print(trie.search("key"))
print(trie.search("so"))
print(trie.startsWith("soms"))
print(trie.startsWith("some"))
print(trie.startsWith("somestring"))

 f={'a':{'b':{'c':1},'d':{'e':0}}}
 res={}
 for key in f.keys():
     res[key]=f[key]
"""
