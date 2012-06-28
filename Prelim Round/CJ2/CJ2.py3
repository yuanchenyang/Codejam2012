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
	n=0
	s=0
	p=0
	numP=0
	charBuffer=""
	for char in lineBuffer:
		if char == " ":
			numP=numP+1
			if numP == 1:
				n=int(charBuffer)
				charBuffer=""
			elif numP ==2:
				s=int(charBuffer)
				charBuffer=""
			elif numP ==3:
				p=int(charBuffer)
				break
		else:
			charBuffer=charBuffer+char
	if p<2:
		withoutS=p
		withS=p
	else:
		withoutS = p*3-2
		withS = p*3-4
	charsCut = 3+len(str(n))+len(str(s))+len(str(p))
	lineBuffer=lineBuffer[charsCut:]
	charBuffer=""
	for char in lineBuffer:
		if (char == " ") or (char == "\n"):
			g=int(charBuffer)
			if g>=withoutS:
				answer = answer + 1
			elif (g>=withS) and (s>0):
				answer = answer + 1
				s = s - 1
			charBuffer = ""
		else:
			charBuffer=charBuffer+char
	output = output + "Case #"+str(i+1)+": " + str(answer) + "\n"
	
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