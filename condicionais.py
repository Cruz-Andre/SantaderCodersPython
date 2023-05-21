# Estruturas condicionais

idade = 20

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Vocé é menor de idade")


"""
    Imagine que você queira imprimir "Aprovado(a)", caso o estudante tenha uma média 
    superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7.
"""

media = float(input("Digite sua média: "))
if media >= 7:
    print("Você foi aprovado(a)")
elif media >= 5: # o else if abreviado
    print("Vocé está de recuperação")
else:
    print("Vocé foi reprovado(a)")


media2 = 10
presenca = 100
if media2 >= 7 and presenca >= 70:
    print("Você foi aprovado(a)")
else:
    print("Você foi reprovado(a)")