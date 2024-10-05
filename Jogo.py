import pygame
from random import randint, choice 

from random import randint

def criaBola():

    posx = randint(50, 850)
    posy = randint(50, 450)
   
    novaBola = {
        "cor" : (randint(0, 255), randint(0, 255), randint(0, 255)),
        "velocidade" : randint(50,250),
        "posicao" : pygame.Vector2(posx, posy),
        "direcao" : pygame.Vector2(choice([-1, 1]), choice([-1, 1])),
        "tamanho" : randint(25, 70)
    }

    return novaBola

def desenhaBolas(listaBolas):
    for bola in listaBolas:
        pygame.draw.circle(tela, bola["cor"], bola["posicao"], bola["tamanho"])



def animaBolas(listaBolas):
    for bola in listaBolas:
        bola["posicao"].y += bola["velocidade"] * bola["direcao"].y * dt
        bola["posicao"].x += bola["velocidade"] * bola["direcao"].x * dt

        if bola["posicao"].y >= (tamanho[1] - bola["tamanho"]) or bola["posicao"].y <= (0 + bola["tamanho"]):
            bola["direcao"].y *= -1

        if bola["posicao"].x >= (tamanho[0] - bola["tamanho"]) or bola["posicao"].x <= (0 + bola["tamanho"]):
            bola["direcao"].x *= -1



# iniciar o pygame 

tamanho = (900, 500)
#criar uma tele com  tamanho especifico 
tela = pygame.display.set_mode(tamanho)

#define o titulo do jogo
pygame.display.set_caption("hello mundo")

#define um relogio para controlar o fps
relogio = pygame.time.Clock()

posicaoBola = pygame.Vector2(100, 100)
listaBolas = []
dt = 0 

# listaBolas.append(criaBola())
# listaBolas.append(criaBola())
# listaBolas.append(criaBola())
# listaBolas.append(criaBola())
# listaBolas.append(criaBola())
# listaBolas.append(criaBola())
# listaBolas.append(criaBola())
# listaBolas.append(criaBola())

# criar um evento

adicionaBola = pygame.USEREVENT + 1

#define um timer para acionar o addbolas
pygame.type.set_timer()




# direçaoY = 1
# direçaoX = 1
while True:
    #lida com os eventos da aplicaçao
    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            pygame.quit() # fechamento do pygame 

    # preenche a tela com uma cor
    tela.fill((0, 0, 125))



    desenhaBolas(listaBolas)
    animaBolas(listaBolas)


    # desenha circulo na tela
    # pygame.draw.circle(tela, (46, 234, 70), posicaoBola, 24, 10)

   

    # posicaoBola.y += 300 * direçaoY * dt
    # posicaoBola.x += 300 * dt * direçaoX

    


    # Atualiza a tela 
    pygame.display.update()
    dt = relogio.tick(60) / 1000  # define quantidade de fps

    relogio.tick(60) # define a quantidade de fps

#     if posicaoBola.y >= 475 or posicaoBola.y <= 25:
#         direçaoY *= -1 
        
#     if posicaoBola.x >= 875 or posicaoBola.x <= 25:
#         direçaoX *= -1   
# #


    

