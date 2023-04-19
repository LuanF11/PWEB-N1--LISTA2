lista = []

for n in range(4):
    num = int(input("Insira o numero => "))
    lista.append(num)


media = sum(lista) / len(lista)

print("A media e {}".format(media))
