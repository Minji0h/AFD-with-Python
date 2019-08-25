import random 

#Define uma variavel global para o numero binario

global numero_binario
global div, nn_div, numero

div = []
nn_div = []
#Faz a conversão do valor para binario

def ConverterBinario():
    global numero_binario, numero
    numero_binario = []
    for i in range(len(numero)):  
        loc = numero[i]  
        numro_binario = []
        while loc != 0:
            numro_binario.append(loc%2)
            loc = loc//2
        numero_binario.append(numro_binario[::-1])

#Q0: 
#N = 0 : Q0
#N = 1 : Q1

def Q0(pos, i):
    global div
    if(pos != len(numero_binario[i])):
        if(numero_binario[i][pos] == 0):
            Q0(pos+1,i)
        else:
            Q1(pos+1,i)
    else:
        div.append(numero[i])

#Q1: 
#N = 0 : Q2
#N = 1 : Q3

def Q1(pos, i):
    global nn_div
    if(pos != len(numero_binario[i])):
        if(numero_binario[i][pos] == 0):
            Q2(pos+1,i)
        else:
            Q3(pos+1,i)
    else:
        nn_div.append(numero[i])

#Q2: 
#N = 0 : 
#N = 1 : Q0

def Q2(pos, i):
    global nn_div
    if(pos != len(numero_binario[i])):
        if(numero_binario[i][pos] == 0):
            Q4(pos+1,i)
        else:
            Q0(pos+1,i)
    else:
        nn_div.append(numero[i])

#Q3: 
#N = 0 : Q4
#N = 1 : Q1

def Q3(pos, i):
    global nn_div
    if(pos != len(numero_binario[i])):
        if(numero_binario[i][pos] == 0):
            Q1(pos+1,i)
        else:
            Q2(pos+1,i)
    else:
        nn_div.append(numero[i])

#Q4: 
#N = 0 : Q0
#N = 1 : Q130

def Q4(pos, i):
    global nn_div
    if(pos != len(numero_binario[i])):
        if(numero_binario[i][pos] == 0):
            Q3(pos+1,i)
        else:
            Q4(pos+1,i)
    else:
        nn_div.append(numero[i])

#Recebe o valor

def RecebeValor(qtd):
    global numero_binario, numero
    numero = []
    for i in range(qtd):
        numero.append(random.randint(0,1000))
    print(numero)
    ConverterBinario()
    for i in range(len(numero_binario)):
        Q0(0,i)

#Inicio

def inicio():
    global div, nn_div
    cont = 1
    while cont == 1:
        qtd = int(input("Digite a quantidade de valores"))
        RecebeValor(qtd)
        print("Valores divisiveis: " + str(div) + "\nValores não divisiveis: " + str(nn_div))
        cont = int(input("Deseja continuar? 1 - Sim 2 - Não"))
        

inicio()
