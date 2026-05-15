import  random

n = int(input('Digite um número maior que 0: '))
while n <= 0:
    print("Numero invalido")
    n = int(input('Digite um número maior que 0: '))

lista = []

for i in range(n):
    numero = random.uniform(0, 100)
    lista.append(numero)

for num in lista:
    print(num)
