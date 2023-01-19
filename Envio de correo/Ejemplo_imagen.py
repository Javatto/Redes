import smtplib,Encriptado,Formato
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

Encriptado.generar()
password = (str)(Encriptado.desencriptar()).split("'")
remitente = 'traps.warning@gmail.com'
destinatario = 'javier.martinez.carranzaipn@gmail.com'

def attach_file_to_email(email, filename, extra_headers=None):
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())   
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    if extra_headers is not None:
        for name, value in extra_headers.items():
            file_attachment.add_header(name, value)
    email.attach(file_attachment)

email = MIMEMultipart()
email['From'] = remitente
email['To'] = destinatario
email['Subject'] = 'Correo con imagen en el cuerpo del mensaje'
email.attach(MIMEText(Formato.html, "html"))

attach_file_to_email(email, 'fig08.png', {'Content-ID': '<myimageid>'})
attach_file_to_email(email, "fig08.png")

smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente,password[1])
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()

