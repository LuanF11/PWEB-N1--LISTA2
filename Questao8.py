lista = []

for n in range(4):
    num = int(input("Insira o numero => "))
    lista.append(num)

print("O maior numero da lista e {} e o menor e {}".format(max(lista), min(lista)))
