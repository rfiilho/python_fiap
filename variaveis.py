nome =input("Digite um funcionario: ")
empresa = input("Digite a instituicao: ")
qtde_funcionarios = int(input("Digite Qtde Funcionarios: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))
print(nome + " trabalha na empresa " + empresa)
print("Possui ", qtde_funcionarios, " funcionários")
print("A média da mensalidade é de: " + str(mediaMensalidade))
print("======== Verifique os tipos de dados abaixo ===========")
print("O tipo de dado da variavel [nome] é: ", type(nome))
print("O tipo de dado da variavel [empresa] é: ", type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ", type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ", type(mediaMensalidade))