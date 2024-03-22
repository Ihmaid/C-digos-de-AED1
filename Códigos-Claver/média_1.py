núm_somandos = 6
soma = 0

for i in range(núm_somandos):
    núm = float(input("Escreva o "+str(i+1)+chr(176)+" número: "))
    soma += núm

média = soma/núm_somandos
print("A média dos " + str(núm_somandos) + " somandos é: "+ str(round(média,2))) 
    
