from tkinter import *
janela = Tk()
janela.title('Nome do Programa')
janela.iconbitmap('logo.ico')
janela.geometry('400x250')
janela.configure(background='green')


#ADD CAIXA DE ENTRADA

#A caixa de entrada deve ser atribuida a uma variavel, para salvarmos os dados digitados nelas

entrada1 = Entry(janela)
entrada1.place(x=20, y=20, width=70, height=20)

#Podemos add caixas maiores, para textos longos

entradaOBS = Text(janela)
entradaOBS.place(x=20, y=50, width=200, height=100)





janela.mainloop()