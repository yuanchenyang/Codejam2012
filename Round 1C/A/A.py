import sys
import resource
 

sys.setrecursionlimit(1500)


fileName = sys.argv[1]
asmFile = open(fileName)
lineList = asmFile.readlines()
asmFile.close()


lineList = [[int(a) for a in s.split()] for s in lineList]
numCases=lineList[0][0]
lineList = lineList[1:]

#Build Index
index=[0]
cases=[]
s=0
su=0
for i in range(numCases):
	su=lineList[s][0]
	index.append(su+1)
	cases.append(lineList[s+1:s+1+su])
	s=sum(index)

output = ""

diamond = False
def expand(node):
	global diamond, visited
	if (graph[node] != []) and (diamond==False):
		for n in graph[node]:
			if n not in visited:
				expand(n)
				visited.append(n)
			else: 
				diamond = True
				break
	
count=0
d={True:"Yes", False:"No"}
for case in cases:
	count+=1
	graph={}
	diamond = False
	for i in range(len(case)):
		if case[i][0] != 0:
			graph[i+1]=case[i][1:]
		else:
			graph[i+1]=[]
	for vertex in graph:
		visited = []
		if diamond == False:
			expand(vertex)
		else: break
	output+="Case #"+str(count)+": "+ d[diamond] +"\n"
		


print output

writeFileName = fileName.rsplit(".",1)[0] + ".out"

writeFile = open(writeFileName, 'w')
writeFile.write(output)
writeFile.close()