prod1 = float(input("digite o preço do primeiro produto: R$ "))
prod2 = float(input("digite o preço do segundo produto: R$ "))
prod3 = float(input("digite o preço do terceiro produto: R$ "))

tot = (prod1 + prod2 + prod3)

desc = (tot*0.2)

valor = tot - desc

print("O total das compras foi R$ {}\nO desconto foi de R$ {}\nO cliente deve pagar R$ {}".format(tot, desc, valor))

