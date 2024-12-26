import customtkinter as ctk
import mysql.connector
from datetime import datetime
from tkinter import ttk

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="produtos_db"
)

mycursor = mydb.cursor()

sql_insert = "INSERT INTO produtos (tipo_produto, nome_produto, medida, revestimento, cor_revestimento, quantidade, preco, estado, observacao, prod_entrada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
sql_select = "SELECT * FROM produtos WHERE tipo_produto LIKE %s AND nome_produto LIKE %s AND medida LIKE %s AND revestimento LIKE %s AND cor_revestimento LIKE %s AND quantidade LIKE %s AND preco LIKE %s AND estado LIKE %s AND observacao LIKE %s"

def validate_float(value_if_allowed, text):
    if text in "0123456789.x":
        try:
            parts = value_if_allowed.split('x')
            if len(parts) <= 2:
                for part in parts:
                    if part.strip():
                        float(part.strip())
                return True
        except ValueError:
            return False
    return False

def format_currency(event):
    value = price_var.get()
    if value:
        try:
            value = float(value)
            price_var.set(f"R${value:,.2f}")
        except ValueError:
            price_var.set("")

def format_measurement(event):
    value = measure_var.get()
    if value:
        try:
            parts = value.split('x')
            formatted_parts = [f"{float(part.strip()):.2f}m" for part in parts]
            measure_var.set(' x '.join(formatted_parts))
        except ValueError:
            measure_var.set("")

def insert_values():
    price_value = price_var.get().replace("R$", "").replace(",", "")
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    values = (
        tipo_produto_var.get(),
        nome_produto_var.get(),
        measure_var.get(),
        revestimento_var.get(),
        cor_revestimento_var.get(),
        quantidade_var.get(),
        float(price_value),
        estado_var.get(),
        observacao_var.get(),
        current_datetime
    )
    mycursor.execute(sql_insert, values)
    mydb.commit()
    print("Dados inseridos com sucesso!")
    fetch_data()

def fetch_data():
    for row in tree.get_children():
        tree.delete(row)
    search_values = (
        f"%{tipo_produto_var.get()}%",
        f"%{nome_produto_var.get()}%",
        f"%{measure_var.get()}%",
        f"%{revestimento_var.get()}%",
        f"%{cor_revestimento_var.get()}%",
        f"%{quantidade_var.get()}%",
        f"%{price_var.get()}%",
        f"%{estado_var.get()}%",
        f"%{observacao_var.get()}%"
    )
    mycursor.execute(sql_select, search_values)
    rows = mycursor.fetchall()
    for row in rows:
        tree.insert("", "end", values=row)

# Configurando o estilo do customtkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Estoque Lua Nova Colchões")

frm = ctk.CTkFrame(root)
frm.grid()

# Variáveis para armazenar os valores das entries e comboboxes
tipo_produto_var = ctk.StringVar()
nome_produto_var = ctk.StringVar()
measure_var = ctk.StringVar()
revestimento_var = ctk.StringVar()
cor_revestimento_var = ctk.StringVar()
quantidade_var = ctk.StringVar()
price_var = ctk.StringVar()
estado_var = ctk.StringVar()
observacao_var = ctk.StringVar()

dados_produto = {
    "tipo_produto": tipo_produto_var,
    "nome_produto": nome_produto_var,
    "measure": measure_var,
    "revestimento": revestimento_var,
    "cor_revestimento": cor_revestimento_var,
    "quantidade": quantidade_var,
    "price": price_var,
    "estado": estado_var,
    "observacao": observacao_var
}

# Labels e Entries alinhados
ctk.CTkLabel(frm, text="ESTOQUE LUA NOVA COLCHÕES", font=('Snowy Night', 14)).grid(column=0, row=0, columnspan=5, pady=10)

ctk.CTkLabel(frm, text="Tipo do Produto").grid(column=0, row=1, sticky="w", padx=5, pady=5)
combobox_tipo_produto = ctk.CTkComboBox(frm, variable=tipo_produto_var, values=["Escolha Aqui", "Colchão", "Box", "Cabiçeira", "Produto Avulso"], width=150)
combobox_tipo_produto.grid(column=0, row=2, sticky="w", padx=5, pady=5)

ctk.CTkLabel(frm, text="Nome do Produto:").grid(column=1, row=1, sticky="w", padx=5, pady=5)
ctk.CTkEntry(frm, textvariable=nome_produto_var, width=150).grid(column=1, row=2, sticky="w", padx=5, pady=5)

ctk.CTkLabel(frm, text="Medida:").grid(column=0, row=3, sticky="w", padx=5, pady=5)
vcmd_measure = (root.register(validate_float), '%P', '%S')
measure_entry = ctk.CTkEntry(frm, textvariable=measure_var, validate='key', validatecommand=vcmd_measure, width=150)
measure_entry.grid(column=0, row=4, sticky="w", padx=5, pady=5)
measure_entry.bind('<FocusOut>', format_measurement)

ctk.CTkLabel(frm, text="Revestimento").grid(column=1, row=3, sticky="w", padx=5, pady=5)
combobox_revestimento = ctk.CTkComboBox(frm, variable=revestimento_var, values=["Escolha Aqui", "Corino", "Linhão", "Suede"], width=150)
combobox_revestimento.grid(column=1, row=4, sticky="w", padx=5, pady=5)

ctk.CTkLabel(frm, text="Cor do Revestimento").grid(column=2, row=3, sticky="w", padx=5, pady=5)
combobox_cor_revestimento = ctk.CTkComboBox(frm, variable=cor_revestimento_var, values=["Escolha Aqui", "Branco", "Bege", "Marrom", "Preto", "Palha", "Ocre", "Cinza", "Cosmo", "Rosé"], width=150)
combobox_cor_revestimento.grid(column=2, row=4, sticky="w", padx=5, pady=5)

ctk.CTkLabel(frm, text="Quantidade:").grid(column=3, row=3, sticky="w", padx=5, pady=5)
ctk.CTkEntry(frm, textvariable=quantidade_var, width=50).grid(column=3, row=4, sticky="w", padx=5, pady=5)

ctk.CTkLabel(frm, text="Preço:").grid(column=4, row=3, sticky="w", padx=5, pady=5)
vcmd_price = (root.register(validate_float), '%P', '%S')
price_entry = ctk.CTkEntry(frm, textvariable=price_var, validate='key', validatecommand=vcmd_price, width=100)
price_entry.grid(column=4, row=4, sticky="w", padx=5, pady=5)
price_entry.bind('<FocusOut>', format_currency)

ctk.CTkLabel(frm, text="Estado").grid(column=0, row=5, sticky="w", padx=5, pady=5)
combobox_estado = ctk.CTkComboBox(frm, variable=estado_var, values=["Escolha Aqui", "Novo", "Defeito", "Mostruário"], width=150)
combobox_estado.grid(column=0, row=6, sticky="w", padx=5, pady=5)

ctk.CTkLabel(frm, text="Observação:").grid(column=0, row=7, sticky="w", padx=5, pady=5)
ctk.CTkEntry(frm, textvariable=observacao_var, width=600).grid(column=0, row=8, columnspan=5, sticky="w", padx=5, pady=5)

# Botões
ctk.CTkButton(frm, text="Pesquisar", command=fetch_data).grid(column=0, row=9, sticky="w", padx=5, pady=10)
ctk.CTkButton(frm, text="Registrar", command=insert_values).grid(column=1, row=9, sticky="w", padx=5, pady=10)

# Tabela para mostrar os dados
tree = ttk.Treeview(root, columns=("ID", "Tipo do Produto", "Nome do Produto", "Medida", "Revestimento", "Cor do Revestimento", "Quantidade", "Preço", "Estado", "Observação", "Data de Entrada"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Tipo do Produto", text="Tipo do Produto")
tree.heading("Nome do Produto", text="Nome do Produto")
tree.heading("Medida", text="Medida")
tree.heading("Revestimento", text="Revestimento")
tree.heading("Cor do Revestimento", text="Cor do Revestimento")
tree.heading("Quantidade", text="Quantidade")
tree.heading("Preço", text="Preço")
tree.heading("Estado", text="Estado")
tree.heading("Observação", text="Observação")
tree.heading("Data de Entrada", text="Data de Entrada")

# Ajustando a largura das colunas
tree.column("ID", width=30)
tree.column("Tipo do Produto", width=100)
tree.column("Nome do Produto", width=100)
tree.column("Medida", width=80)
tree.column("Revestimento", width=100)
tree.column("Cor do Revestimento", width=100)
tree.column("Quantidade", width=80)
tree.column("Preço", width=80)
tree.column("Estado", width=80)
tree.column("Observação", width=150)
tree.column("Data de Entrada", width=100)

tree.grid(column=0, row=10, columnspan=5, padx=5, pady=10)

fetch_data()

root.mainloop()