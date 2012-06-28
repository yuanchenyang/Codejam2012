import sys

fileName = sys.argv[1]
asmFile = open(fileName)
lineList = asmFile.readlines()
asmFile.close()


lineList = lineList[1:]

lines = [[int(a) for a in s.split()] for s in lineList]

output = ""

i=0
for line in lines:
	i+=1
	output+="Case #"+str(i)+": "
	n =line[0]
	line = line[1:]
	x=sum(line)
	xt=x
	#[a+b,a,b,i]
	lin=[]
	for b in range(n):
		lin.append([0,line[b],0,b])
	#line = [[0,a,0,i] for i in range(n) for a in line]
	while x!=0:
		for l in lin:
			l[0]=l[1]+l[2]
		lin.sort()
		no=0
		j=lin[0][0]
		for l in lin:
			if l[0] == j:
				no+=1
			else:
				k=l[0]
				break
		if (k-j)*no <= x and no!=n:
			for m in range(no):
				lin[m][2]+=k-j
			x-=(k-j)*no
		else:
			for m in range(no):
				lin[m][2]+=float(x/no)
			break
	for l in lin:
		l[0]=l[3]
	lin.sort()
	for l in lin:
		output+=str(100*float(l[2]/xt))+" "
	output+="\n"

print(output)

writeFileName = fileName.rsplit(".",1)[0] + ".out"

writeFile = open(writeFileName, 'w')
writeFile.write(output)
writeFile.close()
