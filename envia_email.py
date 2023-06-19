import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email.message
from email import encoders
import json

def enviar_email(arquivo, destinatario, copia, pedido, marca):
    
    with open('token.json', 'r') as f:
        ARQUIVO_JSON = json.load(f)

    send = ",".join([destinatario, copia]).split(',')

    mensagem = MIMEMultipart()
    mensagem['Subject'] = 'PEDIDO BBX - JUNHO - {} - {} - REGULARES'.format(marca, pedido)
    mensagem['From'] = ARQUIVO_JSON['from']
    mensagem['To'] = destinatario
    mensagem['Cc'] = copia
    senha = ARQUIVO_JSON['token']

    corpo_email = '''Boa tarde, tudo bem?
    Segue pedido para abastecimento do CD Registro - Lojas BBX, liberado para faturamento imediato.

    Número do pedido = {}

    IMPORTANTE:
    - Volumes muito alto devem ser paletizados;  
    - Não recebemos itens não vendáveis no Centro de Distribuição (brindes /provadores).
    - Só recebemos produtos com o prazo de validade mínimo de 12 meses; 

    DADOS FATURAMENTO E ENTREGA DO E-COMMERCE:
    NOME DA EMPRESA LTDA
    CNPJ: 12.345.678/9101-12
    I.E.: 73773873992
    ENDEREÇO: Rua, Complemento - Bairro - CEP:  00.000-000 – Cidade - Estado

    Check list | Agendamentos:
    · As notas que chegarem sem agendamento ou fora da data agendada, serão recusadas.
    · O e-mail de solicitação de agendamento deve ser enviado para contato@dominio.com;
    · Entregas com 30 por cento dos itens avariados ou fora destas políticas serão totalmente recusadas.

    Qualquer dúvida, estou a disposição!
    Att,'''.format(pedido)


    mensagem.attach(MIMEText(corpo_email, 'plain'))
    
    # Anexando os pedidos
    filename = arquivo
    attachment = open(f'C:/Users/usuario/pedidos/{arquivo}', 'r+b')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    mensagem.attach(part)
    attachment.close()

    # Envio do email
    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        s.ehlo()
        s.starttls()
        s.login(mensagem['From'], senha)
        s.send_message(mensagem)
        print('Email para {} enviado com sucesso!'.format(marca)) 
    # s(quit())