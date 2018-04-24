#inventário

inventario = []
resposta = "S"

while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digita \"S\" para continuar...").upper()

for objeto in inventario:
    print(objeto)