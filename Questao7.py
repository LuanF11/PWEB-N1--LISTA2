def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


num = int(input("Insira o numero => "))

for n in range(num):
    print(fibonacci(n))
