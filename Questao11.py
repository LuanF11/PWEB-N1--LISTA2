lista = []

for n in range(4):
    num = int(input("Insira o numero => "))
    lista.append(num)

for n in range(len(lista)):
    if lista[n] % 2 != 0:
        print(lista[n])
