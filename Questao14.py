lista = []

for n in range(4):
    num = int(input("Insira o numero => "))
    lista.append(num)

lista.sort(reverse=True)

print(lista)
