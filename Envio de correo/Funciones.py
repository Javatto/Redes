import smtplib,Encriptado,Formato
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

password = (str)(Encriptado.desencriptar()).split("'")
remitente = 'traps.warning@gmail.com'

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

def mandar_correo(destinatario):
    email = MIMEMultipart()
    email['From'] = remitente
    email['To'] = destinatario
    email['Subject'] = 'Problemas con una interfaz'
    email.attach(MIMEText(Formato.html, "html"))

    attach_file_to_email(email,"fig08.png", {'Content-ID': '<myimageid>'})

    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(remitente,password[1])
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()

