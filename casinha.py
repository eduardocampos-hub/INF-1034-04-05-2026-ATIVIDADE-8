from pygame import *
import sys
init()

window = display.set_mode((1280,720))
running = True
clock = time.Clock()

## Definição de variáveis
estagio = 0
pos_x = 300
pos_y = 150
background_color = "#97D1FA"
texto = "I am ARROZ!"
movimento_com_mouse = False  # Controla se o sol se move com mouse (True) ou teclado (False)

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
nuvem_x = 400
velocidade = 2

while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        
        if ev.type == MOUSEBUTTONUP:
            if ev.button == 1:
                texto = "I said I AM ARROZ!"
            elif ev.button == 3:
                texto = "I AM ARROZ!"
        
        # AÇÕES INSTANTÂNEAS
        if ev.type == KEYDOWN:
            key_pressed = ev.key
            # Tecla G para alternar entre movimento com teclado e mouse
            if key_pressed == K_g:
                movimento_com_mouse = not movimento_com_mouse
    # #desenhar a partir daqui
     # NUVEM ANDANDO
    window.fill(background_color)

        ## Update
    dt = clock.get_time()/1000
    keys = key.get_pressed()
    
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
    draw.rect(window, (34, 139, 34), (0, 600, 1280, 120)) 

    # Casa
    draw.rect(window, (169, 169, 169), (500, 400, 300, 200))

    # Telhado
    draw.polygon(window, (139, 69, 19), [(500, 400), (650, 250), (800, 400)]) 

    # Porta
    draw.rect(window, (100, 50, 0), (620, 500, 60, 100))  

    # Janela
    draw.rect(window, (68, 161, 219), (530, 480, 50, 50))  

    # sol
    draw.circle(window, (255, 255,0),(pos_x,pos_y),50)



    #Macaneta
    draw.circle(window,(255,215,0),(670,550),7)



    # Árvore
    draw.rect(window, (139, 69, 19), (900, 500, 30, 120))  
    draw.circle(window, (34, 139, 34), (915, 470), 80)  

    # Arroz
    window.blit(arroz_img,(1010, 390))

    #desenhar texto:
    window.blit(arroz_text,(750, 650))

    # Oito linhas em volta do sol
    draw.line(window, (255, 255, 0), (pos_x, pos_y - 50), (pos_x, pos_y - 110), 7)   
    draw.line(window, (255, 255, 0), (pos_x, pos_y + 50), (pos_x, pos_y + 110), 7) 
    draw.line(window, (255, 255, 0), (pos_x - 50, pos_y), (pos_x - 100, pos_y), 7)  
    draw.line(window, (255, 255, 0), (pos_x + 50, pos_y), (pos_x + 100, pos_y), 7) 
    draw.line(window, (255, 255, 0), (pos_x - 36, pos_y - 36), (pos_x - 78, pos_y - 78), 7)  
    draw.line(window, (255, 255, 0), (pos_x + 36, pos_y - 36), (pos_x + 78, pos_y - 78), 7)  
    draw.line(window, (255, 255, 0), (pos_x - 36, pos_y + 36), (pos_x - 78, pos_y + 78), 7) 
    draw.line(window, (255, 255, 0), (pos_x + 36, pos_y + 36), (pos_x + 78, pos_y + 78), 7)

    #nuvem
    draw.circle(window,(255, 255, 255), (nuvem_x, 100), 50)
    draw.circle(window,(255, 255, 255), (nuvem_x + 65, 100), 50)
    draw.circle(window,(255, 255, 255), (nuvem_x + 130, 100), 50)
    draw.circle(window,(255, 255, 255), (nuvem_x + 195, 100), 50)

    music.play()
    display.update()