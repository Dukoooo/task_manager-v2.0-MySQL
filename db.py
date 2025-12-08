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
                stav ENUM('nezahájené', 'hotovo', 'prebieha') NOT NULL DEFAULT 'nezahájené',
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


# 04. Zobrazenie úloh

def zobrazit_ulohy(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT id, nazov, popis, stav FROM ulohy
            WHERE stav IN ('nezahájené', 'prebieha')
        """)
        ulohy = cursor.fetchall()
        if not ulohy:
            print("Žiadne úlohy k zobrazeniu.")
        else:
            print("Zoznam úloh :")
            for uloha in ulohy:
                print(f"ID: {uloha[0]}, Názov: {uloha[1]}, Popis: {uloha[2]}, Stav: {uloha[3]}")
    except mysql.connector.Error as err:
            print(f"Chyba pri načítávaní úloh: {err}")


# 6. Aktualizácia stavu úlohy
def aktualizovat_ulohu(conn):
    zobrazit_ulohy(conn)
    cursor = conn.cursor()
    try:
        id_ulohy = int(input("Zadejte ID úlohy, kterú chcete aktualizovať:\n "))
        novy_stav = input("Zadejte nový stav (prebieha/hotovo):\n ").strip().lower()
        if novy_stav not in ['prebieha', 'hotovo']:
            print("Neplatný stav.")
            return

        cursor.execute("SELECT id FROM ulohy WHERE id = %s", (id_ulohy,))
        if cursor.fetchone() is None:
            print("Zadané ID úlohy neexistuje.")
            return

        cursor.execute(
            "UPDATE ulohy SET stav = %s WHERE id = %s",
            (novy_stav, id_ulohy)
        )
        conn.commit()
        print("Úloha bola aktualizovaná.")
    except ValueError:
        print("Zadejte platné číselné ID.")
    except mysql.connector.Error as err:
            print(f"Chyba pri aktualizácii úlohy: {err}")



# uzavrenie kurzoru po pripojení
    cursor.close()
    conn.close()
    print("Pripojenie k databáze bolo uzavrené.")
