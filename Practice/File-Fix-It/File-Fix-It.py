#Parses each space-separated string on a line into a list, 
#then nests those lists based on their line order in the original file

#!/usr/bin/env python3 
import sys

fileName = sys.argv[1]
asmFile = open(fileName)
lineList = asmFile.read()
asmFile.close()

numCases=int(lineList.split("\n")[0])
lineList = lineList.split("\n")[1:]

#Build Index
su=0
index=[[0,0]]
existing=[]
new=[]
for i in range(numCases):
	index.append([int(j) for j in lineList[su].split()])
	e=index[-1][0]
	n=index[-1][1]
	existing.append(lineList[su+1:su+1+e])
	new.append(lineList[su+1+e:su+1+e+n])
	su += sum(index[-1])+1

output = ""

#l=[leaf1,leaf2,...]
#subtree={node1:{subnode1:...},node2:{subnode1:...},...}
mkdir=0
def addToTree(l,subtree):
	global mkdir
	if len(l) !=0:
		if l[0] not in subtree:
			subtree[l[0]]={}
			mkdir+=1
		addToTree(l[1:],subtree[l[0]])

for i in range(numCases):
	tree={"":{}}
	e=existing[i]
	if len(e)!=0:
		e=[s.split("/") for s in e]
		for j in e:
			addToTree(j,tree)
	n=[s.split("/") for s in new[i]]
	mkdir=0
	for j in n:
		addToTree(j,tree)
	output+="Case #"+str(i+1)+": "+str(mkdir)+"\n"
	print(tree)

writeFileName = fileName.rsplit(".",1)[0] + ".out"

writeFile = open(writeFileName, 'w')
writeFile.write(output)
writeFile.close()