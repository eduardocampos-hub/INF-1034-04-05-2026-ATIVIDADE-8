import pygame
from pygame import *

# Fazendo sistema de email senha e login.
def valida_email(email):
    return email[-8:] == '@puc.com'

def maiuscula(senha):
    for carac in senha:
        if 'A'<= carac <= 'Z':
            return True
    return False

def minuscula(senha):
    for carac in senha:
        if 'a'<= carac <= 'z':
            return True
    return False

def numero(senha):
    for carac in senha:
        if carac.isnumeric():
            return True
    return False

def criptografa(senha):
    senha_cripto = ""
    for carac in senha:
        if carac.isalpha():
            pos_alpha = ord(carac) - ord('a')
            pos_alpha = (pos_alpha + 3) % 26
            pos_ascii = pos_alpha + ord('a')
            senha_cripto += chr(pos_ascii)
    return senha_cripto

def valida_senha(senha):
    if len(senha) < 8:
        return False
    if not maiuscula(senha):
        return False
    if not minuscula(senha):
        return False
    if not numero(senha):
        return False
    return True

# Comeco Pygame:
pygame.init()

screen = pygame.display.set_mode((1280, 720))
running = True
clock = time.Clock()

# Definicao de variaveis
input_senha = ''
input_email = ''
mensagem = ''
cor_mensagem = 'red'
##### CASINHA ########
estagio = 0
pos_x = 300
pos_y = 150
background_color = "#97D1FA"
texto = "I am ARROZ!"
movimento_com_mouse = False  

#imagem
arroz_img = image.load("arroz.png")
arroz_img = transform.scale(arroz_img,(50,50))

#texto
arroz_font = font.Font("LoveDays-2v7Oe.ttf", 30)
arroz_text = arroz_font.render(texto, True, (255,222,234))

#musica
mixer_music.load("Luan santana - Chuva De Arroz (Luan Santana Acústico - Vídeo Oficial) - Luan Santana (128k).mp3")
mixer_music.play(-1)
music = mixer.Sound("Luan santana - Chuva De Arroz (Luan Santana Acústico - Vídeo Oficial) - Luan Santana (128k).mp3")
music.set_volume(0.1)

#margem 
margem_esquerda = 10
margem_direita = 1050 
margem_topo = 50
margem_base = 720 - 50

#nuvem andando
nuvem_x = 200
velocidade = 2

### Mudanca de tela ###
tela_atual = 'email'
fonte = pygame.font.Font(size=50)
fonte_validation = pygame.font.Font(size=25)
fonte_titulo = pygame.font.Font(size=35)

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                key_pressed = event.key
                movimento_com_mouse = not movimento_com_mouse
            if event.key == pygame.K_BACKSPACE:
                key_pressed = event.key
                if tela_atual == 'email':
                    input_email = input_email[:-1]
                elif tela_atual == 'senha':
                    input_senha = input_senha[:-1]
            elif event.key == pygame.K_RETURN:
                if tela_atual == 'email':
                    if valida_email(input_email):
                        tela_atual = 'senha'
                        mensagem = ''
                    else:
                        mensagem = 'Email incorreto, tente novamente'
                        cor_mensagem ='red'
                elif tela_atual == 'senha':
                    if valida_senha(input_senha):
                        mensagem = 'Senha correta!'
                        cor_mensagem = 'green'
                        tela_atual = 'casinha'
                    else:
                        mensagem = 'Senha incorreta ou fraca, tente novamente.'
                        cor_mensagem = 'red'
            else:
                if tela_atual == 'email':
                    input_email += event.unicode
                if tela_atual == 'senha':
                    input_senha += event.unicode
    # Inicio desenho ==============================================================
    screen.fill('white')

    if tela_atual == 'email':
        titulo = fonte_titulo.render("Digite seu E-mail:", True, "black")
        screen.blit(titulo,(100,40))

        pygame.draw.rect(screen,'black',(100,100,500,50),3)
        input_text = fonte.render(input_email,True,'black')
        screen.blit(input_text,(120,105))
    if tela_atual == 'senha':
        titulo = fonte_titulo.render("Digite sua senha:", True, "black")
        screen.blit(titulo,(100,40))

        pygame.draw.rect(screen,'black',(100,100,500,50),3)
        input_text = fonte.render(input_senha,True,'black')
        screen.blit(input_text,(120,105))
    if tela_atual == 'casinha':
        screen.fill(background_color)

            ## Update
        dt = clock.get_time()/1000
        keys = pygame.key.get_pressed()
        
        # AÇÕES CONTÍNUAS - Movimento condicional
        if not movimento_com_mouse:
            # Movimento com teclado (WASD)
            if keys[K_d]:
                pos_x = pos_x + 300 * dt
            elif keys[K_a]:
                pos_x = pos_x - 300 * dt
            elif keys[K_w]:
                pos_y = pos_y - 300 * dt
            elif keys[K_s]:
                pos_y = pos_y + 300 * dt
        else:
            # Movimento com mouse
            mouse_x, mouse_y = mouse.get_pos()
            pos_x = mouse_x
            pos_y = mouse_y
        # Movimento da nuvem com margens
        if nuvem_x > margem_direita:
            velocidade = -2
        if nuvem_x < margem_esquerda: 
            velocidade = 2
        nuvem_x += velocidade


        if pos_x < 400:
            background_color = "#97D1FA"
        elif pos_x < 800:
            background_color = "#F2883B"    
        else:
            background_color = "#0D1664"
        # Chão
        draw.rect(screen, (34, 139, 34), (0, 600, 1280, 120)) 

        # Casa
        draw.rect(screen, (169, 169, 169), (500, 400, 300, 200))

        # Telhado
        draw.polygon(screen, (139, 69, 19), [(500, 400), (650, 250), (800, 400)]) 

        # Porta
        draw.rect(screen, (100, 50, 0), (620, 500, 60, 100))  

        # Janela
        draw.rect(screen, (68, 161, 219), (530, 480, 50, 50))  

        # sol
        draw.circle(screen, (255, 255,0),(pos_x,pos_y),50)



        #Macaneta
        draw.circle(screen,(255,215,0),(670,550),7)



        # Árvore
        draw.rect(screen, (139, 69, 19), (900, 500, 30, 120))  
        draw.circle(screen, (34, 139, 34), (915, 470), 80)  

        # Arroz
        screen.blit(arroz_img,(1010, 390))

        #desenhar texto:
        screen.blit(arroz_text,(750, 650))

        # Oito linhas em volta do sol
        draw.line(screen, (255, 255, 0), (pos_x, pos_y - 50), (pos_x, pos_y - 110), 7)   
        draw.line(screen, (255, 255, 0), (pos_x, pos_y + 50), (pos_x, pos_y + 110), 7) 
        draw.line(screen, (255, 255, 0), (pos_x - 50, pos_y), (pos_x - 100, pos_y), 7)  
        draw.line(screen, (255, 255, 0), (pos_x + 50, pos_y), (pos_x + 100, pos_y), 7) 
        draw.line(screen, (255, 255, 0), (pos_x - 36, pos_y - 36), (pos_x - 78, pos_y - 78), 7)  
        draw.line(screen, (255, 255, 0), (pos_x + 36, pos_y - 36), (pos_x + 78, pos_y - 78), 7)  
        draw.line(screen, (255, 255, 0), (pos_x - 36, pos_y + 36), (pos_x - 78, pos_y + 78), 7) 
        draw.line(screen, (255, 255, 0), (pos_x + 36, pos_y + 36), (pos_x + 78, pos_y + 78), 7)

        #nuvem
        draw.circle(screen,(255, 255, 255), (nuvem_x, 100), 50)
        draw.circle(screen,(255, 255, 255), (nuvem_x + 65, 100), 50)
        draw.circle(screen,(255, 255, 255), (nuvem_x + 130, 100), 50)
        draw.circle(screen,(255, 255, 255), (nuvem_x + 195, 100), 50)

        music.play()
    if mensagem != '':
        text_msg = fonte_validation.render(mensagem, True, cor_mensagem)
        screen.blit(text_msg,(100,180))
    pygame.display.update()
pygame.quit()
