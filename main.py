import pygame

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

input_senha = ''
input_email = ''
mensagem = ''
cor_mensagem = 'red'

# Mudanca de tela
tela_atual = 'email'
fonte = pygame.font.Font(size=50)
fonte_validation = pygame.font.Font(size=25)
fonte_titulo = pygame.font.Font(size=35)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
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
        
    if mensagem != '':
        text_msg = fonte_validation.render(mensagem, True, cor_mensagem)
        screen.blit(text_msg,(100,180))
    pygame.display.update()
pygame.quit()
