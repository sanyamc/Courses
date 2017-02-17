
# class Solution:
#     def __init__(self):
#         self.result=[]
#         self.counter=0
#         self.k=0
#     def bt(self,A,soFar):
#         if len(soFar)==len(A):
#             self.counter+=1
#             if self.counter==self.k:
#                 self.result=soFar
#             #self.result.append(soFar)
#             return
#         for i in A:
#             if i not in soFar:
#                 soFar.append(i)
#                 self.bt(A,soFar+[])
#                 soFar.pop()
                
#     def get_permutation(self, inputSet, k):
#         if len(inputSet)==0:
#             return ""
#         so_far=inputSet
#         self.k=k
#         self.result=[]
#         self.bt(inputSet,[])
#         # for i in range(0,k-1):
#         #     val = self.next_permutation(so_far)
#         #     if val==None:
#         #         return ""
#         #     else:
#         #         so_far = val
            
#         so_far = [ str(j) for j in self.result]

#         return "".join(so_far)
#     # @param n : integer
#     # @param k : integer
#     # @return a strings
#     def getPermutation(self, n, k):
#         inputSet=[]
#         for i in range(1,n+1):
#             inputSet.append(i)
#         return self.get_permutation(inputSet,k)



class Solution:

    def next_permutation(self, so_far):

        i=len(so_far)-1
        new = so_far+[]
        #print("soFar: "+str(so_far))
        
        while(i>0):
            if new[i]>new[i-1]:
                # swap with the largest element just greater than i-1
                j=i
                while(j<len(new)):
                    if new[j]>new[i-1]:
                        j+=1
                    else:
                        j=j-1
                        break
                #print("i: "+str(i)+" j: "+str(j))
                
                if j==len(new):
                    j=j-1
                new[i-1],new[j]=new[j],new[i-1]
                #print("new: "+str(new))
                #new = new[i+1::-1]
                temp=new[i:]
                temp.sort()
                new = new[:i]+temp
               # print("new: "+str(new))
                return new
            # j=i-1
            # while (j>=0):
            #     if new[i]>new[j]:
            #         new[i],new[j]=new[j],new[i]
            #         temp = new[j+1:]
            #         temp.sort()
            #         new=new[:j+1]+temp
            #         print("new: "+str(new))
            #         return new
            #     j=j-1
            i=i-1


    def get_permutation(self, inputSet, k):
        if len(inputSet)==0:
            return ""
        so_far=inputSet
        for i in range(0,k-1):
            val = self.next_permutation(so_far)
            if val==None:
                return ""
            else:
                so_far = val
            
        so_far = [ str(j) for j in so_far]

        return "".join(so_far)
                

            
        
        return so_far
    # @param n : integer
    # @param k : integer
    # @return a strings
    def getPermutation(self, n, k):
        inputSet=[]
        for i in range(1,n+1):
            inputSet.append(i)
        return self.get_permutation(inputSet,k)

s=Solution()
s.getPermutation(4,5)