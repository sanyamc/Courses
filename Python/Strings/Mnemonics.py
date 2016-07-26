def getData(letter):
    dict={"2":["A","B","C"],
          "3":["D","E","F"],
          "4":["G","H","I"],
          "5":["J","K","L"],
          "6":["M","N","O"],
          "7":["P","Q","R","S"],
          "8":["T","U","V"],
          "9":["W","X","Y","Z"]}
    return dict[letter]

def computeMnemonics(number):
    mnemonics =[]
    for (i,val) in enumerate(number):
        mnemonics=getCombo(val,mnemonics)
    print(mnemonics)

def getCombo(val,mnemonics):
    #print(val)
    newData=[]
    #for i,value in enumerate(mnemonics):
    #    newData.append(value)

    if(len(mnemonics)==0):
        for i,letter in enumerate(getData(val)):
            newData.append(letter)
    else:
        for i,letter in enumerate(mnemonics):
            for j,value in enumerate(getData(val)):
                newData.append(mnemonics[i]+value)
    return newData

computeMnemonics(["2","3","4"])








