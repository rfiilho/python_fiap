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


pergunta = "S"
while pergunta == "S":
    pesquisa = input("\nDigita o nome do equipamento que deseja buscar: ")

    for atual in range(0, len(seriais)):
        if pesquisa== equipamentos[atual]:
            print("Valor........:", valores[atual])
            print("Serial.......:", seriais[atual])
            print("Departamento.:", departamentos[atual])
            pergunta = input("Digita \"S\" para procurar outro equipamento: ").upper()