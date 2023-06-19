import os
from envia_email import enviar_email

def verifica_pedidos(destinatario, copia, pedido, marca):
    diretorio = os.listdir('C:/Users/usuario/pedidos')
    for arquivo in diretorio:
        if marca == arquivo.replace('.csv', ''):
            enviar_email(arquivo, destinatario, copia, pedido, marca)


