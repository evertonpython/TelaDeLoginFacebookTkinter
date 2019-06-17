# coding=utf-8
from tkinter import *

janela = Tk()

janela["bg"] = "blue"

def sair():
    quit()

def Login():
    if etUsuario.get() == 'teste' and etSenha.get() == 'admin':
        print("LOGADO!!!")
        from tkinter import *
        root = Tk()

        hello = Label(root, text="Hello World", fg="red")
        hello.pack()

        btSair = Button(root, text="SAIR", bg="red", fg="white", command=sair)
        btSair.place(x=50,y=350)

        root.title("LOGADO")
        root.geometry("300x500")
        root.mainloop()

    else:
        print("ACESSO NEGADO!!!")

imagem = PhotoImage(file="facebook.png")
logo = Label(janela, image=imagem, bg="blue")
logo.place(x=5,y=10)

lbUsuario = Label(janela, text="Usuário", bg="blue", fg="white")
lbUsuario.place(x=250,y=150)

lbSenha = Label(janela, text="Senha", bg="blue", fg="white")
lbSenha.place(x=250,y=250)

etUsuario = Entry(janela, bg="white", fg="black")
etUsuario.place(x=320,y=150)

etSenha = Entry(janela, bg="white", fg="black", show="*")
etSenha.place(x=320,y=250)

btEntrar = Button(janela, text="Entrar", bg="blue", fg="white", command=Login)
btEntrar.place(x=400,y=320)

janela.title("FACEBOOK_LOGIN")
janela.geometry("500x400")
janela.mainloop()
