# Správca úloh 2 (Task Manager V2.0) — Python + MySQL

Jednoduchý správca úloh napísaný v Pythone s využitím MySQL databázy. Tento projekt umožňuje pridávať, zobrazovať, aktualizovať a odstraňovať úlohy cez textové menu.

Úlohy sú teraz uložené v databázovej tabuľke ukoly, takže sa zachovávajú aj po vypnutí programu.


# Funkcie

Pridať novú úlohu – názov + popis, automatické ID a dátum vytvorenia

Zobraziť všetky úlohy – s poradovým číslom, názvom, popisom, stavom a dátumom

Aktualizovať stav úlohy – možnosť nastaviť stav na nezahájeno, probíhá alebo hotovo

Odstrániť úlohu – podľa ID úlohy

Ukončiť program


# Databázová štruktúra

Tabuľka ukoly:

Stĺpec	    Typ	Popis

id	                INT	Primárny kľúč, auto increment

nazov	            VARCHAR(255)	Názov úlohy

popis	            TEXT	Popis úlohy

stav	            ENUM	Stav úlohy (nezahájené, prebieha, hotovo)

datum_vytvorenia	DATETIME	Dátum a čas vytvorenia úlohy


# Požiadavky

Python 3.6 alebo novší

MySQL server (lokálny alebo vzdialený)

Python knižnica mysql-connector-python (inštalácia: pip install mysql-connector-python)


# Použitie — príklad

Po spustení sa zobrazí menu:

Správca úloh - hlavné menu
1. Pridať novú úlohu
2. Zobraziť všetky úlohy
3. Aktualizovať stav úlohy
4. Odstrániť úlohu
5. Koniec programu
Vyberte možnosť (1-5):