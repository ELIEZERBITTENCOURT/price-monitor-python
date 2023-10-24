import requests
import smtplib
from bs4 import BeautifulSoup

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# URL do produto que quer monitorar
url = 'URL_DO_PRODUTO_AQUI'

# Fazendo a requisição HTTP
response = requests.get(url)

# Parseando o conteúdo da página
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrando o preço do produto (a classe pode variar de acordo com o site)
price = soup.find(class_='CLASSE_DO_PRECO').get_text()

# Convertendo o preço para um formato numérico (removendo símbolos de moeda, vírgulas, etc.)
price = float(price.replace('R$', '').replace(',', '').strip())

# Definindo o preço máximo que está disposto a pagar
preco_maximo = 1000  # Substitua pelo seu preço máximo

# Verificando se o preço atual é menor ou igual ao preço máximo
if price <= preco_maximo:
    print(f'O preço do produto é {price}. Vale a pena comprar!')
else:
    print(f'O preço do produto é {price}. Ainda está caro.')

# Aqui o código para enviar notificações
# Configure as informações do servidor de e-mail
email_servidor = 'smtp.seu-servidor-de-email.com'
email_porta = 587
email_usuario = 'seu-email@example.com'
email_senha = 'sua-senha'

# Configure as informações do remetente e destinatário
remetente = 'seu-email@example.com'
destinatario = 'destinatario@example.com'

# Verifique se o preço está abaixo do limite
if price <= preco_maximo:
    # Crie a mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = 'Preço do Produto Baixou!'

    corpo_mensagem = f'O preço do produto é {price}. Vale a pena comprar!'
    msg.attach(MIMEText(corpo_mensagem, 'plain'))

    # Conecte-se ao servidor de e-mail e envie a mensagem
    servidor = smtplib.SMTP(email_servidor, email_porta)
    servidor.starttls()
    servidor.login(email_usuario, email_senha)
    servidor.sendmail(remetente, destinatario, msg.as_string())
    servidor.quit()

    print('Notificação por e-mail enviada com sucesso!')
else:
    print(f'O preço do produto é {price}. Ainda está caro.')

