numero = int(input("digite um numero inteiro: "))
for ex in range(1, numero+1, 1):
    if numero % ex == 0:
        print(ex)