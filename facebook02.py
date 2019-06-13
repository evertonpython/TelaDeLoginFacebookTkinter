# Projeto desenvolvido por Everton Sousa 
# GitHub: github.com/evertonpython
#coding=utf-8
from tkinter import * # IMPORTAÇÃO DA BIBLIOTECA

root = Tk() # DEFINIÇÃO DIRETA, O NOME root FOI OPCIONAL, PODE-SE COLOCAR O QUE QUISER


def Login():
    if etUsuario.get() == 'admin' and etSenha.get() == 'admin':
        print('LOGADO!')
        from tkinter import *

        janela = Tk()

        fundo = Frame(janela, bg="blue", width=600, height=600)
        fundo.pack()

        welcome = Label(janela, text="LOGADO COM SUCESSO", bg="blue", fg="black")
        welcome.place(x=150,y=50)

        logado = Label(janela, text="SEJA BEM VINDO", bg="blue", fg="white")
        logado.place(x=150,y=200)

        btSair = Button(janela, text="SAIR", bg="red", fg="white", command= Sair)
        btSair.place(x=330,y=330)

        janela.title("FEED")
        janela.geometry("400x400")
        janela.mainloop()

    else:
        print('ACESSO NEGADO!')

frame = Frame(root,bg="blue", width=900, height=900) # FRAME COM SUAS ATRIBUIÇÕES BÁSICAS
frame.pack() # LOCALIDADE PADRÃO PARA O FRAME

imagem = PhotoImage(file="facebook.png") #VARIÁVEL QUE RECEBERÁ O VALOR DA IMAGEM/LOCALIDADE E TYPE(PhotoImage)
foto = Label(root, image=imagem, bg="blue") # NÃO SE CONFUNDA, A IMAGEM FOI COLOCADA EM UMA LABEL SENÃO NÂO TERIA LUGAR P/ FICAR NA TELA
foto.place(x=150,y=10) # LOCALIDADE NA TELA(CORDENADAS), QUE NESTE CASO ESTÁ PADRÃO

btLogin = Button(root, text="ENTRAR", bg="blue", fg="white", command= Login) #BOTÃO ENTRAR
btLogin.place(x=200, y=400)

etUsuario = Entry(root, bg="white", fg="black") # BG= BACKGOUNG(FUNDO), FG=FONTE
etUsuario.place(x=200,y=300) # X= HORIZONTAL, Y=VERTICAL(ALTURA)

lbUsuario = Label(root, text="Usuário", bg="blue", fg="white")
lbUsuario.place(x=130,y=300)

etSenha = Entry(root, bg="white", fg="black", show="*") # BG= BACKGOUNG(FUNDO), FG=FONTE
etSenha.place(x=200,y=350)

lbSenha = Label(root, text="Senha", bg="blue", fg="white")
lbSenha.place(x=130,y=350)


root.geometry("500x500") # LARGURA x ALTURA
root.title("LOGIN FACEBOOK") # TITULO
root.mainloop() # FIM DO CÓDIGO E RESPONSÁVEL PELA EXECUÇÃO DO PROGRAMA
