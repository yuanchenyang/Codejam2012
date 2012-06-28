import sys

fileName = sys.argv[1]
asmFile = open(fileName)
lineList = asmFile.readlines()
asmFile.close()

#Converts everything to floating point
lines = [[float(a) for a in s.split()] for s in lineList]

n=lines[0][0]
output = ""
#s1:keep typing
#s2:enter right away
for i in range(int(n)):
	print(i)
	a=lines[2*i+1][0]
	b=lines[2*i+1][1]
	p=lines[2*(i+1)]
	s=[]
	s2 = b+2
	q=1
	for j in range(int(a)):
		q=q*p[j]
	s1=q*(b-a+1)+(1-q)*(2+2*b-a)
	s.append(s1)
	s.append(s2)
	q=1
	for j in range(int(a)):
		j1=a-j-1
		q=q*p[j]
		s.append(q*(2*j1+b-a+1)+(1-q)*(2*j1+2*b-a+2))
	output+="Case #"+str(i+1)+": "+str(min(s))+"\n"
	
print(output)

writeFileName = fileName.rsplit(".",1)[0] + ".out"

writeFile = open(writeFileName, 'w')
writeFile.write(output)
writeFile.close()
