#coding=utf-8
from tkinter import * # IMPORTAÇÃO DA BIBLIOTECA

root = Tk() # DEFINIÇÃO DIRETA, O NOME root FOI OPCIONAL, PODE-SE COLOCAR O QUE QUISER


frame = Frame(root,bg="blue", width=900, height=900) # FRAME COM SUAS ATRIBUIÇÕES BÁSICAS
frame.pack() # LOCALIDADE PADRÃO PARA O FRAME

imagem = PhotoImage(file="facebook.png") #VARIÁVEL QUE RECEBERÁ O VALOR DA IMAGEM/LOCALIDADE E TYPE(PhotoImage)
foto = Label(root, image=imagem, bg="blue") # NÃO SE CONFUNDA, A IMAGEM FOI COLOCADA EM UMA LABEL SENÃO NÂO TERIA LUGAR P/ FICAR NA TELA
foto.place(x=150,y=10) # LOCALIDADE NA TELA(CORDENADAS), QUE NESTE CASO ESTÁ PADRÃO

btLogin = Button(root, text="ENTRAR", bg="blue", fg="white", command= Login) #BOTÃO ENTRAR
btLogin.place(x=200, y=400)


root.geometry("500x500") # LARGURA x ALTURA
root.title("LOGIN FACEBOOK") # TITULO
root.mainloop() # FIM DO CÓDIGO E RESPONSÁVEL PELA EXECUÇÃO DO PROGRAMA
