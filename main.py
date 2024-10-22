import tkinter
from tkinter import messagebox as mb
import sqlite3


connection = sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (nome TEXT, curso TEXT, matricula INTEGER)")

def inserevalores(nome, curso='Não especificado', matricula=0):
    
    cursor.execute("INSERT INTO Tabela1 VALUES (?, ?, ?)", (nome, curso, matricula))
    connection.commit()  
    mb.showinfo("Sucesso", f"Nome '{nome}' inserido com sucesso!")

def Main():
    root = tkinter.Tk()
    root.title("Trabalho RAD")
    root.resizable(False, False)

    label = tkinter.Label(root, text="Nome:")
    label.pack()

    nome_var = tkinter.StringVar()
    e1 = tkinter.Entry(root, textvariable=nome_var)
    e1.pack()


    label_cpf = tkinter.Label(root, text="CPF:")
    label_cpf.pack()

    cpf_var = tkinter.StringVar()
    e2 = tkinter.Entry(root, textvariable=cpf_var)
    e2.pack()

  
    label_estado = tkinter.Label(root, text="Estado:")
    label_estado.pack()

    estado_var = tkinter.StringVar()
    e3 = tkinter.Entry(root, textvariable=estado_var)
    e3.pack()

    salvar_button = tkinter.Button(root, text="Salvar", command=lambda: inserevalores(nome_var.get()))
    salvar_button.pack()

    root.mainloop()  


Main()