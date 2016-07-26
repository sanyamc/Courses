class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        length=len(nums)
        if(length<2):
            return []
        result=[]
        print(nums)
        #dp=[]
        for i in range(0,length):
            target=0-nums[i]
            sub_nums=nums[0:i]
            sub_nums.extend(nums[i+1:length])
            j=0
            k=j+1
            print(sub_nums)
            
            out=True
            while(j<k and j>=0):
                temp=sub_nums[k]+sub_nums[j]
                if(temp==target):
                    val=sorted([sub_nums[j],sub_nums[k],nums[i]])
                    if val not in result:
                        result.append(val)
                    if(out==True and j==0 and k==len(sub_nums)-1):
                        break
                    if(out==False and k-j<=1):
                        break
                    if(j==0):
                       k-=1
                    elif k==len(sub_nums)-1:
                        j+=1
                    else:
                        k+=1
                        j-=1

                elif(temp<target):
                    if(k==len(sub_nums)-1):
                        j+=1
                    else:
                        k+=1
                else:
                    if(j==0):
                        k-=1
                    else:
                        j-=1
                print("j "+str(j)+" k: "+str(k))
                


        return result
                


                


        #for i in range(0,length):
        #    s=set()
        #    for j in range(i+1,length):
        #        s.add((nums[i],nums[j]))
        #    dp.append(s)


        ##dp.append(s)
        #print(dp)
        #for i in range(2,length):
        #    j=i-1
        #    while(j>=0):
        #        #print(dp[j])
        #        for t in dp[j]:
        #            #print(dp)
        #            temp=t[0]+t[1]+nums[i]
        #            if(temp==0):
        #                val=[t[0],t[1],nums[i]]
        #                if val not in result:
        #                    result.append(val)
        #            #elif(t[0]+t[1]>nums[i]):
        #            #    break
        #        j-=1


        
       


                
            #for b in range(i+1,len(nums)):
            #    for c in range(b+1,len(nums)):
            #        if(nums[b]+nums[c]+nums[i]==0):
            #            result.append([nums[b],nums[c],nums[i]])
        #return result


s=Solution()
test2=[3,0,-2,-1,1,2]
test1=[-1, 0, 1, 2, -1, -4]
test3=[0,0,0]
test4=[0,-4,-1,-4,-2,-3,2]
print(s.threeSum(test2))
            
        