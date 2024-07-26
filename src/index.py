from decouple import config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time
import os

# Configuración del servidor SMTP y la cuenta de correo
smtp_server = 'smtp.gmail.com'  # Servidor SMTP de Gmail
smtp_port = 587  # Puerto utilizado por el servidor SMTP de Gmail
# Dirección de correo electrónico del remitente (extraída de variables de entorno)
sender_email = config('EMAIL')
# Contraseña de la cuenta de correo del remitente (extraída de variables de entorno)
password = config('CLV_EMAIL')

# Destinatario del correo
# Dirección de correo electrónico del destinatario
receiver_email = 'jpineda@viva.com.do'


def send_email():
    """
    Función para enviar un correo electrónico con un archivo adjunto.
    """
    # Crear el mensaje de correo
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Informe Diario Test from Python'

    # Contenido del informe diario
    body = """
Estimado/a [Jhon Doe],

Espero que este correo le encuentre bien.

Adjunto a este mensaje encontrará el informe diario correspondiente a [7/26/2024]. 
El documento adjunto incluye la factura detallada de las actividades realizadas durante el día.

Si tiene alguna pregunta o necesita información adicional, no dude en ponerse en contacto conmigo.

Quedo a su disposición para cualquier consulta.

Atentamente,

Jhon Doe
Developer
Python Company
809-555-6666
www.python.com
jhondoepython@mail.com
        """
    msg.attach(MIMEText(body, 'plain'))

    # Adjuntar el archivo
    # Ruta del archivo a adjuntar
    file_path = os.path.join('documents', 'factura.xlsx')
    attach_file(msg, file_path)

    try:
        # Conectar al servidor SMTP y enviar el correo
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Iniciar la comunicación TLS
        # Iniciar sesión en el servidor SMTP
        server.login(sender_email, password)
        print(server.login(sender_email, password))
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)  # Enviar el correo
        server.quit()  # Cerrar la conexión con el servidor SMTP
        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")


def attach_file(msg, filename):
    """
    Función para adjuntar un archivo a un mensaje de correo electrónico.

    msg: El mensaje de correo electrónico.
    filename: La ruta del archivo a adjuntar.
    """
    try:
        with open(filename, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            f'attachment; filename= {os.path.basename(filename)}')
            msg.attach(part)
    except Exception as e:
        print(f"Error al adjuntar el archivo: {e}")


# Programar el envío diario del correo
schedule.every().day.at("09:00").do(send_email)

# #Diferentes formas para agendar y enviar el correo
# schedule.every(1).minutes.do(send_email) #Cada minuto
# schedule.every().hour.do(send_email) #Cada hora
# schedule.every().day.at("10:30").do(send_email) #Cada dia a X hora
# schedule.every().monday.do(send_email) #Cada Lunes
# schedule.every().wednesday.at("13:15").do(send_email) #Cada miercoles
# schedule.every().day.at("12:42", "Europe/Amsterdam").do(send_email) #Cada dia a cierta hora segun el pais

print("El script está en funcionamiento. Presiona Ctrl + C para detenerlo.")
while True:
    schedule.run_pending()  # Ejecutar las tareas programadas
    time.sleep(1)  # Esperar 1 segundo antes de verificar nuevamente
