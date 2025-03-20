import pandas as pd
import smtplib
import pyodbc
import yagmail
import keyring
from email.message import EmailMessage

# Configuración de la conexión a SQL Server
server = 'LAPTOP-74G1IJ7R'  # O el nombre de tu servidor desde SSMS
database = 'BancoDB'

conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')

query = """
SELECT TOP 10 cliente_id, nombre, monto, fecha_transaccion
FROM transacciones
ORDER BY fecha_transaccion DESC
"""

df = pd.read_sql_query(query, conn)  
conn.close()

# Guardar los datos en un archivo Excel
file_path = "reporte_transacciones.xlsx"
df.to_excel(file_path, index=False)

# Configuración del correo
email_sender = "@gmail.com"
email_receiver = "@gmail.com"
subject = "Reporte de Transacciones"
body = "Adjunto el reporte de las últimas transacciones."

# Almacenar la contraseña en keyring (Ejecutar esto solo una vez en config.py)
# keyring.set_password("yagmail", email_sender, "tu_contraseña")

# Conectar y enviar correo
yag = yagmail.SMTP(email_sender)  # No necesitas ingresar la contraseña

yag.send(to=email_receiver, subject=subject, contents=body, attachments=file_path)

print("Correo enviado con éxito.")
