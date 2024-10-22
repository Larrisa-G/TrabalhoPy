import tkinter
from tkinter import messagebox as mb
from PIL import Image, ImageTk
from tkinter import ttk  # Importar ttk para usar Combobox
import sqlite3

# Conexão com o banco de dados SQLite
connection = sqlite3.connect('example.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (nome TEXT, cpf TEXT, estado TEXT, tipo TEXT)")


def inserevalores(nome, cpf, estado, tipo):
    
    with open("config.txt", "r") as file:
        content = file.read()
        estados = content.split(';')

    if estado not in estados:
        mb.showerror("Erro", "Estado inválido! O estado deve estar contido no arquivo config.txt")
        return

    cursor.execute("INSERT INTO Tabela1 VALUES (?, ?, ?, ?)", (nome, cpf, estado, tipo))
    connection.commit()
    mb.showinfo("Sucesso", f"Dados de '{nome}' inseridos com sucesso!")

def Main():
    root = tkinter.Tk()
    root.title("Trabalho RAD")
    root.resizable(False, False)

    # Carregue a imagem usando Pillow
    image = Image.open(r"C:\Users\Laris\OneDrive\Área de Trabalho\TrabalhoPy\biru.png")
    bg_image = ImageTk.PhotoImage(image)

    # Usar Canvas para colocar a imagem de fundo
    canvas = tkinter.Canvas(root, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    frame = tkinter.Frame(root, bg="lightgray", bd=5)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    label_nome = tkinter.Label(frame, text="Nome:", bg='lightgray')
    label_nome.pack(pady=5)
    nome_var = tkinter.StringVar()
    e1 = tkinter.Entry(frame, textvariable=nome_var)
    e1.pack(pady=5)

    label_cpf = tkinter.Label(frame, text="CPF:", bg='lightgray')
    label_cpf.pack(pady=5)
    cpf_var = tkinter.StringVar()
    e2 = tkinter.Entry(frame, textvariable=cpf_var)
    e2.pack(pady=5)

    label_estado = tkinter.Label(frame, text="Estado:", bg='lightgray')
    label_estado.pack(pady=5)
    estado_var = tkinter.StringVar()
    e3 = tkinter.Entry(frame, textvariable=estado_var)
    e3.pack(pady=5)

    # Adicionando o Combobox para selecionar o tipo
    label_tipo = tkinter.Label(frame, text="Tipo:", bg='lightgray')
    label_tipo.pack(pady=5)
    tipo_var = tkinter.StringVar()
    combobox_tipo = ttk.Combobox(frame, textvariable=tipo_var)
    combobox_tipo['values'] = ('clt', 'mei', 'socio')
    combobox_tipo.pack(pady=5)

    salvar_button = tkinter.Button(frame, text="Salvar", command=lambda: inserevalores(nome_var.get(), cpf_var.get(), estado_var.get(), tipo_var.get()))
    salvar_button.pack(pady=10)

    root.mainloop()

Main()
