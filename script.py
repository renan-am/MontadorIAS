#variaveis globais para usar nas funções
pos = False
codePos = 0
auxVar = []
code = []

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
def createCode( i, hex ):
	global pos
	global codePos
	global auxVar
	global code
	if pos:
		code[codePos] += hex + read(i,1)
		codePos += 1
		pos = not pos
	else:	
		code.append( hex + read(i,1) + " ")
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
	elif i[0] == "JUMPM_E":
		continue
	elif i[0] == "JUMPM_D":
		continue
	elif i[0] == "JUMP+M_E":
		continue
	elif i[0] == "JUMP+M_D":
		continue
	elif i[0] == "STORM_E":
		continue
	elif i[0] == "STORM_D":
		continue
	else:
		auxVar.append(i)

#memCount começa a contagem de espaço de memorias utilizados
memCount = 0
var = []

# salva em var as linhas de código pronta, com o endereço e valor da memória de cada variavel
# salva em auxVar o endereço de cada variavel
for i in auxVar:
	aux = hex(memCount)[2:] #converte em uma string hexadecimal, depois ignora os dois primeiros caracteres (0x)
	endVar = aux.zfill(3)   #zfill(x) coloca 0 a esquerda do valor da string, até ter x caracteres
	var.append(endVar + " " + i[1])
	i[1] = endVar
	memCount += 1

# salva em code as instruções e memorias relativas, em hexadecimal, com duas isntruções por linha, e variaveis substituidas por seus endereços
for i in vet:
	if i[0] == "LOADM":
		createCode(i,"01 ")
	elif i[0] == "LOADMQM":
		createCode(i,"09 ")
	elif i[0] == "STORM":
		createCode(i,"21 ")
	elif i[0] == "LOADMQ":
		createCode(i,"0A ")
	elif i[0] == "ADDM":
		createCode(i,"05 ")
	elif i[0] == "SUBM":
		createCode(i,"06 ")
	elif i[0] == "MULM":
		createCode(i,"0B ")
	elif i[0] == "DIVM":
		createCode(i,"0C ")
	elif i[0] == "RSH":
		createCode(i,"15 ")
	elif i[0] == "LSH":
		createCode(i,"14 ")
	elif i[0] == "LOADM_ABS":
		createCode(i,"03 ")
	elif i[0] == "LOAD-M":
		createCode(i,"02 ")
	elif i[0] == "ADDM_ABS":
		createCode(i,"07 ")
	elif i[0] == "SUBM_ABS":
		createCode(i,"08 ")
	elif i[0] == "JUMPM_E":
		createCode(i,"0D ")
	elif i[0] == "JUMPM_D":
		createCode(i,"0E ")
	elif i[0] == "JUMP+M_E":
		createCode(i,"0F ")
	elif i[0] == "JUMP+M_D":
		createCode(i,"10 ")
	elif i[0] == "STORM_E":
		createCode(i,"12 ")
	elif i[0] == "STORM_D":
		createCode(i,"13 ")
	else:
		continue


#salva em instr a linha de código completa, com o endereço de cada linha
instr= []
for i in code:
	aux = hex(memCount)[2:] 
	instr.append(aux.upper().zfill(3) + " " + i)
	memCount += 1

#concatena var e instr, final é um vetor onde cada elemento representa uma linha do código hexadecimal
final = var + instr


#gera arquivo final
saida = open("ra.hex", "w+")
for i in final:
	saida.write(i + '\n')


