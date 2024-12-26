import customtkinter as ctk
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="produtos_db"
)

mycursor = mydb.cursor()

sql = "INSERT INTO produtos (tipo_produto, nome_produto, medida, revestimento, cor_revestimento, quantidade, preco, estado, observacao, prod_entrada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

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
    mycursor.execute(sql, values)
    mydb.commit()
    print("Dados inseridos com sucesso!")

def pegar_valores():
    mycursor.execute("SELECT * FROM produtos")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

# Configurando o estilo do customtkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Estoque Lua Nova Colchões")

frm = ctk.CTkFrame(root, width=400, height=300)
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
combobox_tipo_produto = ctk.CTkComboBox(frm, variable=tipo_produto_var, values=["Escolha Aqui", "Colchão", "Box", "Cabiçeira", "Produto Avulso"], width=200)
combobox_tipo_produto.grid(column=0, row=2, sticky="w", padx=5, pady=5)

ctk.CTkLabel(frm, text="Nome do Produto:").grid(column=1, row=1, sticky="w", padx=5, pady=5)
ctk.CTkEntry(frm, textvariable=nome_produto_var, width=200).grid(column=1, row=2, sticky="w", padx=5, pady=5)

ctk.CTkLabel(frm, text="Medida:").grid(column=0, row=3, sticky="w", padx=5, pady=5)
vcmd_measure = (root.register(validate_float), '%P', '%S')
measure_entry = ctk.CTkEntry(frm, textvariable=measure_var, validate='key', validatecommand=vcmd_measure, width=200)
measure_entry.grid(column=0, row=4, sticky="w", padx=5, pady=5)
measure_entry.bind('<FocusOut>', format_measurement)

ctk.CTkLabel(frm, text="Revestimento").grid(column=1, row=3, sticky="w", padx=5, pady=5)
combobox_revestimento = ctk.CTkComboBox(frm, variable=revestimento_var, values=["Escolha Aqui", "Corino", "Linhão", "Suede"], width=200)
combobox_revestimento.grid(column=1, row=4, sticky="w", padx=5, pady=5)

ctk.CTkLabel(frm, text="Cor do Revestimento").grid(column=2, row=3, sticky="w", padx=5, pady=5)
combobox_cor_revestimento = ctk.CTkComboBox(frm, variable=cor_revestimento_var, values=["Escolha Aqui", "Branco", "Bege", "Marrom", "Preto", "Palha", "Ocre", "Cinza", "Cosmo", "Rosé"], width=200)
combobox_cor_revestimento.grid(column=2, row=4, sticky="w", padx=5, pady=5)

ctk.CTkLabel(frm, text="Quantidade:").grid(column=3, row=3, sticky="w", padx=5, pady=5)
ctk.CTkEntry(frm, textvariable=quantidade_var, width=50).grid(column=3, row=4, sticky="w", padx=5, pady=5)

ctk.CTkLabel(frm, text="Preço:").grid(column=4, row=3, sticky="w", padx=5, pady=5)
vcmd_price = (root.register(validate_float), '%P', '%S')
price_entry = ctk.CTkEntry(frm, textvariable=price_var, validate='key', validatecommand=vcmd_price, width=100)
price_entry.grid(column=4, row=4, sticky="w", padx=5, pady=5)
price_entry.bind('<FocusOut>', format_currency)

ctk.CTkLabel(frm, text="Estado").grid(column=0, row=5, sticky="w", padx=5, pady=5)
combobox_estado = ctk.CTkComboBox(frm, variable=estado_var, values=["Escolha Aqui", "Novo", "Defeito", "Mostruário"], width=200)
combobox_estado.grid(column=0, row=6, sticky="w", padx=5, pady=5)

ctk.CTkLabel(frm, text="Observação:").grid(column=0, row=7, sticky="w", padx=5, pady=5)
ctk.CTkEntry(frm, textvariable=observacao_var, width=600).grid(column=0, row=8, columnspan=5, sticky="w", padx=5, pady=5)

# Botões
ctk.CTkButton(frm, text="Pesquisar", command=pegar_valores).grid(column=0, row=9, sticky="w", padx=5, pady=10)
ctk.CTkButton(frm, text="Registrar", command=insert_values).grid(column=1, row=9, sticky="w", padx=5, pady=10)

root.mainloop()