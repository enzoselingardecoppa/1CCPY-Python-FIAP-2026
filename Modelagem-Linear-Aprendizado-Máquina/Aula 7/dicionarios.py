eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'


eng2sp = {
    "one": "uno",
    "two": "dos"

}
print(eng2sp)
print(len(eng2sp))

valores = eng2sp.values()
print()


print('dos' in valores)
print()



print()

def count_letters(s):
    d =dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

dict_contagem = count_letters("Paralelepipedo")
print(dict_contagem)

print()

personagens = [
    {
        "Nome": "Rick",
        "idade": 70,
        "hobbies": ["Xingar", "beber", "comer planetas"]
    },
    {
        "Nome": "Morty",
        "idade": 14,
        "hobbies": ["Jessica", "minecraft",]
    }
]

for personagem in personagens:
    nome = personagem["Nome"]
    idade = personagem["idade"]

    for key, value in personagem.items():
        print(f"{key}: {value}")
print()