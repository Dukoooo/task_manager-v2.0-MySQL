import mysql.connector  #prepojenie mysql
from dotenv import load_dotenv  # modul python-dotenv (na načítanie .env súboru)
import os  # štandardná knižnica Pythonu (práca s OS a premennými prostredia)


load_dotenv() # spustenie modulu


#pripojenie databázy / servera
try:
    conn = mysql.connector.connect(
         host=os.getenv("DB_HOST"),
         user=os.getenv("DB_USER"),
         password=os.getenv("DB_PASSWORD"),
         database=os.getenv("DB_NAME")
    )
    print("Pripojenie k databáze bolo úspešné.")

except mysql.connector.Error as err:
    print(f"Chyba spojenia: {err}")
    exit()  # Pokiaľ sa nepripojí, vypíše sa chybová hláška a program sa zavrie

# Vytvorenie kurzoru 
cursor = conn.cursor()

try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS testovacia_tabulka (
            id INT AUTO_INCREMENT PRIMARY KEY,
            meno VARCHAR(100),
            vek INT
        )
    ''')
    print("Tabuľka 'testovacia_tabulka' bola vytvorená.")
except mysql.connector.Error as err:
    print(f"Chyba pri vytváraní tabuľky: {err}")

# Uloženie zmien (Dôležité)
conn.commit()

# uzavrenie kurzoru po pripojení
cursor.close()
conn.close()
print("Pripojenie k databáze bolo uzavrené.")
