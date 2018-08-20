# MontadorIAS
Script simples para gerar código hexadecimal de IAS

# Variaveis
varExemplo.1234  
  cria varExemplo com valor 1234  
OBS: Valor da variavel tem que ser em hexadecimal  

# Instruções:

LOAD M(X) -> LOADM.X  
LOAD MQ,M(X) -> LOADADMQM.X  
STOR M(X) -> STORM.X.toChange#  
LOAD MQ -> LOADMQ  
ADD M(X) -> ADDM.X  
SUB M(X) -> SUBM.X  
MUL M(X) -> MULM  
DIV M(X) -> DIVM  
RSH -> RSH  
LSH -> LSH  
LOAD |M(X)| -> LOADM_ABS.X  
LOAD -M(X) -> LOAD-M.X  
ADD |M(X)| -> ADDM_ABS.X  
SUB |M(X)| -> SUBM_ABS.X  
JUMP M(X) -> JUMPM.X.toPoint#  
JUMP+ M(X) -> JUMP+M.X.toPoint#  
STOR M(X) -> STORM.X.toChange#  

# JUMP M, JUMP+M, STOR M

exemplo de loop:  
    
  003 LOAD M(X) ADD M(X)  
  004 JUMP M(003,20:39)   
      
  LOADM.x.point1 ADDM.X  
  JUMPM.x.toPoint1  
