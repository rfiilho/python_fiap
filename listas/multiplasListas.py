equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar...").upper()

for atual in range(0, len(departamentos)):
    print("\nEquipamento..:", (atual+1))
    print("Nome.........:", equipamentos[atual])
    print("Valor........:", valores[atual])
    print("Serial.......:", seriais[atual])
    print("Departamento.:", departamentos[atual])

print("Total de equipamentos: ", len(equipamentos))