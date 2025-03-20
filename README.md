Este proyecto extrae datos de una base de datos SQL Server, genera un reporte en Excel con las transacciones recientes y lo envía automáticamente por correo electrónico usando Python.


carpeta -Automatizacion (Carpeta del proyecto)
│── carpeta - .venv (Entorno virtual con dependencias)
│── script.py (Script principal de automatización)
│── config.py (Opcional, para credenciales y configuración)
│── requirements.txt (Lista de dependencias)
│── reporte_transacciones.xlsx (Archivo Excel generado con los datos)


 1. Crear el Entorno Virtual
    python -m venv .venv
 2. Activar el Entorno Virtual
    .venv\Scripts\Activate
3. Instalar las Dependencias del Proyecto
   pip install -r requirements.txt



¿Cómo se conecta Python a SQL Server?
Python usa la librería pyodbc para conectarse a SQL Server.
En el código, se establece la conexión y se ejecuta una consulta SQL para extraer los últimos 10 registros

 ¿Cómo se convierte la consulta SQL en un archivo Excel?
Una vez obtenidos los datos en Pandas, se guardan en un archivo Excel usando openpyxl

Se guarda el DataFrame en un archivo Excel llamado reporte_transacciones.xlsx.

¿Cómo se envía el archivo Excel por correo?
Se usa yagmail y keyring para enviar el archivo sin escribir la contraseña en el código.

Programación Automática del Script
Para que el script se ejecute automáticamente todos los días a una hora específica, se puede usar el programador de tareas de Windows 

RESUMEN
Python se conecta a SQL Server y extrae los datos con pyodbc.
Guarda los datos en un archivo Excel con pandas y openpyxl.
Envía el archivo por correo automáticamente usando yagmail y keyring.
Se puede programar para que corra automáticamente todos los días con el programador de tareas de Windows.
