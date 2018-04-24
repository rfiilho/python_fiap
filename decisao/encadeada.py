nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca=input("O paciente possui doença infectocontagiosa? ").upper()
if idade >= 65:
    print("O paciente possui atendimento prioritário")
    if doenca == "SIM":
        print("Encaminhe o paciente " + nome + " para a sala amarela.")
    elif doenca == "NAO":
        print("Encaminhe o paciente " + nome + " para a sala branca.")
    else:
        print("Responda com SIM ou NAO à doença infectocontagiosa")
else:
    print("O paciente não possui atendimento prioritário")
    if doenca == "SIM":
        print("Encaminhe o paciente " + nome + " para a sala amarela.")
    elif doenca == "NAO":
        print("Encaminhe o paciente " + nome + " para a sala branca.")
    else:
        print("Responda com SIM ou NAO à doença infectocontagiosa")