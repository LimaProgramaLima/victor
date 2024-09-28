nomes = [] # Cria uma lista vazia
destinos = []
continua = "s"
while continua == "s":
    nome = input("qual o nome deseja cadastrar para vaijar?: ")
    nomes.append(nome) # Adiciona o nome na lista de nomess

    destino = input("qual sera o destido do passageiro?:")
    destinos.append(destino)

    continua = input("cadastrar outra pessoa? (s/n): ")
   
   
for i in range(len(nomes)):
    print(f"{i + 1} - {nomes[i]} - {destinos[i]}")



# Imprime os nomes da lista que o usuário digitou
# for nome in nomes:
#     print(f"O nome da vez é: {nome}")
