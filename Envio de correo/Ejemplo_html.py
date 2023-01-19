import smtplib,Encriptado,Formato
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

Encriptado.generar()
password = (str)(Encriptado.desencriptar()).split("'")

remitente = 'traps.warning@gmail.com'
destinatario = 'javier.martinez.carranzaipn@gmail.com'

email = MIMEMultipart()
email['From'] = remitente
email['To'] = destinatario
email['Subject'] ='Envio de correo con HTML '
email.attach(MIMEText(Formato.html, "html")) 

smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente, password[1])
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()
