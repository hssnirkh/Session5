mainList = []
showList = []

for i in range(0,3):
	mainList.append(input("STR : "))
chr = input("Enter chr : ")
for j in range(0,len(mainList)):
	c = mainList[j]
	for z in range(0,len(c)):
		if(c[1] == chr):
			showList.append(j)
			break

print(mainList,showList)
