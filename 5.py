mainList = []

for i in range(0,10):
	mainList.append(int(input("Enter {0}: ".format(i))))
print(mainList)

mainList.reverse()
print(mainList)
