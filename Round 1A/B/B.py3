#This algorithm is wrong, but because of weak test cases in 
#Code Jam, it was still accepted.

#Changes to be made but too lazy to bother:
#	Should take the number in the second column whose 
#	difference with the current star count is the greatest

#Edit: Everything is correct now!

import sys

fileName = sys.argv[1]
asmFile = open(fileName)
lineList = asmFile.readlines()
asmFile.close()

#Converts everything to integer
lines = [[int(a) for a in s.split()] for s in lineList]

output = ""
l=[[]]
count=0
for line in lines[1:]:
	if len(line)==1:
		count+=1
		l.append([])
	else:
		l[count].append([line[0],line[1]])

count=0
for line in l[1:]:
	count+=1
	first=[]
	second=[]
	for i in line:
		i.insert(0,i[1])
	line.sort()
	for i in line:
		first.append(i[1])
		second.append(i[2])
	stars=0
	games=0
	skip=False
	feasible=False
	while len(line)!=0:
		for i in range(len(second)):
			if second[i] <= stars:
				if len(line[i]) == 4:
					stars+=1
				else:
					stars+=2
				games+=1
				temp=second.pop(i)
				temp=first.pop(i)
				t=line.pop(i)
				skip=True
				feasible=True
				break
		if not skip:
			for k in range(len(first)):
				feasible=False
				j=len(first)-k-1
				if (first[j] <= stars) and (len(line[j])<4):
					games+=1
					stars+=1
					line[j].append(0)
					feasible=True
					break
			if (not feasible) and (len(line)!=0):
				break	
		skip=False
	if not feasible:
		output+="Case #"+str(count)+": Too Bad\n"
	else:
		output+="Case #"+str(count)+": "+str(games)+"\n"
	

writeFileName = fileName.rsplit(".",1)[0] + ".out"

writeFile = open(writeFileName, 'w')
writeFile.write(output)
writeFile.close()
