pos = False
codePos = 0

def read(i, ind):
	try:
		return i[ind]
	except:
		return "000"

def createCode( i, code, hex ):
	global pos
	global codePos
	if pos:
		code[codePos] += hex + read(i,1)
		codePos += 1
		pos = not pos
	else:	
		code.append( hex + read(i,1) + " ")
		pos = not pos



with open('teste') as f:
     read_data = f.read()

#print (read_data)

data = read_data.split()

#print(data)

vet = []
for i in data:
	vet.append(i.split("."))


saida = open("ra.hex", "w+")

code = []
auxVar = []

for i in vet:
	if i[0] == "LOADM":
		createCode(i,code,"01 ")
	elif i[0] == "LOADMQM":
		createCode(i,code,"09 ")
	elif i[0] == "STORM":
		createCode(i,code,"21 ")
	elif i[0] == "LOADMQ":
		createCode(i,code,"0A ")
	elif i[0] == "ADDM":
		createCode(i,code,"05 ")
	elif i[0] == "SUBM":
		createCode(i,code,"05 ")
	elif i[0] == "MULM":
		createCode(i,code,"0B ")
	elif i[0] == "DIVM":
		createCode(i,code,"0C ")
	elif i[0] == "RSH":
		createCode(i,code,"15 ")
	elif i[0] == "LSH":
		createCode(i,code,"14 ")
	elif i[0] == "LOADM_ABS":
		createCode(i,code,"03 ")
	elif i[0] == "LOAD-M":
		createCode(i,code,"02 ")
	elif i[0] == "ADDM_ABS":
		createCode(i,code,"07 ")
	elif i[0] == "SUBM_ABS":
		createCode(i,code,"08 ")
	elif i[0] == "JUMPM_E":
		createCode(i,code,"0D ")
	elif i[0] == "JUMPM_D":
		createCode(i,code,"0E ")
	elif i[0] == "JUMP+M_E":
		createCode(i,code,"0F ")
	elif i[0] == "JUMP+M_D":
		createCode(i,code,"10 ")
	elif i[0] == "STORM_E":
		createCode(i,code,"12 ")
	elif i[0] == "STORM_D":
		createCode(i,code,"13 ")
	else:
		auxVar.append(i)


varCount = 0
var = []

for i in auxVar:
	aux = hex(varCount)[2:]
	endVar = aux.zfill(3)
	var.append(endVar + " " + i[1])
	i[1] = endVar
	varCount += 1

codeCount = varCount
for i in code:
	aux = hex(codeCount)[2:]
	saida.write(aux.upper().zfill(3) + " " + i + '\n')
	codeCount += 1


#print (code)
print (auxVar)
print (var)

