
## combination and subset is interesting
## key to any backtracking solution is identifying what to look for
## for e.g. in subsets we are looking for if element is there in the entire set/subset or not
## however in permutation we are looking for if element has acquired that position or not.



def combine(input, soFar, k=None, index=0):
    if k and len(soFar)==k:
        print(soFar)
        return
    if index==len(input) and not k:
        print(soFar)
        return
    if index>=len(input):
        return
    soFar.append(input[index])
    combine(input, soFar, k, index+1)
    soFar.pop()
    
    combine(input, soFar, k, index+1)


f=[1,2,3,4,5]

# combine(f,[],3)
# print("next is: ")
# combine(f,[])

def permute(input, soFar):
    if len(input)==len(soFar):
        print(soFar)
    
    for i in range(0,len(input)):
        if input[i] not in soFar:  ## we could optimize here which could become a basis of bitmasking
            soFar.append(input[i])
            permute(input,soFar)
            soFar.pop()
f=[1,2,3,4]

permute(f,[])

            

        


    
    

    