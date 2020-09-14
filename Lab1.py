transactions = {'bread': set("12345678"), 'milk': set("123678"), 'water': set("23568"),
              'coffee': set("2567"), 'cake': set("1478"),'potatoes': set("123468")}
frequentSetsOfProducts = []
minimumSupport = 0.6
helpList = []
for i in transactions:
    if len(transactions[i])/8 > minimumSupport:
        helpList.append([i])
frequentSetsOfProducts = helpList
currantIteration = 2
amountOfElementsInHelpList = len(helpList)
while currantIteration <= len(transactions.keys()):
    newList = []
    index = 0
    for i in range(amountOfElementsInHelpList):
        for j in range(amountOfElementsInHelpList):
            if i != j and i < j:
                newList.append(helpList[i].copy())
                newList[index].extend(helpList[j].copy())
                index += 1
    if len(newList)==0:
        currantIteration += 1
        continue
    for i in range(len(newList)):
        newList[i] = list(set(newList[i]))
    for i in newList:
        i.sort()
    for i in newList:
        while newList.count(i) > 1:
            newList.remove(i)
    helpList = newList.copy()
    newList.clear()
    amountOfElementsInHelpList = len(helpList)
    helpSet = set()
    for i in helpList:
        helpSet = transactions[i[0]].copy()
        for j in range(len(i)):
            for k in range(j,len(i)):
                helpSet.intersection_update(transactions[i[j]], transactions[i[k]])
        if len(helpSet)/8 > minimumSupport:
            frequentSetsOfProducts.append(i)
    currantIteration += 1
print("The result of the program\n", frequentSetsOfProducts)


helpList.clear()
frequentSetsOfProducts.clear()
























