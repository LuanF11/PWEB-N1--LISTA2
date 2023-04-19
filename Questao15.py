lista = []

for n in range(4):
    num = int(input("Insira o numero => "))
    lista.append(num)

x = int(input("Insira o numero para verificar se existe na lista=> "))

if lista.count(x):
    print("O numero {} existe na lista".format(x))
else:
    print("O numero {} não existe na lista".format(x))
