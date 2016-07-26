"""
This file is mainly a review of implementing graph data structure.
For most scenarios i will be using some inbuilt graph structure to solve problems or use this module.
Below graph has following methods added for learning purposes:

Unidirected vs directed
In python we represent unidirected graph by having an edge for both the nodes to each other while directed will just have one edge.

- Initialization with empty dict or with a dictionary
- Insert Vertex/Node method
- Add edge between two nodes
- Compute path, allpaths and shortest path between two nodes/vertex
- Nodes, to return all nodes of a graph
- Edges, to return all edges of a graph

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

    #def insert(self,from,value):
        # search for from node in the graph and then add value to iter


    def searchPath(self,graph,start,to,path=[]):
        # returns a path between the two nodes
        # does a dfs
        # from, to is string(key)
        #path.append(from)................... not good as this function is recursive and we are modifying the original variable in caller
        path=path+[start] # creates a new list by same name as path instead of appending to original
        if start==end:
            return path
        
        if start not in graph:
            return None
        else:
            for node in graph[start]:                            
                if node not in path:
                    val=self.searchPath(self,graph,node,to,path)       # to take care of already covered nodes/cycles using this if so have an if which searches
                    if(val):
                        return val


    def searchAllPaths(self,graph,start,to,path=[]):
        """
        Returns all paths between 2 nodes, simple variant of above
        rtype:list[list[nodes]]
        """
        path=path+[start] # creates a new list by same name as path instead of appending to original
        if start==end:
            return [path]
        paths=[]
        if start not in graph:
            return None
        else:
            for node in graph[start]:                            
                if node not in path:
                    val=self.searchPath(self,graph,node,to,path)       # to take care of already covered nodes/cycles using this if so have an if which searches
                    if(val):
                        paths=paths+val        
        return paths

    def searchShortestPath(self,graph,start,to,path=[]):
        """
        Returns shortest path between 2 nodes, simple variant of above
        rtype:list[list[nodes]]
        """
        path=path+[start] # creates a new list by same name as path instead of appending to original
        if start==end:
            return path
        shortest=[]
        if start not in graph:
            return None
        else:
            for node in graph[start]:                            
                if node not in path:# to take care of already covered nodes/cycles using this if so have an if which searches
                    val=self.searchPath(self,graph,node,to,path)       
                    if(len(shortest)>0 and len(val)<len(shortest)):
                        shortest=val
                    elif(len(shortest)==0:
                        shortest=val
        return shortest






def testList(nums):
    nums=nums+[2]#nums.append(2)
    #return nums

nums=[1]
testList(nums)
print(nums)




    
        