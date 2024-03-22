núm_somandos = 6
lista_núms = []

for i in range(núm_somandos):
    núm = float(input("Escreva o "+str(i+1)+chr(176)+" número: "))
    lista_núms.append(núm)

média = sum(lista_núms)/núm_somandos
print("A média dos " + str(núm_somandos) + " somandos é: "+ str(round(média,2))) 
    
