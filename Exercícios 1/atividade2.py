sal = float(input("Informe o seu salário total: "))
hr_dia = int(input("Informe quantas horas trabalha por dia: "))

hr_mes = (hr_dia*24)

print("É recebido o salário de R$ {:.2f} por hora".format(sal/hr_mes))