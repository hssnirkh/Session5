#not compilited
mainList = []
showList = []
c = 0
for i in range(0,3):
	mainList.append(input("Enter {0}:".format(i)))
print(mainList)

for j in range(0,3):
	for z in range(j+1,3):
		if(mainList[j][0] == mainList[z][0]):
			print(mainList[j])
			#continue
print(">>>>>>>>>>>>>>>")
for ii in range(0,3):
	for jj in range(ii+1,3):
		if(mainList[ii]==mainList[jj]):
			print("yes",mainList[jj])
			
