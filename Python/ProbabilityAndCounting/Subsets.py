# using dfs
result=[]
perm=[]
def subsets_dfs(input_set):
    result=[]
    if not input_set:
        return set()
    if len(result)==0:
        [result.append(set({i})) for i in input_set if set({i}) not in result]


    queue = []
    queue.append(result[0])
    while(len(queue)>0):
        val = queue.pop(0)
        for i in input_set:
            if i in val:
                continue
            else:
                new_val = val.union({i})
                if new_val not in result:
                    result.append(new_val)
                    queue.insert(0,new_val)
    print("subsets are: "+str(result))


## using backtracking to generate permutation

def generate_permutations(input):
    if not input:
        return []
    soFar = []
    backtrack(input,soFar)
    print("perm is: "+str(perm))
    return perm


def backtrack(input,soFar):
    if len(input)==0:
        print(soFar)
        perm.append([soFar.copy()]) # process solution
        # soFar=[]
    else:
        for i in input:
            # if i in soFar:
            #     continue
            new_input=input.copy()
            new_input.pop(new_input.index(i))
            soFar.append(i)
            
            backtrack(new_input,soFar)
            soFar.pop()
            #input.append(i)

def backtrack_perm2(input, soFar, used):
    if len(soFar)==len(input):
        print(soFar)    
    else:
        for i in range(0,len(input)):
            # if input[i] not in soFar:
            #     soFar.append(input[i])
            #     backtrack_perm2(input, soFar.copy(),used)
            #     soFar.pop()
            if not used[i]:   ## above method does extra checking which we could avoid using an additional array
                used[i]=True
                soFar.append(input[i])
                backtrack_perm2(input, soFar.copy(),used)
                soFar.pop() # most algorithms overwrite at this position as opposed to appending and popping
                used[i]=False

used=[]
f = [1,2,3]
for i in range(0,len(f)):
    used.append(False)

backtrack_perm2(f, [], used)



        

#generate_permutations([1,2,3])


#########################################################
######### Generates subset of size k from input of size n
#########

def backtrack_subsetK(soFar,inputSet, k, n=None):

    if len(soFar)==k:
        print(str(soFar))
        
        return
    if len(soFar)==k or len(inputSet)==0:
        #print("returning")
        return
    
    
    new_input = inputSet.copy()
    new_input.pop(0)
      
    backtrack_subsetK(soFar.union({inputSet[0]}).copy(), new_input.copy(), k)
    backtrack_subsetK(soFar.copy(), new_input.copy(),k)


f = [1,2,3,4,5]
#backtrack_subsetK(set(),f,3)



