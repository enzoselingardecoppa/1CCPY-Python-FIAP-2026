num1 = int(input("digite um numero maior que 2: "))
if num1 >= 2:
    for ex in range(2, num1+1, 2):
        print(ex)
else:
    print("voce digitou um numero inteiro menor que 2")