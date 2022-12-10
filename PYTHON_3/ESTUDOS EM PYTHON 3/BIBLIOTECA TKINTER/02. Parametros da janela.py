from tkinter import *
janela = Tk()

# Quando digitamos janela no inicio, nos estamos chamando a biblioteca para usar as funções de interface grafica,
# como a geometria, textos...
# a ordem é!
# BIBLIOTECA. FUNÇÃO (CONFIGURAÇÕES)
janela.title('Nome do Programa') # TITULO
janela.iconbitmap('logo.ico') # ICONE DA JANELA
janela.geometry('400x250') # TAMANHO -> largura x altura
janela.configure(background='green') # COR DE FUNDO
janela.mainloop() # DEIXA A JANELA EM LOOP, ELA NAO FECHA



