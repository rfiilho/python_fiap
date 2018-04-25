from PrimeiroProjeto.funcoes.identificacaoDeFuncoes import *

minhaLista = []

print("\nPreenchendo..")
preencherInventario(minhaLista)

print("\nExibindo")
exibirInventario(minhaLista)

print("\nPesquisando")
localizarPorNome(minhaLista)

print("\nDepreciando")
depreciarPorNome(minhaLista, 10)

print("\nExcluindo")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("Resumindo")
resumirValores(minhaLista)