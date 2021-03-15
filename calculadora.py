import pygame

pygame.init()

largura = 425
altura = 605

#  CORES
branco = (255, 255, 255)
preto = (0, 0, 0)
cinza21 = (54, 54, 54)
cinza11 = (28, 28, 28)
cinza31 = (79, 79, 79)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
cinza = (128, 128, 128)
prata = (192, 192, 192)
amarelo = (255, 255, 0)
fuchsia = (255, 0, 255)

#  CRIA A TELA DE EXIBIÇÃO
scren = pygame.display.set_mode((largura, altura))


class Botao:
    #  INICIALIZA O METODO CONSTRUTOR
    def __init__(self, pos_x, pos_y, tam_x, tam_y, cor, num):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tam_x = tam_x
        self.tam_y = tam_y
        self.cor = cor
        self.num = num

    #  FUNÇÃO PARA MOSTRAR O BOTÃO NA TELA
    def mostrar(self, tex_pos_x=0, tex_pos_y=0):

        global tela, op, sair, block

        #  VERIFICA E DEFINE A POSIÇÃO DO TEXTO
        if tex_pos_x == 0 and tex_pos_y == 0:
            tex_pos_x = self.pos_x + 30
            tex_pos_y = self.pos_y + 10
        else:
            tex_pos_x = self.pos_x + tex_pos_x
            tex_pos_y = self.pos_y + tex_pos_y

        #  DESENHA O BOTÃO
        pygame.draw.rect(scren, self.cor, [self.pos_x, self.pos_y, self.tam_x, self.tam_y])

        #  PEGA A POSIÇÃO X E Y DO MOUSE
        x1 = pygame.mouse.get_pos()[0]
        y1 = pygame.mouse.get_pos()[1]

        #  VERIFICA A POSIÇÃO DO MOUSE NO QUADRADO CORRESPONDENTE
        if self.pos_x < x1 < self.pos_x + self.tam_x and self.pos_y < y1 < self.pos_y + self.tam_y:

            #  MUDA A COR DO BOTÃO
            pygame.draw.rect(scren, cinza31, [self.pos_x, self.pos_y, self.tam_x, self.tam_y])

            #  DESENHA AS BORDAS DO BOTÃO QUANDO O CURSO ESTA EM CIMA
            pygame.draw.rect(scren, azul, [self.pos_x, self.pos_y, self.tam_x, 2])  # X SUPERIOR
            pygame.draw.rect(scren, azul, [self.pos_x, self.pos_y, 2, self.tam_y])  # Y DIREITO
            pygame.draw.rect(scren, azul, [self.pos_x, self.pos_y + self.tam_y - 2, self.tam_x, 2])  # X INFERIOR
            pygame.draw.rect(scren, azul, [self.pos_x + self.tam_x - 2, self.pos_y, 2, self.tam_y])  # Y ESQUERDO

        #  ESCREVE O NUMERO NA TELA
        font = pygame.font.SysFont('Arial', 70)
        texto = font.render(self.num, True, branco)
        scren.blit(texto, [tex_pos_x, tex_pos_y])


#  FUNÇÃO DE EXIBIÇÃO DOS VALORES NA TELA
def gui():

    global tela, op, block, num1, num2, total

    #  VERIFICA O TAMANHO DA 'TELA' E REDIMENSIONA
    tam_tela = len(tela) * 39

    #  BLOQUEIA A ENTRADA DE VALORES SE HOUVER 10 ITENS
    if len(tela) == 10:
        block = True

    #  VERIFICA SE É O PRIMEIRO VALOR QUE ESTA ENTRANDO
    if op == '':

        #   VERIFICA O TAMANHO DO TOTAL E MOSTRA NO MAXIMO DEZ ELEMNTOS
        if len(tela) >= 10:
            tela = tela[0:10]
            fonte_tela = pygame.font.SysFont('Arial', 70)
            txt_tela = fonte_tela.render(tela, True, branco)
            scren.blit(txt_tela, [420 - tam_tela, 10])
        else:
            #  CONFIGURA O TEXTO DA PRIMEIRA ENTRADA
            fonte_tela = pygame.font.SysFont('Arial', 70)
            txt_tela = fonte_tela.render(tela, True, branco)
            scren.blit(txt_tela, [420 - tam_tela, 10])
    else:

        #  CONFIGURA O TEXTO DA SEGUNDA ENTRADA
        fonte_tela_2 = pygame.font.SysFont('Arial', 40)
        txt_tela_2 = fonte_tela_2.render(tela, True, branco)
        scren.blit(txt_tela_2, [420 - (len(tela) * 22), 55])

        # CONFIGURA A EXIBIÇÃO DE TEXTO DA PRIMEIRA ENTRADA JUNTO COM A SEGUNDA
        fonte_num = pygame.font.SysFont('Arial', 40)
        txt_num = fonte_num.render(str(int(num1)), True, branco)
        scren.blit(txt_num, [420 - (len(str(int(num1))) * 24), 5])

        #  RETORNA NA TELA O TOTAL DA OPERAÇÃO
        if op != 'C' and op != '=':
            fonte_op = pygame.font.SysFont('Arial', 60)
            txt_op = fonte_op.render(op, True, branco)
            scren.blit(txt_op, [5, 10])


#  VERIFICA A POSIÇÃO DO MOUSE AO BOTÃO CORRESPONDENTE
def verificar(verificar_x, verificar_y):

    global tela, op, sair, block

    if b0.pos_x < verificar_x < b0.pos_x + b0.tam_x and b0.pos_y < verificar_y < b0.pos_y + b0.tam_y:
        if not block:
            tela += b0.num

    if b1.pos_x < verificar_x < b1.pos_x + b1.tam_x and b1.pos_y < verificar_y < b1.pos_y + b1.tam_y:
        if not block:
            tela += b1.num

    if b2.pos_x < verificar_x < b2.pos_x + b2.tam_x and b2.pos_y < verificar_y < b2.pos_y + b2.tam_y:
        if not block:
            tela += b2.num

    if b3.pos_x < verificar_x < b3.pos_x + b3.tam_x and b3.pos_y < verificar_y < b3.pos_y + b3.tam_y:
        if not block:
            tela += b3.num

    if b4.pos_x < verificar_x < b4.pos_x + b4.tam_x and b4.pos_y < verificar_y < b4.pos_y + b4.tam_y:
        if not block:
            tela += b4.num

    if b5.pos_x < verificar_x < b5.pos_x + b5.tam_x and b5.pos_y < verificar_y < b5.pos_y + b5.tam_y:
        if not block:
            tela += b5.num

    if b6.pos_x < verificar_x < b6.pos_x + b6.tam_x and b6.pos_y < verificar_y < b6.pos_y + b6.tam_y:
        if not block:
            tela += b6.num

    if b7.pos_x < verificar_x < b7.pos_x + b7.tam_x and b7.pos_y < verificar_y < b7.pos_y + b7.tam_y:
        if not block:
            tela += b7.num

    if b8.pos_x < verificar_x < b8.pos_x + b8.tam_y and b8.pos_y < verificar_y < b8.pos_y + b8.tam_y:
        if not block:
            tela += b8.num

    if b9.pos_x < verificar_x < b9.pos_x + b9.tam_x and b9.pos_y < verificar_y < b9.pos_y + b9.tam_y:
        if not block:
            tela += b9.num

    if tot.pos_x < verificar_x < tot.pos_x + tot.tam_x and tot.pos_y < verificar_y < tot.pos_y + tot.tam_y:
        op = tot.num
        block = False

    if ad.pos_x < verificar_x < ad.pos_x + ad.tam_x and ad.pos_y < verificar_y < ad.pos_y + ad.tam_y:
        op = ad.num
        tela = ''
        block = False

    if sub.pos_x < verificar_x < sub.pos_x + sub.tam_x and sub.pos_y < verificar_y < sub.pos_y + sub.tam_y:
        op = sub.num
        tela = ''
        block = False

    if mult.pos_x < verificar_x < mult.pos_x + mult.tam_x and mult.pos_y < verificar_y < mult.pos_y + mult.tam_y:
        op = mult.num
        tela = ''
        block = False

    if div.pos_x < verificar_x < div.pos_x + div.tam_x and div.pos_y < verificar_y < div.pos_y + div.tam_y:
        op = div.num
        tela = ''
        block = False

    if back.pos_x < verificar_x < back.pos_x + back.tam_x and back.pos_y < verificar_y < back.pos_y + back.tam_y:

        #  APAGA O ULTIMO ELEMENTO
        if not block:
            tela = tela[0:len(tela) - 1]

    if clear.pos_x < verificar_x < clear.pos_x + clear.tam_x and clear.pos_y < verificar_y < clear.pos_y + clear.tam_y:
        op = clear.num
        tela = ''
        block = False


def principal():
    global tela, op, block, num1, num2, total, sair

    #  TESTA OS EVENTOS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sair = True

        #  TESTA OS EVENTOS DO MOUSE
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            verificar(verificar_x=x, verificar_y=y)

        #  TESTA OS EVENTOS DO TECALDO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sair = True

            #  TESTA O NUMERO DO TECLADO PRECIONADO
            if event.key == pygame.K_KP0 or event.key == pygame.K_0:
                if not block:
                    tela += '0'
            if event.key == pygame.K_KP1 or event.key == pygame.K_1:
                if not block:
                    tela += '1'
            if event.key == pygame.K_KP2 or event.key == pygame.K_2:
                if not block:
                    tela += '2'
            if event.key == pygame.K_KP3 or event.key == pygame.K_3:
                if not block:
                    tela += '3'
            if event.key == pygame.K_KP4 or event.key == pygame.K_4:
                if not block:
                    tela += '4'
            if event.key == pygame.K_KP5 or event.key == pygame.K_5:
                if not block:
                    tela += '5'
            if event.key == pygame.K_KP6 or event.key == pygame.K_6:
                if not block:
                    tela += '6'
            if event.key == pygame.K_KP7 or event.key == pygame.K_7:
                if not block:
                    tela += '7'
            if event.key == pygame.K_KP8 or event.key == pygame.K_8 and event.mod != pygame.KMOD_RSHIFT \
                    or event.key == pygame.K_8 and event.mod != pygame.KMOD_LSHIFT:
                if not block:
                    tela += '8'
            if event.key == pygame.K_KP9 or event.key == pygame.K_9:
                if not block:
                    tela += '9'

            #  TESTA O OPERADOR PRECIONADO
            if event.key == pygame.K_KP_PLUS or event.mod == pygame.KMOD_RSHIFT and event.key == pygame.K_EQUALS \
                    or event.mod == pygame.KMOD_LSHIFT and event.key == pygame.K_EQUALS:
                op = '+'
                tela = ''
                block = False

            if event.key == pygame.K_KP_MINUS or event.key == pygame.K_MINUS:
                op = '-'
                tela = ''
                block = False

            if event.key == pygame.K_KP_MULTIPLY or event.mod == pygame.KMOD_RSHIFT and event.key == pygame.K_8 \
                    or event.mod == pygame.KMOD_LSHIFT and event.key == pygame.K_8:
                op = 'x'
                tela = ''
                block = False

            if event.key == pygame.K_KP_DIVIDE or event.mod == pygame.KMOD_RALT and event.key == pygame.K_q \
                    or event.key == pygame.K_SLASH:
                op = '/'
                tela = ''
                block = False

            if event.key == pygame.K_RETURN:
                op = '='
                block = False

            if event.key == pygame.K_BACKSPACE:

                #  APAGA O ULTIMO ELEMENTO
                if not block:
                    tela = tela[0:len(tela) - 1]

            if event.key == pygame.K_c:
                op = "C"
                tela = ''
                block = False

    #  COR DA TELA
    scren.fill(cinza21)

    #  DESENHA AS BORDA DA TELA
    pygame.draw.rect(scren, preto, [0, 0, 425, 5])  # X SUPERIOR
    pygame.draw.rect(scren, preto, [0, 0, 5, 600])  # Y ESQUERDO
    pygame.draw.rect(scren, preto, [0, 600, 425, 5])  # X INFERIOR
    pygame.draw.rect(scren, preto, [420, 0, 5, 600])  # Y DIREITO

    pygame.draw.rect(scren, preto, [0, 100, 425, 2])

    #  MOSTRA OS BOTÕES NA TELA
    b0.mostrar()
    b1.mostrar()
    b2.mostrar()
    b3.mostrar()
    b4.mostrar()
    b5.mostrar()
    b6.mostrar()
    b7.mostrar()
    b8.mostrar()
    b9.mostrar()

    tot.mostrar(tex_pos_x=30, tex_pos_y=15)
    ad.mostrar(tex_pos_x=30, tex_pos_y=-10)
    sub.mostrar(tex_pos_x=40, tex_pos_y=-10)
    mult.mostrar(tex_pos_x=35, tex_pos_y=-10)
    div.mostrar(tex_pos_x=40, tex_pos_y=0)
    back.mostrar(tex_pos_x=15, tex_pos_y=-10)
    clear.mostrar(tex_pos_x=25, tex_pos_y=-5)

    #  PASSA O PRIMEIRO VALOR FLOAT DA TELA
    if tela != '' and op == '':
        num1 = float(tela)

    #  PASSA O SEGUNDO VALOR FLOAT DA TELA
    if tela != '' and op != '':
        num2 = float(tela)

        #  VERIFICA E REALIZA A OPERAÇÃO ESCOLHIDA
        if op == '+':
            total = int(num1 + num2)

        if op == '-':
            total = int(num1 - num2)

        if op == 'x':
            total = int(num1 * num2)

        if op == '/':
            total = float(num1 / num2)

        if op == '=':
            num1 = 0
            num2 = 0
            tela = str(total)
            op = ''
            block = True

    #  LIMPA A TELA
    if op == 'C':
        tela = ''
        num1 = 0
        num2 = 0
        total = 0
        op = ''

    #  PASSA AS INFORMAÇÕES QUE SERÃO EXIBIDAS NA TELA DO APP
    gui()

    pygame.display.update()


#  CONFIGURA OS BOTÕES
b0 = Botao(pos_x=110, pos_y=500, tam_x=100, tam_y=100, cor=preto, num='0')
b1 = Botao(pos_x=5, pos_y=395, tam_x=100, tam_y=100, cor=preto, num='1')
b2 = Botao(pos_x=110, pos_y=395, tam_x=100, tam_y=100, cor=preto, num='2')
b3 = Botao(pos_x=215, pos_y=395, tam_x=100, tam_y=100, cor=preto, num='3')
b4 = Botao(pos_x=5, pos_y=290, tam_x=100, tam_y=100, cor=preto, num='4')
b5 = Botao(pos_x=110, pos_y=290, tam_x=100, tam_y=100, cor=preto, num='5')
b6 = Botao(pos_x=215, pos_y=290, tam_x=100, tam_y=100, cor=preto, num='6')
b7 = Botao(pos_x=5, pos_y=185, tam_x=100, tam_y=100, cor=preto, num='7')
b8 = Botao(pos_x=110, pos_y=185, tam_x=100, tam_y=100, cor=preto, num='8')
b9 = Botao(pos_x=215, pos_y=185, tam_x=100, tam_y=100, cor=preto, num='9')

tot = Botao(pos_x=320, pos_y=485, tam_x=100, tam_y=115, cor=preto, num='=')
ad = Botao(pos_x=320, pos_y=410, tam_x=100, tam_y=70, cor=preto, num='+')
sub = Botao(pos_x=320, pos_y=335, tam_x=100, tam_y=70, cor=preto, num='-')
mult = Botao(pos_x=320, pos_y=260, tam_x=100, tam_y=70, cor=preto, num='x')
div = Botao(pos_x=320, pos_y=185, tam_x=100, tam_y=70, cor=preto, num='/')
back = Botao(pos_x=320, pos_y=110, tam_x=100, tam_y=70, cor=preto, num='<-')
clear = Botao(pos_x=215, pos_y=110, tam_x=100, tam_y=70, cor=preto, num='C')

#  VARIAVEIS GLOBAIS
tela = ''
op = ''
sair = False
block = False
num1 = 0
num2 = 0
total = 0

#  LOOP PRINCIPAL
while not sair:
    principal()

pygame.quit()
