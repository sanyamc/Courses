"""Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation 
sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Actually lets do it with the graphs and find shortest path

"""
class Node(object):
    def __init__(self,value):
        self.value=value

class Graph(object):
    """
    In Graph theory following are interchangable:
    vertex=Node
    edge is a tuple of two nodes and path is composed of edges
    """
    def __init__(self):
        self.root={}

    def insertNode(self,node):
        # search for from node in the graph and then add value to iter
         if node not in self.root:
             self.root[node]=[]

    def insertEdge(self,edge):
        # an edge is a tuple of two nodes
        if edge[0] and edge[1] in self.root:
            if(edge[1] not in self.root[edge[0]]):
                self.root[edge[0]].append(edge[1])
            if(edge[0] not in self.root[edge[1]]):
                self.root[edge[1]].append(edge[0])
            
        

    


    def searchPath(self,graph,start,to,path=[]):
        # returns a path between the two nodes
        # does a dfs
        # from, to is string(key)
        #path.append(from)................... not good as this function is recursive and we are modifying the original variable in caller
        path=path+[start] # creates a new list by same name as path instead of appending to original
        if start==to:
            return path
        
        if start not in graph:
            return None
        else:
            for node in graph[start]:                            
                if node not in path:
                    val=self.searchPath(graph,node,to,path)       # to take care of already covered nodes/cycles using this if so have an if which searches
                    if(val):
                        return val


    def searchAllPaths(self,graph,start,to,path=[]):
        """
        Returns all paths between 2 nodes, simple variant of above
        rtype:list[list[nodes]]
        """
        path=path+[start] # creates a new list by same name as path instead of appending to original
        if start==to:
            return [path]
        paths=[]
        if start not in graph:
            return None
        else:
            for node in graph[start]:                            
                if node not in path:
                    val=self.searchAllPaths(graph,node,to,path)       # to take care of already covered nodes/cycles using this if so have an if which searches
                    if(val):
                        paths=paths+val        
        return paths

    def searchShortestPath(self,graph,start,to,path=[]):
        """
        Returns shortest path between 2 nodes, simple variant of above
        rtype:list[list[nodes]]
        """
        path=path+[start] # creates a new list by same name as path instead of appending to original
        if start==to:
            return path
        shortest=None
        if start not in graph:
            return None
        else:
            for node in graph[start]:                            
                if node not in path:
                    #print(path)# to take care of already covered nodes/cycles using this if so have an if which searches

                    val=self.searchShortestPath(graph,node,to,path)   
                    if val:
                        if((shortest==None)):
                            shortest=val
                        elif(len(val)<len(shortest)):
                            shortest=val
        return shortest
# a function to return how many transformation needed between two words

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
