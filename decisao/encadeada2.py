nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca=input("O paciente possui doença infectocontagiosa? ").upper()

if doenca == "SIM":
    print("Encaminhe o paciente para a sala amarela.")
elif doenca == "NAO":
    print("Encaminhe o paciente para a sala branca.")
else:
    print("Responda com SIM ou NAO à doença infectocontagiosa.")


if idade >= 65:
    print("O paciente possui atendimento prioritário.")
else:
    sexo = input("Digite o sexo?").upper()
    if sexo == "FEMININO" and idade>10:
        gravidez=input("A paciente está grávida?").upper()
        if gravidez == "SIM":
            print("O paciente possui atendimento prioritário.")
        else:
            print("O paciente não possui atendimento prioritário.")
    else:
        print("O paciente não possui atendimento prioritário.")