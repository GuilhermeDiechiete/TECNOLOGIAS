from tkinter import *
janela = Tk()
janela.title('Nome do Programa')
janela.iconbitmap('logo.ico')
janela.geometry('400x250')
janela.configure(background='green')


#PARA INSERIR UM TEXTO, O CORRETO É ATRIBUIR A UMA VARIAVEL

# variavel recebe texto (biblioteca, configurações de estilo)
texto1 = Label(janela, text='Texto', background='black', foreground='white')

#CONFIGURAÇÃO DE POSIÇÃO
texto1.place(x=20, y=50, width=200, height=20) # afastamendo esquerdo x afastamento superior, largura x altura


janela.mainloop()

