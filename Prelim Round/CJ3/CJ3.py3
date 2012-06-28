#!/usr/bin/env python3 
import sys

fileName = sys.argv[1]
asmFile = open(fileName)
lines = asmFile.readlines()
asmFile.close()

numberOfLines=int(lines[0])
output = ""

#lines[len(lines)-1]+="\n"

for i in range(numberOfLines):
	lineBuffer = lines[i+1]
	answer = 0
	numP=0
	lB=0
	uB=0
	charBuffer=""
	for char in lineBuffer:
		if (char == " ") or (char=="\n"):
			numP=numP+1
			if numP == 1:
				lB=int(charBuffer)
				charBuffer=""
			elif numP ==2:
				uB=int(charBuffer)
				charBuffer=""
				break
		else:
			charBuffer=charBuffer+char
	for j in range(lB,uB+1):
		if j<10:
			pass
		else:
			n=str(j)
			counted=[]
			for k in range(1,len(n)):
				m=int(n[k:]+n[:k])
				if (n[k]!=0) and (m<=uB) and (m>j) and (m not in counted):
					answer += 1
					counted.append(m)
	output = output + "Case #"+str(i+1)+": " + str(answer) + "\n"
	print(i)
				

output=output[:len(output)-1] #removes unwanted \n at the end

writeFileName = ""
for l in range(len(fileName)):
	if fileName[l] == ".":
		break
	writeFileName = writeFileName + fileName[l]

writeFileName = writeFileName + ".out"

writeFile = open(writeFileName, 'w')
writeFile.write(output)
writeFile.close()