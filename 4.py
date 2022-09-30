mainList = []

for i in range(0,10):
	mainList.append(int(input("Number {0} for list : ".format(i))))
print(mainList)

num = int(input("Num for delet : "))
for j in range(0,len(mainList)):
	if(mainList[j] == num):
		mainList.remove(num)
		break

print(mainList)
