"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""

#result = [0,3,5,4,6,7,2]

class Solution(object):
    def minRange(self,dictionary):
        import heapq

        min_heap=[]
        global_min=float("Inf")
        global_max=-global_min
        min_diff=global_max
        min_max=[]
        min_index=None
        max_index=None

        global_dict={}

        min_key=None
        min_val=global_min

        keys=list(dictionary.keys())
        i=0
        j=0
        

        for key in keys:
            # print(dictionary)
            val=dictionary[key].pop(0)
            global_dict[val]=key
            heapq.heappush(min_heap,val) 
            if val<min_val:
                min_val=val
                min_key=key
        if(len(dictionary[key])==0):
            val=heapq.heappop(min_heap)
            if(len(min_heap)>0):
                return (val,max(min_heap))
            else:
                return (val,val)


        while(len(min_heap)>0 and len(dictionary[global_dict[min_heap[0]]])>0):
             
            #print(min_heap)
            val2=heapq.heappop(min_heap)
            if(len(min_heap)==0):
                key=global_dict[val2]
                max_val=dictionary[key][0]
            else:
                max_val=max(min_heap)
            min_max.append((val2,max_val))
            # if val2<min_val:
            #     min_val=val2
            min_key=global_dict[val2]
            
            val=dictionary[min_key].pop(0)
            global_dict[val]=min_key
            heapq.heappush(min_heap,val)  
            # print("min key "+str(min_key))
            print("heap "+str(min_heap))   
            print(dictionary)       
            print("min max"+str(min_max))
            # if(len(min_heap)==0 or len(dictionary[global_dict[min_heap[0]]])==0):
            #     val = heapq.heappop(min_heap)
            #     if(len(min_heap)==0):
            #         max_val=
            #     else:
            #         max_val=max(min_heap)
            #     min_max.append((val,max_val))
            #     break
        if(len(min_heap)>0):
            val2=heapq.heappop(min_heap)
            if(len(min_heap)==0):
                key=global_dict[val2]
                if(len(dictionary[key])>0):
                    max_val=dictionary[key][0]
                else:
                    max_val=float("Inf")
            else:
                max_val=max(min_heap)
            min_max.append((val2,max_val))
            


        print(min_max)
        print(min_heap)

        for tup in min_max:
            
            if abs(tup[1]-tup[0])<global_min:
                global_min=abs(tup[1]-tup[0])
                min_index=min(tup)
                max_index=max(tup)
        return (min_index,max_index)

        

        
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s==t:
            return s
        if len(s)==0 or len(s)<len(t):
            return ""
        dictionary={}
        t_dict={}
        for i in t:
            if i in t_dict:
                t_dict[i]+=1
            else:
                t_dict[i]=1

        for i,val in enumerate(s):
            if val in t:
                if val in dictionary:
                    dictionary[val].append(i)
                else:
                    dictionary[val]=[i]
        #print(t_dict)
        #print(dictionary)
        for key in t_dict:
            if key not in dictionary or len(dictionary[key])<t_dict[key]:
                return ""


        # print(dictionary)
        tup=self.minRange(dictionary)
        # print(tup)
        if(tup[0]==None or tup[1]==None):
            return ""
        else:
            return s[tup[0]:tup[1]+1]



a={
    'a':[0,2,4],
    'b':[1,5,7],
    'c':[3,6]
}

s=Solution()
S = "ADOBECODEBANC"
T = "ABC"
# S="baab"
# T="bbb"
# S="aabaabaaab"
# T="bb"
# S="ab"
# T="a"
# S="abc"
# T="ab"
# S="cabwefgewcwaefgcf"
# T="cae"
S="aabaabaaab"
T="bb"
S="bbaa"
T="aba"
print(s.minWindow(S,T))