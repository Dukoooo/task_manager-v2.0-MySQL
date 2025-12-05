import mysql.connector  #prepojenie mysql
from dotenv import load_dotenv  # modul python-dotenv (na načítanie .env súboru)
import os  # štandardná knižnica Pythonu (práca s OS a premennými prostredia)
from datetime import datetime

load_dotenv() # spustenie modulu


# 01. pripojenie databázy / servera
def pripojenie_db():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Chyba spojenia: {err}")
        exit()  # Pokiaľ sa nepripojí, vypíše sa chybová hláška a program sa zavrie



# 02. Vytvorenie tabulky ak neexistuje
def vytvorenie_tabulky(conn):
    try:
        cursor = conn.cursor() #vytvorenie kurzora na komunikáciu
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ulohy (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nazov VARCHAR(255) NOT NULL,
                popis TEXT,
                stav ENUM('nezahájeno', 'hotovo', 'probíhá') NOT NULL DEFAULT 'nezahájeno',
                datum_vytvorenia DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        ''')

    # Uloženie zmien (Dôležité)
        conn.commit()
        print("Tabuľka 'testovacia_tabulka' bola vytvorená.")
    except mysql.connector.Error as err:
        print(f"Chyba pri vytváraní tabuľky: {err}")






# 03. Pridanie úlohy
def pridat_ulohu(conn):
    cursor = conn.cursor()
    while True:
        nazov = input("Zadajte názov úlohy:\n ").strip()
        if not nazov:
            print("Názov nesmie byť prázdny.")
            continue

        popis = input("Zadejte popis úlohy:\n ").strip()
        if not popis:
            print("Popis nesmie byť prázdny.")
            continue

        try:
            cursor.execute(
                "INSERT INTO ulohy (nazov, popis) VALUES (%s, %s)",
                (nazov, popis)
            )
            conn.commit()
            print("Úlohy boli úspešne pridané.")
            break
        except mysql.connector.Error as err:
            print(f"Chyba pri pridávaní úlohy: {err}")
            break

# uzavrenie kurzoru po pripojení
    cursor.close()
    conn.close()
    print("Pripojenie k databáze bolo uzavrené.")
