numero = float(input("Me informe o primeiro numero>?"))
               
numero1 = float(input("Me informe o segundo numero?"))

operaçao = input("Me informe a operaçao?")

print("seu resultado é" )

if  operaçao == "+":
    print(f" {numero + numero1} ")

elif  operaçao == "-":
    print(f" {numero - numero1} ") 

elif  operaçao == "*":
    print(f" {numero * numero1} ")

elif  operaçao == "/":
    print(f" {numero / numero1} ")