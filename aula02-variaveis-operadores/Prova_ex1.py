
produto = input("Digite seu produto: ")
preco = int(input('Digite o valor do seu produto: '))
quantidade = int(input("Quantos vc quer comprar: "))
percentual = float(input("Digite a porcentagem de desconto: "))
desconto_total = (preco * quantidade) * (percentual / 100)
preco_final = (preco * quantidade) - desconto_total

print(produto)
print(preco)
print(percentual)
print(preco_final)