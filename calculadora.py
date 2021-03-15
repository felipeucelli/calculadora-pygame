import pygame

pygame.init()

largura = 425
altura = 605

#  CORES
branco = (255, 255, 255)
preto = (0, 0, 0)
cinza11 = (28, 28, 28)
cinza21 = (54, 54, 54)
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

#  SELECIONA O NOME DO PROGRAMA
pygame.display.set_caption('Calculadora')


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

    #  VERIFICA O VALOR DO BOTÃO PRECIONADO E  RETORNA O MESMO
    def verificar(self, x1, y1):
        global sair, block, is_total, tela, op

        if self.pos_x < x1 < self.pos_x + self.tam_x and self.pos_y < y1 < self.pos_y + self.tam_y:

            #  TESTA A FUNÇÃO DO BOTÃO PRECIONADO
            if self.fun == 'op' and tela != '' and tela != '-':

                #  VERIFICA E REOTORNA O OPERADOR
                if self.num != '<-' and self.num != '=':
                    op = self.num
                    tela = ''
                    block = False

                #  APAGA O ULTIMO ELEMENTO
                elif self.num == '<-':
                    if not is_total:
                        tela = tela[0:len(tela) - 1]

                elif self.num == '=':
                    op = self.num
                    block = False

            #  VERIFICA E RETORNA O NUMERO
            elif self.fun == 'num':

                #  TESTA SE TEM PONTO
                if self.num == '.':

                    if tela != '-':
                        #  VERIFICA QUANTOS PONTOS TEM E BLOQUEIA SE FOR MAIOR QUE 1
                        if tela.count('.') < 1:

                            #  VERIFICA SE A TELA ESTA VAZIA E ADIOCNA O 0. CASO ESTEJA
                            if tela == '':
                                tela = '0.'

                            #  ADCIONA O PONTO NA TELA CASO ELA NAO ESTEJA VAZIA E NAO ESTIVER BLOQUEADO
                            else:
                                if not block:
                                    tela += self.num

                #  RETORNA O NUMERO DIGITADO
                else:
                    if not block:

                        #  VERIFICA SE O NUMERO SERA POSITIVO OU NEGATIVO
                        if self.num == '-+':

                            #  VERIFICA SE O NUMERO E POSITIVO
                            if tela == '':
                                tela += '-'

                            #  TORNA O NUMERO POSITIVO SE ELE FOR NEGATIVO
                            elif tela == '-':
                                tela = ''
                        else:
                            tela += self.num


#  FUNÇAO QUE EFETUA OS CALCULOS
def calcular():

    global tela, num1, num2, op, block, is_total, total

    #  PASSA O PRIMEIRO VALOR FLOAT DA TELA
    if tela != '' and op == '' and tela != '-' and tela != '-.':
        num1 = float(tela)

    #  PASSA O SEGUNDO VALOR FLOAT DA TELA
    if tela != '' and op != '' and tela != '-' and tela != '-.':
        num2 = float(tela)

        #  VERIFICA E REALIZA A OPERAÇÃO ESCOLHIDA SEGUINDO UM FLOAT PARA O TOTAL
        if op == '+':
            total = float(num1 + num2)

        if op == '-':
            total = float(num1 - num2)

        if op == 'x':
            total = float(num1 * num2)

        if op == '/' and tela != '0':
            total = float(num1 / num2)

        if op == '^':
            total = float(num1 ** num2)

        #  MOSTRA O RESULTADO DA OPERAÇAO
        if op == '=':
            num1 = 0
            num2 = 0
            op = ''
            block = True
            is_total = True

            #  DIVIDE TOTAL EM ANTES E DEPOIS DO PONTO
            dados = str(total).split('.')
            teste = ''

            #  RETORNA O VALOR DE TOTAL
            for c in dados[1]:
                if c != '0':
                    teste = 'FLOAT'
                    break
                else:
                    teste = 'INT'

            #  TESTA O VALOR DE TOTAL E RETORNA UM INT OU FLOAT
            if teste == 'INT':
                tela = str(int(total))
            else:
                tela = str(float(total))

    #  LIMPA A TELA
    if op == 'C':
        tela = ''
        num1 = 0
        num2 = 0
        total = 0
        op = ''
        block = False
        is_total = False


#  FUNÇÃO DE EXIBIÇÃO DOS VALORES NA TELA
def gui():

    global tela, op, block, num1, num2, total

    #  VERIFICA O TAMANHO DA 'TELA' E REDIMENSIONA
    tam_tela = len(tela) * 39

    #  BLOQUEIA A ENTRADA DE VALORES SE HOUVER 9 ITENS OU SE ESTIVER MOSTRANDO O TOTAL
    if len(tela) >= 9 or is_total:
        block = True
    else:
        block = False

    #  ESCREVE OS 8 PRIMEIROS NUMEROS DA TELA SE HOUVER MAIS DE 8 ELEMENTOS
    if len(tela) > 8 and is_total:
        tela = tela[0:9]
        fonte_num_limite = pygame.font.SysFont('Arial', 60)
        txt_num_limte = fonte_num_limite.render('E', True, branco)
        scren.blit(txt_num_limte, [5, 40])

    #  VERIFICA SE É O PRIMEIRO VALOR QUE ESTA ENTRANDO
    if op == '':

        fonte_tela = pygame.font.SysFont('Arial', 70)
        txt_tela = fonte_tela.render(tela, True, branco)

        #   VERIFICA O TAMANHO DO TOTAL E MOSTRA NO MAXIMO 9 ELEMNTOS
        if len(tela) >= 10:
            tela = tela[0:10]
            scren.blit(txt_tela, [420 - tam_tela, 10])

        else:
            #  CONFIGURA O TEXTO E A FONTE DA PRIMEIRA ENTRADA
            txt_tela = fonte_tela.render(tela, True, branco)

            #  REDIMENSIONA O TEXO DE TELA COM -
            if '-' in tela and '.' not in tela:
                scren.blit(txt_tela, [435 - tam_tela, 10])

            #  REDIMENSONA O TEXTO DE TELA COM - E .
            if '-' in tela and '.' in tela:
                scren.blit(txt_tela, [455 - tam_tela, 10])

            #  REDIMENSIONA O TEXTO DE TELA COM  .
            if '.' in tela and '-' not in tela:
                scren.blit(txt_tela, [440 - tam_tela, 10])

            #  REDIMENSIONA A O TEXTO DE TELA
            if '-' not in tela and '.' not in tela:
                scren.blit(txt_tela, [420 - tam_tela, 10])

    #  CONFIGURA O TEXTO DA SEGUNDA ENTRADA
    else:
        fonte_tela_2 = pygame.font.SysFont('Arial', 40)
        txt_tela_2 = fonte_tela_2.render(tela, True, branco)

        #  SEPARA NUM2 EM ANTES E DEPOIS DO PONTO
        dados2 = str(num2).split('.')
        teste2 = ''

        #  RETORNA O VALOR DE NUM2
        if tela != '' and tela != '-':
            for c in dados2[1]:
                if c != '0':
                    teste2 = 'FLOAT'
                    break
                else:
                    teste2 = 'INT'

        #  TESTA O VALOR DE NUM2 E REDIMENSIONA O TEXTO DE TELA
        if teste2 == 'FLOAT':

            #  REDIMENSIONA O TEXTO DE TELA COM - E .
            if '-' in tela:
                scren.blit(txt_tela_2, [440 - (len(tela) * 22), 55])

            #  REDIMESNSIONA O TEXTO DE TELA COM .
            else:
                scren.blit(txt_tela_2, [430 - (len(tela) * 22), 55])
        else:

            #  REDIMESNIONA O TEXTO DE TELA COM -
            if '-' in tela:
                scren.blit(txt_tela_2, [427 - (len(tela) * 22), 55])

            #  REDIMESNIONA O TEXTO DE TELA
            else:
                scren.blit(txt_tela_2, [418 - (len(tela) * 22), 55])

        # CONFIGURA A FONTE DE TEXTO DA PRIMEIRA ENTRADA JUNTO COM A SEGUNDA
        fonte_num = pygame.font.SysFont('Arial', 40)

        #  SEPARA NUM1 EM ANTES E DEPOIS DO PONTO
        dados = str(num1).split('.')
        teste = ''

        #  RETORNA O VALOR DE NUM1
        for c in dados[1]:
            if c != '0':
                teste = 'FLOAT'
                break
            else:
                teste = 'INT'

        #  TESTA O VALOR DE NUM1 E REDIMENCIONA O TEXTO DE NUM1
        if teste == 'FLOAT':
            txt_num = fonte_num.render(str(float(num1)), True, branco)

            #  REDIMENSIONA O TEXTO DE NUM1 COM - E .
            if '-' in str(num1):
                scren.blit(txt_num, [451 - (len(str(float(num1))) * 24), 5])

            #  REDIMESNIONA O TEXTO DE NUM1 COM .
            else:
                scren.blit(txt_num, [439 - (len(str(float(num1))) * 24), 5])

        else:
            txt_num = fonte_num.render(str(int(num1)), True, branco)

            #  REDIMENSIONA O TEXTO DE NUM1 COM -
            if '-' in str(num1):
                scren.blit(txt_num, [427 - (len(str(int(num1))) * 22), 5])

            #  REDIMESNIONA O TEXTO DE NUM1
            else:
                scren.blit(txt_num, [418 - (len(str(int(num1))) * 22), 5])

        #  RETORNA NA TELA O OPERADOR
        if op != 'C' and op != '=':
            fonte_op = pygame.font.SysFont('Arial', 60)
            txt_op = fonte_op.render(op, True, branco)
            scren.blit(txt_op, [5, 10])


def principal():
    global tela, op, block, is_total, num1, num2, total, sair

    while not sair:
        #  TESTA OS EVENTOS
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sair = True

            #  TESTA OS EVENTOS DO MOUSE
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                b0.verificar(x1=x, y1=y)
                b1.verificar(x1=x, y1=y)
                b2.verificar(x1=x, y1=y)
                b3.verificar(x1=x, y1=y)
                b4.verificar(x1=x, y1=y)
                b5.verificar(x1=x, y1=y)
                b6.verificar(x1=x, y1=y)
                b7.verificar(x1=x, y1=y)
                b8.verificar(x1=x, y1=y)
                b9.verificar(x1=x, y1=y)
                sinal.verificar(x1=x, y1=y)

                ponto.verificar(x1=x, y1=y)

                tot.verificar(x1=x, y1=y)
                ad.verificar(x1=x, y1=y)
                sub.verificar(x1=x, y1=y)
                mult.verificar(x1=x, y1=y)
                div.verificar(x1=x, y1=y)
                expo.verificar(x1=x, y1=y)

                back.verificar(x1=x, y1=y)
                clear.verificar(x1=x, y1=y)

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
                        and event.mod != pygame.KMOD_LSHIFT:
                    if not block:
                        tela += '8'
                if event.key == pygame.K_KP9 or event.key == pygame.K_9:
                    if not block:
                        tela += '9'

                # ADICIONA UM PONTO
                if event.key == pygame.K_PERIOD:

                    if tela != '-':
                        #  TESTA QUANTOS PONTO TEM NA TELA E BLOQUEIA SE FOR MAIOR QUE 1
                        if tela.count('.') < 1:

                            #  TESTA SE A TELA ESTA VAZIA E CASO ESTEJA ADICIONA 0.
                            if tela == '':
                                tela = '0.'
                            else:
                                if not block:
                                    tela += '.'

                #  TESTA O OPERADOR PRECIONADO
                if event.key == pygame.K_KP_PLUS or event.mod == pygame.KMOD_RSHIFT and event.key == pygame.K_EQUALS \
                        or event.mod == pygame.KMOD_LSHIFT and event.key == pygame.K_EQUALS:

                    #  VERIFICA SE O NUMERO E NEGATIVO E TRANSFORMA EM POSITIVO
                    if tela == '-':
                        tela = ''

                    #  VERFICA SE TEM NUMERO NA TELA PARA INSERIR O OPERADOR
                    if tela != '' and op == '' and tela != '-':
                        op = '+'
                        tela = ''
                        block = False
                        is_total = False

                if event.key == pygame.K_KP_MINUS or event.key == pygame.K_MINUS:

                    #  VERIFICA SE O NUMERO E POSITIVO
                    if tela == '':
                        tela += '-'

                    #  TORNA O NUMERO POSITIVO SE ELE FOR NEGATIVO
                    elif tela == '-':
                        tela = ''

                    #  VERIFICA SE TEM NUMERO NA TELA PARA INSERIR O OPERADOR
                    elif tela != '' and op == '' and tela != '-':
                        op = '-'
                        tela = ''
                        block = False
                        is_total = False

                if event.key == pygame.K_KP_MULTIPLY or event.mod == pygame.KMOD_RSHIFT and event.key == pygame.K_8 \
                        or event.mod == pygame.KMOD_LSHIFT and event.key == pygame.K_8:

                    #  VERIFICA SE TEM NUMERO NA TELA PARA INSERIR O OPERADOR
                    if tela != '' and op == '' and tela != '-':
                        op = 'x'
                        tela = ''
                        block = False
                        is_total = False

                if event.key == pygame.K_KP_DIVIDE or event.mod == pygame.KMOD_RALT and event.key == pygame.K_q \
                        or event.key == pygame.K_SLASH:

                    #  VERIFCA SE TEM NUMERO NA TELA PARA INSERIR O OPERADOR
                    if tela != '' and op == '' and tela != '-':
                        op = '/'
                        tela = ''
                        block = False
                        is_total = False

                if event.key == pygame.K_x:

                    #  VERIFICA SE TEM NUMERO NA TELA PARA INSERIR O OPERADOR
                    if tela != '' and op == '' and tela != '-':
                        op = '^'
                        tela = ''
                        block = False
                        is_total = False

                if event.key == pygame.K_RETURN:
                    if tela != '' and op != '':
                        op = '='
                        block = False
                        is_total = False

                if event.key == pygame.K_BACKSPACE:

                    #  APAGA O ULTIMO ELEMENTO
                    if not is_total:
                        tela = tela[0:len(tela) - 1]

                if event.key == pygame.K_c:
                    op = "C"
                    tela = ''
                    block = False
                    is_total = False

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
        sinal.mostrar(tex_pos_x=10, tex_pos_y=0)

        ponto.mostrar(tex_pos_x=40, tex_pos_y=20)

        tot.mostrar(tex_pos_x=30, tex_pos_y=15)
        ad.mostrar(tex_pos_x=30, tex_pos_y=-10)
        sub.mostrar(tex_pos_x=40, tex_pos_y=-10)
        mult.mostrar(tex_pos_x=35, tex_pos_y=-10)
        div.mostrar(tex_pos_x=40, tex_pos_y=0)
        expo.mostrar(tex_pos_x=30, tex_pos_y=5)

        back.mostrar(tex_pos_x=15, tex_pos_y=-10)
        clear.mostrar(tex_pos_x=25, tex_pos_y=-5)

        #  EFETUA OS CALCULOS
        calcular()

        #  PASSA AS INFORMAÇÕES QUE SERÃO EXIBIDAS NA TELA DO APP
        gui()

        pygame.display.update()


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
sinal = Botao(pos_x=5, pos_y=500, tam_x=100, tam_y=100, cor=preto, num='-+', fun='num')

ponto = Botao(pos_x=215, pos_y=500, tam_x=100, tam_y=100, cor=preto, num='.', fun='num')

tot = Botao(pos_x=320, pos_y=485, tam_x=100, tam_y=115, cor=preto, num='=', fun='op')
ad = Botao(pos_x=320, pos_y=410, tam_x=100, tam_y=70, cor=preto, num='+', fun='op')
sub = Botao(pos_x=320, pos_y=335, tam_x=100, tam_y=70, cor=preto, num='-', fun='op')
mult = Botao(pos_x=320, pos_y=260, tam_x=100, tam_y=70, cor=preto, num='x', fun='op')
div = Botao(pos_x=320, pos_y=185, tam_x=100, tam_y=70, cor=preto, num='/', fun='op')
expo = Botao(pos_x=5, pos_y=110, tam_x=100, tam_y=70, cor=preto, num='^', fun='op')

back = Botao(pos_x=320, pos_y=110, tam_x=100, tam_y=70, cor=preto, num='<-', fun='op')
clear = Botao(pos_x=215, pos_y=110, tam_x=100, tam_y=70, cor=preto, num='C', fun='op')


#  VARIAVEIS GLOBAIS
tela = ''
op = ''
sair = False
block = False
is_total = False
num1 = 0
num2 = 0
total = 0.0

#  LOOP PRINCIPAL
if __name__ == '__main__':
    principal()

pygame.quit()
