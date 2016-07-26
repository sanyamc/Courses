import pprint
pp=pprint.PrettyPrinter(indent=6)
print=pp.pprint

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
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
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        curr=self.root
        #print(self.root)
        for index,letter in enumerate(word):
            print(curr)
            if letter==".":
                newKeys={}
                c=0
                for key in curr.keys():
                    for child in curr[key]:
                        if child in newKeys.keys():
                            print(child + ' already exists')
                            newKeys[child].update(curr[key][child])
                            c=1
                    if c==0:
                        newKeys.update(curr[key])
                    c=0
                    #if type(curr[key])==dict:
                        
                        #print(newKeys)
                   # elif(index==len(word)-1 and len(curr.keys())>1):
                   #      newKeys["_end_"]=True
                curr=newKeys                
            elif letter in curr.keys():
                #print(curr)
                curr=curr[letter]
            else:
                print(letter)
                return False
        #print(curr)
        if "_end_" in curr.keys():
            return True
        
        return False



        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
        

# Your Trie object will be instantiated and called as such:
trie = WordDictionary()
"""trie.addWord("a")
trie.addWord("a")
trie.addWord("bad")
trie.addWord("dad")
trie.addWord("mad")
"""
trie.addWord("ran")
trie.addWord("rune")
trie.addWord("runner")
trie.addWord("add")
trie.addWord("adds")
trie.addWord("adder")
trie.addWord("addee")
trie.addWord("runs")

#print(trie.root)
print(trie.search("r.n"))
"""print(trie.root)
print(trie.search("ru.n.e"))
print(trie.root)
print(trie.search("add"))
print(trie.search("add."))
print(trie.search("adde."))
print(trie.search(".an."))
print(trie.search("....e."))
print(trie.search("......."))
print(trie.search("..n.r"))
print(trie.search("ru.n.e"))
print(trie.search("ru.n.e"))
print(trie.search("ru.n.e"))
#print(trie.search("ba."))
#print(trie.search("s..e"))
#print(trie.startsWith("soms"))
#print(trie.startsWith("some"))
#print(trie.startsWith("somestring"))
"""
