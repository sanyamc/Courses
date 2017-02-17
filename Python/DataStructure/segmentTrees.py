
class SegmentTrees:

    def __init__(self,inputArray):
        self.st=[]
        self.ia=inputArray
        self.fun = max
        self.st = [None for i in range(1, 4*len(inputArray))]
        self.build_segment(1,0,len(inputArray)-1)

    def rmq(self, i, j):
        if i==j:
            return self.ia[i]
        else:
            p = self.rmq_helper(1, i, j, 0, len(self.ia)-1)
            print("answer: "+str(self.ia[p]))
            return self.ia[p]


    def rmq_helper(self, node , i, j, l, r):

        if i==l and j==r:
            return self.st[node]

        mid = (l+r)//2
        if j<=mid:
            p = self.rmq_helper(node<<1, i, j, l, mid)
            return p
        elif i>mid:
            p = self.rmq_helper((node<<1) +1, i, j, mid+1, r)
            return p
        elif i<=mid and j>=mid:
            p1 = self.rmq_helper(node<<1, i, mid, l, mid)
            p2 = self.rmq_helper((node<<1) +1 , mid+1 ,j, mid +1, r)
            if (p1 is not None) and (p2 is not None):
                if self.ia[p1]>self.ia[p2]:
                    return p1
                else:
                    return p2
            else:
                if p1:
                    return p1
                elif p2:
                    return p2
        else:
            print("i:{},j:{},l:{},r:{}".format(i, j, l, r))
    
    def build_segment(self, node, l, r):
        if l == r:
            self.st[node] = l
        else:
            left = node<<1
            right = left+1
            #print("l: "+str(l)+" left: "+str(left))
            self.build_segment(left,l,((l+r)//2))
            self.build_segment(right,((l+r)//2 +1),r)
            if self.ia[l]>self.ia[r]:
                p = l
            else:
                p = r
            self.st[node] = p




a=[18,17,13,19,15,11,20]
s=SegmentTrees(a)   
print(s.rmq(0,2))
# print(s.rmq(0,3))
# print(s.rmq(4,6))
# s.rmq(3,6)
# s.rmq(1,3)
