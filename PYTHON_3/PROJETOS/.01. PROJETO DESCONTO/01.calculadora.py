from tkinter import *

def calcular():
    desconto = int(desc.get())
    dinheiro = int(valor.get())
    soma = dinheiro - (dinheiro * desconto / 100)
    resposta = Label(tela, text='R${:.2f}'.format(soma))
    resposta.place(x=115, y=60, width=70, height=20)

tela = Tk()

tela.title('DieTec.Sis')

tela.geometry('225x90')
tela.configure(background='#D2691E')

txtdesc = Label(tela, text='Desconto:', background='#363636', foreground='white')
txtdesc.place(x=5, y=5, width=100, height=20)

desc = Entry(tela)
desc.place(x=115, y=5, width=70, height=20)

txtvalor = Label(tela, text='Valor:', background='#363636', foreground='white')
txtvalor.place(x=5, y=30, width=100, height=20)

valor = Entry(tela)
valor.place(x=115, y=30, width=70, height=20)

but = Button(tela, text='Calcular', command=calcular)
but.place(x=5, y=60, width=100, height=20)

tela.mainloop()