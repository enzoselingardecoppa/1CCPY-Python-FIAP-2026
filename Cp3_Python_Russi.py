temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]
criticos = []
media = []

for sala in temperaturas:
    media.append(sum(sala)/ 4)

    contador = 0
    for temperatura in sala:
        if temperatura >= 33:
            contador += 1
    criticos.append(contador)

sala_critica = 0
for i in criticos:
    if i > sala_critica:
        sala_critica = i

for i in range(len(temperaturas)):
    print(f"Sala: {i+1}")
    print(f"Temp média: {media[i]}")
    print(f"Quantidade de registros críticos: {criticos[i]}")
    print()


print(f"A sala com mais risco é a sala {sala_critica}")