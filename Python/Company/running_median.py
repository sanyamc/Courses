#class Node(object):
#    def __init__(self,value=None):
#        self.value=value
#        self.left=None
#        self.right=None


#class BST(object):
#    def __init__(self):
#        self.root=None
#        self.nodes=0
#        self.result=[]
#        self.median=0
    
#    def addHelper(self,root,node):
#        if root==None:
#            root=node            
#        elif(node.value<root.value):
#            root.left=self.addHelper(root.left,node)
#        else:
#            root.right=self.addHelper(root.right,node)
#        return root


    
#    def addItem(self,value):
#        newItem=Node(value)
#        self.nodes+=1
#        if(self.root==None):
#            self.root=newItem
#            return
#        self.addHelper(self.root,newItem)
        

#    def PreOrder(self):
#        self.result=[]
#        return self.PreHelp(self.root)

#    def PreHelp(self,root):
#        if(len(self.result)>(self.nodes/2 +1)):
#            return
#        if(root==None):
#            return
#        self.PreHelp(root.left)
#        self.result.append(root.value)
#        self.PreHelp(root.right)

#    def leftMost(self,root):
#        curr=root
#        while(curr.left):
#            curr=curr.left
#        return curr

#    def rightMost(self,root):
#        curr=root
#        while(curr.right):
#            curr=curr.right
#        return curr

#class MedianFinder:
#    def __init__(self):
#        """
#        Initialize your data structure here.
#        """
#        self.list=[]
#        self.length=0
#        self.tree=BST()

        

#    def addNum(self, num):
#        """
#        Adds a num into the data structure.
#        :type num: int
#        :rtype: void
#        """
#        self.tree.addItem(float(num))
#        #self.list.append(float(num))
#        #self.list=sorted(self.list)
#        #self.length+=1

#    def findMedian(self):
#        """
#        Returns the median of current data stream
#        :rtype: float
#        """
#        length=len(self.tree.result)
#        if(len(self.tree.result)<self.tree.nodes):
#            self.tree.PreOrder()
#        val1=self.tree.result[length-1]
            
#        if(self.tree.nodes==0):
#            return None
#        elif((self.tree.nodes%2==0)):
#            val=val1+self.tree.result[length-2]
#            return val/2
#        else:
#            return val1
#        #if(self.tree.nodes==0):
#        #    return None
#        #elif((self.tree.nodes % 2)==0):
#        #    # get the leftmost in right subtree to avg the values
#        #    second=self.tree.leftMost(self.tree.root.right)

#        #    val=(second.value+self.tree.root.value)/2
#        #    return val
#        #else:
#        #    return self.tree.root.value
        
        

## Your MedianFinder object will be instantiated and called as such:
## mf = MedianFinder()
## mf.addNum(1)
## mf.findMedian()

import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min_heap=[]
        self.max_heap=[]
        self.initial=False
        #self.min_len=0
        #self.max_len=0
        #self.length=0
        #self.tree=BST()

        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        num=float(num)
        if(self.initial==False):
            heapq.heappush(self.max_heap,-num)
            self.initial=True
            return


        if (num<-(self.max_heap[0])):
            heapq.heappush(self.max_heap,-num)
        else:
            heapq.heappush(self.min_heap,num)
            
        min_len=len(self.min_heap)
        max_len=len(self.max_heap)

        # balancing act
        if(max_len-min_len>1):
            #move element from max to min            
            val=-heapq.heappop(self.max_heap)
            #print("removing "+ str(val))
            heapq.heappush(self.min_heap,val)
        elif(min_len-max_len>1):
            val=heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-val)




        #heapq.heappush(self.list,float(num))
        #self.length+=1
        #self.tree.addItem(float(num))
        #self.list.append(float(num))
        #self.list=sorted(self.list)
        #self.length+=1

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        min_len=len(self.min_heap)
        max_len=len(self.max_heap)
        if(min_len==max_len):
            return (-self.max_heap[0]+self.min_heap[0])/2
        elif(min_len>max_len):
            return self.min_heap[0]
        else:
            return -self.max_heap[0]
        #if(self.length==0):
        #    return None
            
        #if(self.length%2 == 0):
        #    val=self.list[self.length//2]+self.list[self.length//2 -1]
        #    return val/2
        #else:
        #    return self.list[self.length//2]
            
        
        
        #if(len(self.tree.result)<self.tree.nodes):
        #    self.tree.PreOrder()
        #length=len(self.tree.result)
        ##val1=
            
        #if(self.tree.nodes==0):
        #    return None
        #elif((self.tree.nodes%2==0)):
        #    val=self.tree.result[length-1]+self.tree.result[length-2]
        #    return val/2
        #else:
        #    return self.tree.result[length-1]
        #if(self.tree.nodes==0):
        #    return None
        #elif((self.tree.nodes % 2)==0):
        #    # get the leftmost in right subtree to avg the values
        #    second=self.tree.leftMost(self.tree.root.right)

        #    val=(second.value+self.tree.root.value)/2
        #    return val
        #else:
        #    return self.tree.root.value
        
        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()