# Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector


def connectionBD():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="crud_python",
            charset='utf8mb4'
        )

        if connection.is_connected():
            return connection

    except mysql.connector.Error as error:
        print(f"No se pudo conectar: {error}")