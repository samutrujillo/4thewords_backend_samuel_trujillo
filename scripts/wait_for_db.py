import time
import mysql.connector
from app.core.config import settings

def wait_for_db():
    while True:
        try:
            conn = mysql.connector.connect(
                host="mysql_db",
                user=settings.DATABASE_URL.split("//")[1].split(":")[0],
                password=settings.DATABASE_URL.split(":")[2].split("@")[0],
                database=settings.DATABASE_URL.split("/")[-1]
            )
            conn.close()
            print("✅ Database is ready!")
            break
        except mysql.connector.Error:
            print("⏳ Waiting for database to be ready...")
            time.sleep(2)

if __name__ == "__main__":
    wait_for_db()
