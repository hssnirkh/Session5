nameList = []
gradeList = []
countList = []
print(nameList)

for j in range(0,3):
	c = 0
	nameList.append(input("Name {0}: ".format(j)))
	sum=int(input("tedad dars = "))
	for z in range(0,sum):
		gradeList.append(int(input("Grade {0} for {1}: ".format(z,nameList[j]))))
		c += 1
	countList.append(c)
print(nameList)
print(gradeList)
print(countList)

