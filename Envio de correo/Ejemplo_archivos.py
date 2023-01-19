import smtplib,Encriptado,Formato
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

Encriptado.generar()
password = (str)(Encriptado.desencriptar()).split("'")
remitente = 'traps.warning@gmail.com'
destinatario = 'javier.martinez.carranzaipn@gmail.com'

def cargar_archivo_email(email, filename):
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read()) 
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    email.attach(file_attachment) 

email = MIMEMultipart()
email['From'] = remitente
email['To'] = destinatario
email['Subject'] = 'Report email'
email.attach(MIMEText(Formato.html, "html"))

cargar_archivo_email(email, 'PySNMP y Pygal.pdf')
cargar_archivo_email(email, 'MIB.pptx')
cargar_archivo_email(email, 'Pexpec_Paramiko.zip')
cargar_archivo_email(email, 'escudoESCOM.png')

smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente, password[1])
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()

