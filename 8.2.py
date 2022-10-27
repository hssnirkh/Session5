mainList = []
showList = []


for i in range(0,4):
    mainList.append(input())
print(mainList)

for j in range(0,len(mainList)):
    counter = 0
    c = mainList[j][0]
    for z in range(j+1,len(mainList)):
        ch = mainList[z][0]
        if(c == ch):
            counter += 1
            print(counter)
            if(counter == 1):
                showList.append(mainList[j]) #in ro yebar niaz darim
                showList.append(mainList[z])
                print(showList)