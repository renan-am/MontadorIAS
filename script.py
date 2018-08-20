#posição da memoria (em decimal) onde inicia a alocação de memoria, se deixada em 0, o programa escolhe um valor adequado
memVarStart = 0
#variaveis globais para usar nas funções
pos = False #False -> esquerda, inicio da linha // True: direita, final da linha
codePos = 0
auxVar = []
code = []
memCount = 0
points = [["pointfinal", 400, False]]
toPoints= []


#checa flags
def checkFlags (i, line, pos):
	if i[-1][0:5] == "point":
		points.append([i[-1], line, pos])
	elif i[-1][0:7] == "toPoint":
		toPoints.append([i[-1], line, pos])
	elif i[-1][0:4] == "change":
		return
	elif i[-1][0:4] == "toChange":
		return


#retorna o endereço da variavel, encontrado em auxVar
def varAdress (variable):
	for i in auxVar:
		if i[0] == variable:
			return i[1]
	return variable

# testa se o indíce existe no vetor, evita outofbounds error
# se existir retorna o endereço da variavel
# se não existir retorna 000, (pra funções como RSH, LSH etc)
def read(i, ind):
	try:
		return varAdress(i[ind])
	except:
		return "000"

# concatena a instrução junto com a memória respectiva
def createLine( i, hexaCode ):
	global pos
	global codePos
	global auxVar
	global code
	global memCount
	line = hex(memCount)[2:].upper().zfill(3)
	checkFlags (i, line, pos);
	if pos:
		code[codePos].append(hexaCode)
		code[codePos].append(read(i,1) + " ")
		codePos += 1	
		memCount += 1
	else:
		code.append([line + " "])	
		code[codePos].append(hexaCode)
		code[codePos].append(read(i,1) + " ")
	pos = not pos


#abre o codigo a ser "compilado"
with open('teste') as f:
     read_data = f.read()


# cria um vetor com cada bloco do texto (separado por " "), 
# a partir do vetor cria uma matriz com cada linha referente a um bloco, cada coluna referente a (instrução, memoria), ou ao (nome da variavel, valor da variavel)
vet = []

data = read_data.split()
for i in data:
	vet.append(i.split("."))

#procura flags




	

#preenche auxVar com as variaveis
for i in vet:
	if i[0] == "LOADM":
		continue	
	elif i[0] == "LOADMQM":
		continue	
	elif i[0] == "STORM":
		continue	
	elif i[0] == "LOADMQ":
		continue	
	elif i[0] == "ADDM":
		continue	
	elif i[0] == "SUBM":
		continue	
	elif i[0] == "MULM":
		continue
	elif i[0] == "DIVM":
		continue
	elif i[0] == "RSH":
		continue
	elif i[0] == "LSH":
		continue
	elif i[0] == "LOADM_ABS":
		continue
	elif i[0] == "LOAD-M":
		continue
	elif i[0] == "ADDM_ABS":
		continue
	elif i[0] == "SUBM_ABS":
		continue
	elif i[0] == "JUMPM":
		continue
	elif i[0] == "JUMP+M":
		continue
	elif i[0] == "STORM_E":
		continue
	elif i[0] == "STORM_D":
		continue
	else:
		auxVar.append(i)

var = []

if memVarStart != 0:
	memVar = memVarStart
else:
	memVar = int(len(vet) / 2)

# salva em var as linhas de código pronta, com o endereço e valor da memória de cada variavel
# salva em auxVar o endereço de cada variavel
for i in auxVar:
	# converte em uma string hexadecimal, depois ignora os dois primeiros caracteres (0x), zfill(x) coloca 0 a esquerda do valor da string, até ter x caracteres
	endVar =  hex(memVar)[2:].upper().zfill(3)   
	var.append([endVar + " ", i[1]])
	i[1] = endVar
	memVar += 1

# salva em code as instruções e memorias relativas, em hexadecimal, com duas isntruções por linha, e variaveis substituidas por seus endereços


for i in vet:
	if i[0] == "LOADM":
		createLine(i,"01 ")
	elif i[0] == "LOADMQM":
		createLine(i,"09 ")
	elif i[0] == "STORM":
		createLine(i,"21 ")
	elif i[0] == "LOADMQ":
		createLine(i,"0A ")
	elif i[0] == "ADDM":
		createLine(i,"05 ")
	elif i[0] == "SUBM":
		createLine(i,"06 ")
	elif i[0] == "MULM":
		createLine(i,"0B ")
	elif i[0] == "DIVM":
		createLine(i,"0C ")
	elif i[0] == "RSH":
		createLine(i,"15 ")
	elif i[0] == "LSH":
		createLine(i,"14 ")
	elif i[0] == "LOADM_ABS":
		createLine(i,"03 ")
	elif i[0] == "LOAD-M":
		createLine(i,"02 ")
	elif i[0] == "ADDM_ABS":
		createLine(i,"07 ")
	elif i[0] == "SUBM_ABS":
		createLine(i,"08 ")
	elif i[0] == "JUMPM":
		createLine(i,"LOOP ")
	elif i[0] == "JUMP+M":
		createLine(i,"IFLOOP ")
	elif i[0] == "STORM_E":
		createLine(i,"12 ")
	elif i[0] == "STORM_D":
		createLine(i,"13 ")
	else:
		continue


# for i in code:
# 	print (i[0] + i[1] + i[2] + i[3] + i[4])

# print ("")
# for i in var:
# 	print (i[0] + i[1])	

# print ("")
# for i in points:
# 	print (i)

# print ("")
# for i in toPoints:
# 	print (i)


final = code + var

# for i in final:
# 	print (i)

for i in toPoints:
	aux = 0
	for j in points:
		if j[0] == i[0][2:].lower():
			aux = j
	for j in final:
		if j[0][0:3] == i[1]:
			if i[2]: #instrução do loop está na direita
				if aux[2]: #destino do loop esta na direita
					if j[3][0:2] == "IF": 
						j[3] = "10 " #JUMP+M Direita
					else:
						j[3] = "0E " #JUMP M direita
				else: #destino do loop esta na esquerda
					if j[3][0:2] == "IF": 
						j[3] = "0F " #JUMP+M Esquerda
					else:
						j[3] = "0D " #JUMP M Esquerda
				j[4] = aux[1] #memoria do destino do loop
			else: #instrução do loop está na direita
				if aux[2]: #destino do loop esta na direita
					if j[1][0:2] == "IF": 
						j[1] = "10 " #JUMP+M Direita
					else:
						j[1] = "0E " #JUMP M direita
				else:  #destino do loop esta na esquerda
					if j[1][0:2] == "IF": 
						j[1] = "0F " #JUMP+M Esquerda
					else:
						j[1] = "0D " #JUMP M Esquerda
				j[2] = aux[1] #memoria do destino do loop	



# gera arquivo final
saida = open("ra.hex", "w+")

for i in final:
	aux = ""
	for j in i:
		aux += str(j)
	saida.write(aux + '\n')


