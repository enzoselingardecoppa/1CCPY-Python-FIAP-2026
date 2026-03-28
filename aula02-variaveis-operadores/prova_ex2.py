
Nome = input("Digite o nome do colaborador: ")
ValorH = float(input('Digite o valor da hora trabalhada: '))
Horas = int(input('Digite a quantidade de horas trabalhadas: '))
Bonus = float(input("Digite o valor do bonus mensal: "))
Desconto = float(input("Digite o valor do desconto: "))
salarioB = ((ValorH*Horas) + Bonus)
salarioL = (salarioB - Desconto)

print(f'Colaborador: {Nome}')
print(f"Salário Bruto: {salarioB}R$")
print(f"Salário Líquido:{salarioL}R$")