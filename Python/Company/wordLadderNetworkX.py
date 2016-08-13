


class Solution(object):
    # do below with levenstien distance
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len=len(s)
        t_len=len(t)
        edit=0
        
        if(abs(s_len-t_len)>1):
            return False
        if(abs(s_len-t_len)==1):
            temp=s if s_len>t_len else t
            small=s if s_len<t_len else t
            for i in range(len(small)):
                if(small[i]==temp[i] or small[i]==temp[i+1]):
                    continue
                else:
                    return False;
            return True 
        
        for i in range(len(s)):
            if(edit>1):
                return False
            if(s[i]!=t[i]):
                edit+=1
        if(edit==1):
            return True
        return False
               
            

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """

        # create a graph data structure with beginWord and endWord and find shortest route between beginWord and secondWord
        graph = Graph()
        toReturn=[]
        if beginWord==endWord:
            return toReturn
        if self.isOneEditDistance(beginWord,endWord):
            return [[beginWord,endWord]
        
        graph.insertNode(beginWord)
        graph.insertNode(endWord)
        l = list(wordList)
        l.append(beginWord)
        l.append(endWord)
        
        #print(l)
        for word in l:
            for anotherWord in l:
                if word==anotherWord:
                    continue
                elif self.isOneEditDistance(word,anotherWord):
                    graph.insertNode(word)
                    graph.insertNode(anotherWord)
                    graph.insertEdge((word,anotherWord))
        #print(graph.root)      

        #print(all)  
        shortest=graph.searchShortestPath(graph.root,beginWord,endWord)
        #print(shortest)
        if shortest:
            all = graph.searchAllPaths(graph.root,beginWord,endWord)
            #print(all)
            
            for path in all:
                if len(path)==len(shortest):
                    toReturn.append(path)
            
        return toReturn
        # return 0
        #print(shortest)
        #return len(shortest)
        pass

s=Solution()
print(s.ladderLength("sanyam","sany",set({"sanya"})))
print(s.ladderLength("c","bc",set({"a"})))
print(s.ladderLength("hit","cog",set({"hot","cog","dot","dog","hit","lot","log"})))