n = int(input('Digite o tamanho da lista '))
while n <= 0:
    print("Numero invalido")
    n = int(input('Digite o tamanho da lista '))

lista = []

for i in range(n):
    n2 = int(input('Digite numero inteiro '))
    lista.append(n2)
soma = 0
for num in lista:
    soma += num

print(soma)