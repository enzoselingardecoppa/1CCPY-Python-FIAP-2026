idade = 20

maior_idade = idade >= 18
print(maior_idade)

if maior_idade:
    print("Maior de idade")


#operadores lógicos
#AND, OR, NOT
verifica_email = False
verifica_senha = True
Login = verifica_email and verifica_senha
print(Login)

if not Login:
    print("Tu é burro hein, tente novamente")

#notas
print()
nota_final = 10

if nota_final <4:
    print('Reprovado')
elif nota_final <6:
    print("Recuperação")
else:
    print("Aprovado")


print("FIM")