num1 = int(input('Escolha o primeiro numero: '))
num2 = int(input('Escolha o segundo numero: '))
And = num1 & num2
Or = num1 | num2

print(''' Escolha:
[1] And
[2] Or''')
while True:
    escolha = int(input('Sua Escolha: '))
    if escolha == 1:
        print(And)
        print(f'Em binário', bin(And))
    elif escolha == 2:
        print(Or)
        print(f'Em binário', bin(Or))
        break
    print("Tente novamente")

