###########################
#THIS CODE IS SUPER UGLY =(
###########################
import sys

fileName = sys.argv[1]
asmFile = open(fileName)
lineList = asmFile.readlines()
asmFile.close()

#Important! Remove first number from input and add "0 0" at the end of the file
output = ""

#Everything remains as strings
lines = [s.split()[0] for s in lineList]
d={0:"Neither",1:"Red",2:"Blue",3:"Both"}

#/:1,-1
def chk1(l,n,k,c,dx,dy):
	for y in range(k-1,n):
		for x in range(n-k+1):
			if (l[y][x] != ".") and (c==l[y][x]):
				success=True
				for i in range(k): 
					if c!=l[y+(i)*dy][x+(i)*dx]:
						success=False
						break
				if success:
					return True
	return False
#\:1,1				
def chk2(l,n,k,c,dx,dy):
	for y in range(n-k+1):
		for x in range(n-k+1):
			if (l[y][x] != ".") and (c==l[y][x]):
				success=True
				for i in range(k): 
					if c!=l[y+(i)*dy][x+(i)*dx]:
						success=False
						break
				if success:
					return True
	return False				

#-:1,0
def chk3(l,n,k,c,dx,dy):
	for y in range(n):
		for x in range(n-k+1):
			if (l[y][x] != ".") and (c==l[y][x]):
				success=True
				for i in range(k): 
					if c!=l[y+(i)*dy][x+(i)*dx]:
						success=False
						break
				if success:
					return True
	return False

#|:0,-1
def chk4(l,n,k,c,dx,dy):
	for y in range(k-1,n):
		for x in range(n):
			if (l[y][x] != ".") and (c==l[y][x]):
				success=True
				for i in range(k): 
					if c!=l[y+(i)*dy][x+(i)*dx]:
						success=False
						break
				if success:
					return True
	return False

started = False
liner = []
t=0
count=0
for line in lines:
	if line[0]=="R" or line[0]=="B" or line[0]==".":
		#rotate
		ln=""
		for i in line:
			if i != ".":
				ln=ln+i
			else:
				ln="."+ln
		liner.append(ln)
	else:
		if started:
			count+=1
			#check red
			if chk3(liner,n,k,"R",1,0):
				answer+=1
			elif chk4(liner,n,k,"R",0,-1):
				answer+=1				
			elif chk1(liner,n,k,"R",1,-1):
				answer+=1				
			elif chk2(liner,n,k,"R",1,1):
				answer+=1			
			#check blue
			if chk3(liner,n,k,"B",1,0):
				answer+=2
			elif chk4(liner,n,k,"B",0,-1):
				answer+=2				
			elif chk1(liner,n,k,"B",1,-1):
				answer+=2				
			elif chk2(liner,n,k,"B",1,1):
				answer+=2
					
		r=False
		b=False	
		m = lineList[t].split()
		n=int(m[0])
		k=int(m[1])
		liner=[]
		if started:
			output += "Case #" + str(count) + ": "+ d[answer] + "\n"
		answer = 0 
		started = True
	t+=1
	
print(output)

writeFileName = fileName.rsplit(".",1)[0] + ".out"

writeFile = open(writeFileName, 'w')
writeFile.write(output)
writeFile.close()