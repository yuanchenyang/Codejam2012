#!/usr/bin/env python3 
import sys

fileName = sys.argv[1]
asmFile = open(fileName)
lines = asmFile.readlines()
asmFile.close()

cycles = [["e","o","k","i","d","s","n","b","h","x","m","l","g","v","p","r","t","w","f","c"],["j","u"],["q","z"],["a","y"],[" "]]

numberOfLines=int(lines[0])
output = ""

for i in range(numberOfLines):
	lineBuffer=lines[i+1]
	outputBuffer = "Case #"+str(i+1)+": "
	for char in lineBuffer:
		if char == "\n": break
		for cycle in cycles:
			if char in cycle:
				for entry in range(len(cycle)):
					if cycle[entry] == char:
						outputBuffer = outputBuffer + cycle[(entry+1)%len(cycle)]
						break
				break
	output= output+ outputBuffer + "\n"

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