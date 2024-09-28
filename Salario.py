nome = input ("digite teu nome cretino: ")

anos = float(input("quatos anos de empresa? "))

salario = float(input("qual é seu salario atual?"))

print(f"ola {nome} devido ao seu tempo de empresa seu salario atual é de: R$", end="")



bonus = salario + salario * 0.05


if anos > 5: 
   print(bonus)
   print("parabens pelo bonus")
   print(f"ola {nome} devido ao seu tempo de empresa seu salario atual é de: R$", end="")
   print("ce é cagado mesmo em ")
else:
    print(salario)
    print("vai trabalha pobre quer aumento pra que miseral ")



