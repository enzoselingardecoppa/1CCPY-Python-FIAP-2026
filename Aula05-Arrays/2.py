n = int(input('Digite o numero de alunos da turma: '))
while n <= 0:
    print("Numero invalido")
    n = int(input('Digite o numero de alunos da turma: '))


notas = []

for i in range(n):
    nota = int(input('Digite a nota: '))
    notas.append(nota)
soma = 0
for num in notas:
    soma = num + soma

media = soma / n

acima = 0
abaixo = 0
iguais = 0

for num in notas:
    if num > media:
        acima = acima + 1
    elif num < media:
        abaixo = abaixo + 1
    else:
        iguais = iguais + 1

print(f'média = {media} notas acima da média = {acima} notas abaixo da média = {abaixo} notas na média = {iguais}')
