while True:
    num = float(input("Digite um valor qualquer: "))

    if(num > 10 and num <= 100):
        print("O quadrado de {} é: {}".format(num, num**2))

    elif(num <= 10 and num > 5):
        print("O cubo de {} é: {}".format(num, num**3))

    elif(num > 100):
        print("Limite excedido")

    elif(num < 0):

        break

print("programa finalizado")

