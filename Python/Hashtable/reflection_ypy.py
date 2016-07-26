class Solution(object):
    def isReflection(self,a,b):
        if (self.containsOrigin):
            if abs(a[0])==abs(b[0]) and a[1]==b[1]:
                return True
            return False
        if a[1]==b[1]:
            return True
        return False
    def getReflection(self,point,ref_x):
        return ref_x-(point[0]-ref_x)


    def isReflectedYAxis(self,points):
        i=0
        while(i<len(points)):
            reflected=self.getReflection(points[i])
            if(reflected not in points):
                return False
            i+=1
        return True

   # def getReflection(self,point,refX):


    def isReflected(self,points):
        if(len(points)==0):
            return True

        min=float("inf")
        max=-min
        i=0
        while(i<len(points)):
            points[i][0]=float(points[i][0])                        
            if  points[i][0]>max:
                max= points[i][0]
            if  points[i][0]<min:
                min= points[i][0]
            i+=1

        refX=float(max+min)/2
        
        i=0
        while(i<len(points)):
            ref_i=self.getReflection(points[i],refX)
            #print(refX)
            #print(ref_i)
            #print(points)
            if([ref_i,(points[i][1])] not in points):
                return False
            i+=1
        return True


    def isReflectedSlow(self, points):
        
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        x={}

        i=0
        
        #prev
        while(i<len(points)):            
            j=0
            while(j<len(points)):
                if(points[i][1]==points[j][1]):
                    mid=(points[i][0]+points[j][0])/2
                    #print(mid)
                    if(mid in x.keys()):
                        x[mid]+=1
                    else:
                        x[mid]=1
                j+=1
            i+=1
        print(x)
        for key in x.values():
            if key>=len(points):
                return True
        return False



s=Solution()
#print(s.isReflected([[0,0],[1,0],[3,0]]))
#print(s.isReflected([[0,0],[1,1],[-1,1]]))
print(s.isReflected([[1,1],[1,1],[1,1]]))
#print(s.isReflected([[1,1],[1,-1]]))
#print(s.isReflected([[0,0],[1,0],[3,0],[-2,1],[1,1],[5,1]]))

        