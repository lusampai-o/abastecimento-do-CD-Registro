# Código de programação em Python para envio de e-mails automáticos via G-mail.#
import pandas as pd

from pedidos import verifica_pedidos

contatos = pd.read_excel('Parceiros.xlsx')
dados = contatos.values.tolist()

for dado in dados:
    destinatario = dado[1]
    copia = dado[2]
    marca = dado[0]
    pedido = dado [3]
    verifica_pedidos(destinatario, copia, pedido, marca)
