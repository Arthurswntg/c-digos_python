Lanchonete = {
    "Salgado":4.90,
    "Suco":3.00,
    "Refrigerante":4.00,
    "Hamburguer":7.20,
    "Doce":2.00
    }


print("="*40)
print(f"{'Cardápio':^40}")
print("="*40)

for produto, preco in Lanchonete.items():
    print(f"{produto:.<30}R${preco:>5}")

print("="*40)