resposta="SIM"
while resposta == "SIM":
    usuario = input("Digite o nível: ").upper()

    if usuario == "ADM":
        sexo = input("Digite o sexo: ").upper()
        if sexo == "MASCULINO":
            print("Olá, Administrador")
        elif sexo == "FEMININO":
            print("Olá, Administradora")
        else:
            print("Olá, Administrador(a)")
    elif usuario == "USR":
        sexo = input("Digite o sexo: ").upper()
        if sexo == "MASCULINO":
            print("Olá, Usuário")
        elif sexo == "FEMININO":
            print("Olá, Usuária")
        else:
            print("Olá, Usuário(a)")
    elif usuario == "GUEST":
        sexo = input("Digite o sexo: ").upper()
        if sexo == "MASCULINO":
            print("Olá, Convidado")
        elif sexo == "FEMININO":
            print("Olá, Convidada")
        else:
            print("Olá, Convidado(a)")
    else:
        print("Olá, Estranho(a)")
    resposta = input("Digite SIM para continuar...: ").upper()