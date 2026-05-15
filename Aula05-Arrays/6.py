n = int(input('Digite um número maior que 0: '))
while n <= 0:
    print("Numero invalido")
    n = int(input('Digite um número maior que 0: '))

lista = []
for i in range(n):
    c1 = input("Digite um caractere: ")
    while len(c1) != 1:
        print("Caractere invalido")
        c1 = (input('Digite apenas um caractere: '))

    lista.append(c1)
for i in range(len(lista)//2):

    temp = lista[i]
    lista[i] = lista[len(lista)-1-i]
    lista[len(lista)-1-i] = temp

print(lista)

