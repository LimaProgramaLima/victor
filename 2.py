nome = input ("digite teu nome: ")

peso = float(input("digite teu peso: "))
altura = float(input("digite tua altura: "))

print("-"*20)

print("Olá,", nome)
print("seu peso é:", peso)
print("sua altura é:", altura)


imc =  peso / (pow)(altura, 2)

print(f"imc: {imc:.2f}",)
print("-"*20)

