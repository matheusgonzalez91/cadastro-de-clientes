import tkinter as tk
import sqlite3
import pandas as pd

# conexao = sqlite3.connect('clientes.db')
#
# cursor = conexao.cursor()
#
# cursor.execute(''' CREATE TABLE clientes (
#     nome text,
#     sobrenome text,
#     email text,
#     telefone text
#     )
# ''')
#
# conexao.commit()
#
# conexao.close()


def cadastrar_cliente():
    conexao = sqlite3.connect('clientes.db')

    cursor = conexao.cursor()

    cursor.execute('INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)',
                   {
                       'nome': entry_nome.get(),
                       'sobrenome': entry_sobrenome.get(),
                       'email': entry_email.get(),
                       'telefone': entry_telefone.get()
                   }
                   )

    conexao.commit()

    conexao.close()

    entry_nome.delete(0, 'end')
    entry_sobrenome.delete(0, 'end')
    entry_email.delete(0, 'end')
    entry_telefone.delete(0, 'end')


def exportar_cliente():
    conexao = sqlite3.connect('clientes.db')

    cursor = conexao.cursor()

    cursor.execute('SELECT *, oid FROM clientes')
    clientes_cadastrados = cursor.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['NOME', 'SOBRENOME', 'EMAIL', 'TELEFONE', 'ID_BANCO'])
    clientes_cadastrados.to_excel('lista_cadastro_clientes.xlsx')

    conexao.commit()

    conexao.close()


janela = tk.Tk()
janela.title('Cadastrar Clientes')

# Labels:

label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='Email')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)

# Entrys:

entry_nome = tk.Entry(janela, text='Nome', width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, text='Sobrenome', width=30)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, text='Email', width=30)
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, text='Telefone', width=30)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

# Button:

botao_cadastrar = tk.Button(janela, text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=3, ipadx=130)

botao_exportar = tk.Button(janela, text='Exportar para Excel', command=exportar_cliente)
botao_exportar.grid(row=5, column=0, padx=10, pady=10, columnspan=3, ipadx=130)


janela.mainloop()