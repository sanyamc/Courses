# class Solution:
#     # @param A : integer
#     # @return a list of strings
#     def __init__(self):
#         self.result=[]

#     def permute(self,A,soFar, open):
#         if len(soFar) == A:
#             if open==0:
#                 self.result.append(soFar)
#             return
        
#         if open>A:
#             return
#         if open<=A:
#             self.permute(A,soFar+'(', open+1)
#         if open>0:
#             self.permute(A,soFar+')',open-1)       
#         # for i in range(0,A):
#             #soFar+='('

            
    
#     def generateParenthesis(self, A):
#         self.permute(2*A,'',0)
#         #print(self.result)
#         return self.result

# class Solution:
#     # @param A : list of integers
#     # @return a list of list of integers

#     def __init__(self):
#         self.result=[]
#     def subset(self,A,soFar,k):
#         #print(soFar)
#         val=sorted(soFar)
#         if k==len(A) and val not in self.result:
#             self.result.append(val)
#             return
#         if k==len(A):
#             return
#         soFar.append(A[k])
#         self.subset(A,soFar+[],k+1)
#         soFar.pop()
#         self.subset(A,soFar+[],k+1)
        


        

#     def subsetsWithDup(self, A):
#         self.result=[]
#         #B=sorted(A)
#         self.subset(A,[],0)
#         return sorted(self.result)

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def __init__(self):
        self.result=[]
    def bt(self,A,soFar):
        if len(soFar)==len(A):
            self.result.append(soFar)
            return
        for i in A:
            if i not in soFar:
                soFar.append(i)
                self.bt(A,soFar+[])
                soFar.pop()
                
    def permute(self, A):
        self.result=[]
        self.bt(A,[])
        return self.result



