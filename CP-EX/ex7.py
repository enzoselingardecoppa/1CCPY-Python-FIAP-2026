numero = int(input("digite um numero inteiro: "))
soma = 0
if  numero > 0:
    for ex in range(1, numero+1, 1):
        soma = soma + ex
    print(f'A soma de 1 até {numero} é: {soma}')
else:
    print('Digite um número positivo')