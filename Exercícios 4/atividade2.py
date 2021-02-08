cont = 0
while True:
    num = int(input("Informe um valor qualquer: "))

    if num == 0:
        
        break
    
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    

    cont = cont + 1


print("O maior valor é {} e o menor valor é {}".format(maior, menor))


    