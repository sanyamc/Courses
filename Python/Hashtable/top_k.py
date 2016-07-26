class Node(object):
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None


class BST(object):
    def __init__(self):
        self.root=None
        self.nodes=0
    
    def addHelper(self,root,node):
        if root==None:
            root=node            
        elif(node.value<root.value):
            root.left=self.addHelper(root.left,node)
        else:
            root.right=self.addHelper(root.right,node)
        return root


    
    def addItem(self,value):
        newItem=Node(value)
        self.nodes+=1
        if(self.root==None):
            self.root=newItem
            return
        self.addHelper(self.root,newItem)
        

    def PreOrder(self):
        self.PreHelp(self.root)

    def PreHelp(self,root):
        if(root==None):
            return
        self.PreHelp(root.left)
        print(root.value)
        self.PreHelp(root.right)

    def leftMost(self,root):
        curr=root
        while(curr.left):
            curr=curr.left
        return curr

    def rightMost(self,root):
        curr=root
        while(curr.right):
            curr=curr.right
        return curr




class Solution(object):
    def topKFrequent(self,nums,k):
        d={}
        for i in nums:
            if i in d.keys():
                d[i]=d[i]+1
            else:
                d[i]=1
        d=sorted(d, key=d.__getitem__,reverse=True)
        return d[0:k]
        
       
    def topKFrequentOld(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        q=[[]]
        for i in nums:
            q.append([])
            if i in d.keys():
                d[i]=d[i]+1
            else:
                d[i]=1
        for i in d.keys():
            q[d[i]].append(i)
        result=[]
        j=len(q)-1
        n=0
        while(j>=0 and n<k):
            #print(n)
            if(len(q[j])!=0):
                for elem in q[j]:
                    result.append(elem)
                    n+=1
                    if(n>=k):
                        print(result)
                        return
            j-=1
        return result
            
        

s=Solution()
s.topKFrequent([14,1,2,2,3,1],3)