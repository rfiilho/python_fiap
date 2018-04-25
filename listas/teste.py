lista1 = []

usuario = [input("Nome: "), int(input("Idade: ")),input("Cargo: ")]

lista1.append(usuario)

for cadaum in lista1:
    print("\n")
    print(cadaum[0])
    print(cadaum[1])
    print(cadaum[2])
