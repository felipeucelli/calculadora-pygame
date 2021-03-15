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
fps = pygame.time.Clock()


class Botao:
    #  INICIALIZA O METODO CONSTRUTOR
    def __init__(self, pos_x, pos_y, tam_x, tam_y, cor, num, fun):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tam_x = tam_x
        self.tam_y = tam_y
        self.cor = cor
        self.num = num
        self.fun = fun

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
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        #  print(self.pos_x, self.pos_y, self.num)

        #  VERIFICA A POSIÇÃO DO MOUSE NO QUADRADO CORRESPONDENTE
        if self.pos_x < x < self.pos_x + self.tam_x and self.pos_y < y < self.pos_y + self.tam_y:

            #  MUDA A COR DO BOTÃO
            pygame.draw.rect(scren, cinza31, [self.pos_x, self.pos_y, self.tam_x, self.tam_y])

            #  VERIFICA SE O BOTÃO FOI PRECIONADO E RETORNA O VALOR PARA SER ESCRITO NA TELA
            for event1 in pygame.event.get():

                #  FECHA O PROGRAMA
                if event1.type == pygame.QUIT:
                    sair = True

                #  TESTA SE ALGUM BOTÃO FOI PRECIONADO
                if event1.type == pygame.MOUSEBUTTONDOWN:
                    print()

                    #  TESTA A FUNÇÃO DO BOTÃO PRECIONADO
                    if self.fun == 'op':
                        op = self.num

                        #  VERIFICA E REOTORNA O OPERADOR
                        if op != '=':
                            op = self.num
                            tela = ''
                            block = False
                        else:
                            op = self.num

                    #  VERIFICA E RETORNA O NUMERO
                    elif self.fun == 'num':
                        if not block:
                            tela += self.num

        #  ESCREVE O NUMERO NA TELA
        font = pygame.font.SysFont('', 100)
        texto = font.render(self.num, True, branco)
        scren.blit(texto, [tex_pos_x, tex_pos_y])


#  MOSTRA A TELA
def gui():
    global tela, op, block, num1, num2, total

    #  CONFIGURA O TAMANHO DA TELA DE ACORDO COM A QUANTIDADE DE ITENS
    tam_tela2 = tam_tela = 34.5
    tam_tela *= len(tela)
    tam_tela2 *= len(str(int(num1)))

    #  BLOQUEIA A ENTRADA DE NOVOS NUMEROS DE TIVER MAIS DE NOVE ITENS
    if len(tela) >= 9:
        block = True

    font1 = pygame.font.SysFont('', 100)  # SELECIONA A FONTE DA TELA

    texto1 = font1.render(tela, True, branco)  # ESCREVE A 'TELA'
    scren.blit(texto1, [350 - tam_tela, 10])  # SELECIONA A POSIÇÃO X Y DA 'TELA'

    #  VERIFICA SE A TELA FOI LIMPA, CASO COMTRÁRIO MOSTRA O OPERADOR
    if op != 'CE':
        texto1 = font1.render(op, True, branco)  # ESCREVE O OPERADOR
        scren.blit(texto1, [5, 10])  # SELECIONA A POSIÇÃO X Y DO OPERADOR

    #  VERIFICA SE FOI ESCOLHIDO UM OPERADOR E MOSTRA O NUM1
    if op != '' and num1 != 0 and op != '=' and op != 'CE' and num2 == 0:
        texto1 = font1.render(str(int(num1)), True, branco)
        scren.blit(texto1, [350 - tam_tela2, 10])


#  CONFIGURA OS BOTÕES
b0 = Botao(pos_x=110, pos_y=500, tam_x=100, tam_y=100, cor=preto, num='0', fun='num')
b1 = Botao(pos_x=5, pos_y=395, tam_x=100, tam_y=100, cor=preto, num='1', fun='num')
b2 = Botao(pos_x=110, pos_y=395, tam_x=100, tam_y=100, cor=preto, num='2', fun='num')
b3 = Botao(pos_x=215, pos_y=395, tam_x=100, tam_y=100, cor=preto, num='3', fun='num')
b4 = Botao(pos_x=5, pos_y=290, tam_x=100, tam_y=100, cor=preto, num='4', fun='num')
b5 = Botao(pos_x=110, pos_y=290, tam_x=100, tam_y=100, cor=preto, num='5', fun='num')
b6 = Botao(pos_x=215, pos_y=290, tam_x=100, tam_y=100, cor=preto, num='6', fun='num')
b7 = Botao(pos_x=5, pos_y=185, tam_x=100, tam_y=100, cor=preto, num='7', fun='num')
b8 = Botao(pos_x=110, pos_y=185, tam_x=100, tam_y=100, cor=preto, num='8', fun='num')
b9 = Botao(pos_x=215, pos_y=185, tam_x=100, tam_y=100, cor=preto, num='9', fun='num')

tot = Botao(pos_x=320, pos_y=485, tam_x=100, tam_y=115, cor=preto, num='=', fun='op')
ad = Botao(pos_x=320, pos_y=410, tam_x=100, tam_y=70, cor=preto, num='+', fun='op')
sub = Botao(pos_x=320, pos_y=335, tam_x=100, tam_y=70, cor=preto, num='-', fun='op')
mult = Botao(pos_x=320, pos_y=260, tam_x=100, tam_y=70, cor=preto, num='x', fun='op')
div = Botao(pos_x=320, pos_y=185, tam_x=100, tam_y=70, cor=preto, num='/', fun='op')
clear = Botao(pos_x=320, pos_y=110, tam_x=100, tam_y=70, cor=preto, num='CE', fun='op')

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

    #  TESTA OS EVENTOS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sair = True

        #  TESTA OS EVENTOS DO TECALDO
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sair = True

            #  TESTA O NUMERO DO TECLADO PRECIONADO
            if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                if not block:
                    tela += '0'
            if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                if not block:
                    tela += '1'
            if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                if not block:
                    tela += '2'
            if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                if not block:
                    tela += '3'
            if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                if not block:
                    tela += '4'
            if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                if not block:
                    tela += '5'
            if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                if not block:
                    tela += '6'
            if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                if not block:
                    tela += '7'
            if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                if not block:
                    tela += '8'
            if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                if not block:
                    tela += '9'

            #  TESTA O OPERADOR PRECIONADO
            if event.key == pygame.K_KP_PLUS:
                op = '+'
                tela = ''
                block = False
            if event.key == pygame.K_KP_MINUS or event.key == pygame.K_MINUS:
                op = '-'
                tela = ''
                block = False
            if event.key == pygame.K_KP_MULTIPLY:
                op = 'x'
                tela = ''
                block = False
            if event.key == pygame.K_KP_DIVIDE or event.key == pygame.K_SLASH:
                op = '/'
                tela = ''
                block = False
            if event.key == pygame.K_RETURN:
                op = '='
                block = False
            if event.key == pygame.K_BACKSPACE:
                op = "CE"
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
    ad.mostrar(tex_pos_x=30, tex_pos_y=0)
    sub.mostrar(tex_pos_x=40, tex_pos_y=0)
    mult.mostrar(tex_pos_x=30, tex_pos_y=0)
    div.mostrar(tex_pos_x=40, tex_pos_y=0)
    clear.mostrar(tex_pos_x=5, tex_pos_y=5)

    #  PASSA O PRIMEIRO VALOR FLOAT DA TELA
    if tela != '' and op == '':
        num1 = float(tela)

    #  PASSA O SEGUNDO VALOR FLOAT DA TELA
    if tela != '' and op != '':
        num2 = float(tela)

        #  VERIFICA A OPERAÇÃO ESCOLHIDA
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
            op = ''
            tela = str(total)

    #  LIMPA A TELA
    if op == 'CE':
        tela = ''
        num1 = 0
        num2 = 0
        total = 0
        op = ''

    #  PASSA AS INFORMAÇÕES QUE SERÃO EXIBIDAS NA TELA DO APP
    gui()

    pygame.display.update()

pygame.quit()
