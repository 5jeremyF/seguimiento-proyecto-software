import os
import mysql.connector


def connectionBD():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            passwd=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "crud_python"),
            charset="utf8mb4"
        )

        if connection.is_connected():
            return connection

    except mysql.connector.Error as error:
        print(f"No se pudo conectar: {error}")