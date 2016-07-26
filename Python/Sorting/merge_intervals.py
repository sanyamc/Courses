 #Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e


class Solution(object):
    def __init__(self):
        self.interval=[]
    def removeOverlap(self,s,e):

        for index,i in enumerate(self.interval):            
            if((i[0]<=s and i[1]>=e) or (s<=i[0] and e>=i[1])):
                self.interval[index]=[min(s,i[0]),max(e,i[1])]
                
            
            if((i[0]<=s and i[1]>=s) or (s<=i[0] and e>=i[0])):
                self.interval[index]=[min(s,i[0]),max(e,i[1])]

    def doesOverlap(self,p1,p2):# assuming p1[0]<=p2[0]
            if((p1[0]==p2[0]) and (p1[1]==p2[1])):
                return True
            if(p1[1]>p2[0]):
                return True
            #if((p1[0]<=p2[0] and p1[1]>p2[1]) or (p1[0]<p2[0] and p1[1]>p2[1])):                
            #    return True
            #if((p2[0]<p1[0] and p2[1]>p1[0]) or (p1[0]<p2[0] and p1[1]>p2[0])):                
            #    return True
           # print("returning false")
            return False

                

    def handleOverlap(self,s,e):
        #overlapped=False
        indexToRemove=[]
        currMin=s
        currMax=e
        for index,i in enumerate(self.interval):            
            if((i[0]<=s and i[1]>=e) or (s<=i[0] and e>=i[1])):                
                self.interval[index]="remove"
                currMin=min(s,i[0],currMin)
                currMax=max(currMax,e,i[1])
            if((i[0]<=s and i[1]>=s) or (s<=i[0] and e>=i[0])):                
                currMin=min(s,i[0],currMin)
                currMax=max(currMax,e,i[1])
                self.interval[index]="remove"
        self.interval=[x for x in self.interval if x!="remove"]
        self.interval.append([currMin,currMax])

          
        
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        for i in intervals:
            self.handleOverlap(i[0],i[1])
        print(self.interval)
        return self.interval

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        overlaps=0
        skipIndex=[]
        curr_cont=0
        last_overlap=-1
        rooms=1
        length=len(intervals)
        if(length<2):
            return length
        import heapq
       
        intervals=sorted(intervals,key=lambda Interval: Interval.start)
        end=[intervals[0].end]
       # print(intervals)
        for i in range(1,length):
           val=intervals[i]
           if (val.start==intervals[i-1].start and val.end==intervals[i-1].end):
               rooms+=1
           elif val.start<end[0]:
               rooms+=1
               heapq.heappush(end,val.end)
           else:
               heapq.heappop(end)
               heapq.heappush(end,val.end)
            #j=curr_cont
            ##print("j: "+str(j)+" last:"+str(last_overlap))
            
            #if self.doesOverlap([intervals[j].start,intervals[j].end],[intervals[i].start,intervals[i].end]):
            #    if last_overlap==-1:
            #        last_overlap=i
            #        rooms+=1
            #    elif self.doesOverlap([intervals[last_overlap].start,intervals[last_overlap].end],[intervals[i].start,intervals[i].end]):
            #        rooms+=1
            #        last_overlap=i
            #else:
            #    curr_cont=i
        return rooms


              




                
#1,3
#2,5
s=Solution()
#intervals =
print(s.minMeetingRooms([Interval(2,3),Interval(4,5),Interval(6,7),Interval(1,10)]))
print(s.minMeetingRooms([Interval(6,15),Interval(6,17),Interval(13,20)]))
print(s.minMeetingRooms([Interval(11,20),Interval(4,19),Interval(13,17),Interval(6,13)]))
print(s.minMeetingRooms([Interval(6,10),Interval(12,14),Interval(13,14)]))
#[[11,20],[4,19],[13,17],[6,13]]
#print(s.doesOverlap([5,7],[5,7]))
#s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]])
#s.handleOverlap(2,5)
#print(s.interval)
#s.handleOverlap(2,3)
#print(s.interval)
#s.handleOverlap(10,30)
#print(s.interval)
#s.handleOverlap(1,30)
#print(s.interval)