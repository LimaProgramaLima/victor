nome = input ("digite teu nome cretino: ")

nota = float(input("qual sua nota:"))

print(f"ola {nome} sua nota é: ", end="")

if nota >= 90:
    print("A")
elif nota  >=80: 
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
elif nota <= 60 :
    print("F")