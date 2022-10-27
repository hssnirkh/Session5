mainList = []
showList = []
for i in range(0,3):
    mainList.append(input(f"enter {i}:"))
print(mainList)

for j in range(0,len(mainList)):
    for z in range(j,len(mainList)):
        if(mainList[j][0] == mainList[z][0]):
            print(mainList[j])