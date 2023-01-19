from email.message import EmailMessage
import Encriptado
import smtplib

Encriptado.generar()
password = (str)(Encriptado.desencriptar()).split("'")

remitente = "traps.warning@gmail.com"   #Correo configurado
destinatario = "javier.martinez.carranzaipn@gmail.com"  #Correo destino
mensaje = "Problema sucedido con la trap"   #Cuerpo del mensaje

email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Se ha activado una trap"
email.set_content(mensaje)

smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente, password[1])
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()

