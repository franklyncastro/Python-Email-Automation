English
Automated Report Emailer
This application automatically sends report emails.

#-Features

#-Automated email sending
#-Schedule emails at specific intervals
#-Logging and error handling

#-Requirements

#Python 3.7
#smtplib for sending emails
#schedule for scheduling tasks
#dotenv for managing environment variables

#-Installation

#Clone the repository:
sh
Copiar código
git clone https://github.com/yourusername/automated-report-emailer.git
cd automated-report-emailer

Create and activate a virtual environment:
sh
Copiar código
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the dependencies:

sh
Copiar código
pip install -r requirements.txt
Create a .env file and add your email credentials and other configuration variables:
plaintext
Copiar código
EMAIL_HOST=smtp.your-email-provider.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-password
EMAIL_USE_TLS=True
RECIPIENT_EMAIL=recipient@example.com
Usage
Run the application:
sh
Copiar código
python main.py
Check the logs for the status of the email sending process.
Contributing
Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
License
Distributed under the MIT License. See LICENSE for more information.

Español
Envío Automatizado de Correos de Informe
Esta aplicación envía correos de informes de manera automática.

Características
Envío automático de correos electrónicos
Plantillas de correo personalizables
Programación de correos a intervalos específicos
Registro y manejo de errores
Requisitos
Python 3.x
smtplib para enviar correos electrónicos
schedule para programar tareas
dotenv para gestionar variables de entorno
Instalación
Clona el repositorio:
sh
Copiar código
git clone https://github.com/yourusername/automated-report-emailer.git
cd automated-report-emailer
Crea y activa un entorno virtual:
sh
Copiar código
python3 -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
Instala las dependencias:
sh
Copiar código
pip install -r requirements.txt
Crea un archivo .env y añade tus credenciales de correo electrónico y otras variables de configuración:
plaintext
Copiar código
EMAIL_HOST=smtp.tu-proveedor-de-email.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu-email@ejemplo.com
EMAIL_HOST_PASSWORD=tu-contraseña
EMAIL_USE_TLS=True
RECIPIENT_EMAIL=destinatario@ejemplo.com
Uso
Ejecuta la aplicación:
sh
Copiar código
python main.py
Revisa los registros para ver el estado del proceso de envío de correos.
Contribuir
Haz un fork del repositorio
Crea tu rama de funcionalidad (git checkout -b feature/AmazingFeature)
Haz commit de tus cambios (git commit -m 'Add some AmazingFeature')
Haz push a la rama (git push origin feature/AmazingFeature)
Abre un Pull Request
