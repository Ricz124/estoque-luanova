from tkinter import *
from tkinter import ttk
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

print(mydb)

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

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

# Configurando o estilo dos botões
style = ttk.Style()
style.configure('TButton', background='black', foreground='white', font=('Snowy Night', 10))
style.map('TButton', background=[('active', 'black')], foreground=[('active', 'white')])

# Variáveis para armazenar os valores das entries e comboboxes
tipo_produto_var = StringVar()
nome_produto_var = StringVar()
measure_var = StringVar()
revestimento_var = StringVar()
cor_revestimento_var = StringVar()
quantidade_var = StringVar()
price_var = StringVar()
estado_var = StringVar()
observacao_var = StringVar()

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
ttk.Label(frm, text="ESTOQUE LUA NOVA COLCHÕES", font=('Snowy Night', 14), background='black', foreground='white').grid(column=0, row=0, columnspan=5, pady=10)

ttk.Label(frm, text="Tipo do Produto").grid(column=0, row=1, sticky=W, padx=5, pady=5)
combobox_tipo_produto = ttk.Combobox(frm, textvariable=tipo_produto_var, values=["nulo", "Colchão", "Box", "Cabiçeira", "Produto Avulso"], width=22)
combobox_tipo_produto.grid(column=0, row=2, sticky=W, padx=5, pady=5)
combobox_tipo_produto.current(0)

ttk.Label(frm, text="Nome do Produto:").grid(column=1, row=1, sticky=W, padx=5, pady=5)
ttk.Entry(frm, textvariable=nome_produto_var, width=24).grid(column=1, row=2, sticky=W, padx=5, pady=5)

ttk.Label(frm, text="Medida:").grid(column=0, row=3, sticky=W, padx=5, pady=5)
vcmd_measure = (root.register(validate_float), '%P', '%S')
measure_entry = ttk.Entry(frm, textvariable=measure_var, validate='key', validatecommand=vcmd_measure, width=24)
measure_entry.grid(column=0, row=4, sticky=W, padx=5, pady=5)
measure_entry.bind('<FocusOut>', format_measurement)

ttk.Label(frm, text="Revestimento").grid(column=1, row=3, sticky=W, padx=5, pady=5)
combobox_revestimento = ttk.Combobox(frm, textvariable=revestimento_var, values=["nulo", "Corino", "Linhão", "Suede"], width=22)
combobox_revestimento.grid(column=1, row=4, sticky=W, padx=5, pady=5)
combobox_revestimento.current(0)

ttk.Label(frm, text="Cor do Revestimento").grid(column=2, row=3, sticky=W, padx=5, pady=5)
combobox_cor_revestimento = ttk.Combobox(frm, textvariable=cor_revestimento_var, values=["nulo", "Branco", "Bege", "Marrom", "Preto", "Palha", "Ocre", "Cinza", "Cosmo", "Rosé"], width=22)
combobox_cor_revestimento.grid(column=2, row=4, sticky=W, padx=5, pady=5)
combobox_cor_revestimento.current(0)

ttk.Label(frm, text="Quantidade:").grid(column=3, row=3, sticky=W, padx=5, pady=5)
ttk.Entry(frm, textvariable=quantidade_var, width=6).grid(column=3, row=4, sticky=W, padx=5, pady=5)

ttk.Label(frm, text="Preço:").grid(column=4, row=3, sticky=W, padx=5, pady=5)
vcmd_price = (root.register(validate_float), '%P', '%S')
price_entry = ttk.Entry(frm, textvariable=price_var, validate='key', validatecommand=vcmd_price, width=10)
price_entry.grid(column=4, row=4, sticky=W, padx=5, pady=5)
price_entry.bind('<FocusOut>', format_currency)

ttk.Label(frm, text="Estado").grid(column=0, row=5, sticky=W, padx=5, pady=5)
combobox_estado = ttk.Combobox(frm, textvariable=estado_var, values=["Escolha Aqui", "Novo", "Defeito", "Mostruário"], width=22)
combobox_estado.grid(column=0, row=6, sticky=W, padx=5, pady=5)
combobox_estado.current(0)

ttk.Label(frm, text="Observação:").grid(column=0, row=7, sticky=W, padx=5, pady=5)
ttk.Entry(frm, textvariable=observacao_var, width=90).grid(column=0, row=8, columnspan=5, sticky=W, padx=5, pady=5)

# Botões
ttk.Button(frm, text="Pesquisar", style='TButton').grid(column=0, row=9, sticky=W, padx=5, pady=10)
ttk.Button(frm, text="Registrar", style='TButton', command=insert_values).grid(column=1, row=9, sticky=W, padx=5, pady=10)

root.mainloop()