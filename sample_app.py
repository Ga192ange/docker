import os

from flask import Flask, render_template
import pymysql

sample = Flask(__name__)


@sample.route("/")
def home():
    try:
        # Vamos a intentar conectarnos a la BD
        conn = pymysql.connect(
            host="servidor-bd-082",
            user="root",
            password=os.getenv("MYSQL_ROOT_PASSWORD"),
            database="082_db",
            connect_timeout=3
        )

        conn.close()
        db_status = "Conexion exitosa a la BD!"

    except Exception as e:
        db_status = f"Error en la conexion: {e}"

    return "Error intencional para prueba", 500


if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050, debug=True)