from datetime import datetime  # Para criar uma data no e aplicar no Placeholder do HTML
from string import Template  # Para criar o Template do HTML
from dadosEmail import meu_email, minha_senha  # Arquivo que criei com os dados do meu E-mail

from email.mime.multipart import MIMEMultipart  # Para envio de e-mail (Assunto, Remetente, Destinatário, etc)
from email.mime.text import MIMEText  # Para o corpo do e-mail
from email.mime.image import MIMEImage  # Para Anexar imagens no e-mail
import smtplib  # Responsável por fazer o envio de fato via SMTP

with open('template.html', 'r', encoding="UTF-8") as html:  # Abrindo o arquivo HTML
    template = Template(html.read())  # Criando a váriável para receber o texto escrito dentro do arquivo
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpoMsg = template.substitute(nome='Daniel', data=data_atual)  # Substituindo os PlaceHolders que criei no arquivo
    # HTML

msg = MIMEMultipart()  # Instanciando o MIME Multipart para começar a informar os dados do e-mail
msg['from'] = 'Daniel Silva'  # Informando o remetente
msg['to'] = meu_email  # E-mail do destinatário
msg['subject'] = 'Atenção: este é um e-mail de testes.'  # Assunto do e-mail
corpo = MIMEText(corpoMsg, 'html')  # Corpo do e-mail instanciando o MIMEText, aqui peguei o arquivo HTML e informei
# ao Python que é arquivo HTML por parâmetro
msg.attach(corpo)  # Incluindo o corpo do e-mail na variável msg

with open('daora.jfif', 'rb') as img:  # Abrindo a imagem para poder anexar
    img = MIMEImage(img.read())  # Usando o MIMEImage para ler a foto
    msg.attach(img)  # Anexando ao e-mail

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:  # Abrindo o SMTP para realizar o envio com smtplib
    try:
        smtp.ehlo()  # 'Hello' do SMTP para o provedor de e-mail
        smtp.starttls()  # GMAIL permite TLS então aqui estou iniciando o TLS
        smtp.login(meu_email, minha_senha)  # Autenticando com usuário e senha
        smtp.send_message(msg)  # Criando o e-mail com tudo que anexei a variável msg
        print('Email enviado com sucesso')  # Retorno para dizer que deu certo :)
    except Exception as e:
        print('E-mail não enviado:', e)

# print(corpoMsg)
