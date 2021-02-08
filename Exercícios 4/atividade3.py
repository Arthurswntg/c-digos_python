
neg = 0

somaPos = 0
for i in range(1,11):
    val = int(input("Informe o valor número {}: ".format(i)))

    if(val % 2 == 0):

        somaPos = somaPos + val
        

    elif(val < 0):

        neg = neg + 1

print("\nA soma dos números positivos é {}".format(somaPos))


print("\nA quantidade de números negativos é {}".format(neg))