# 1.  Verificação de idade
#Crie um programa que peça ao usuário para inserir sua idade e, em
# seguida, informe se a pessoa é menor de idade ou maior de idade.

idade = float(input("qual sua idade:"))

print("ola voce é: ", end="")

if idade < 4:
    print("bebe")
elif idade < 12: 
    print("criança")
elif idade <= 17:
    print("adolecente")
elif idade >= 18:
    print("adulto")
elif idade >= 65:
    print("velho")

