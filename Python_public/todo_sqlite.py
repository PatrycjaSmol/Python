import sqlite3

connection = sqlite3.connect("todoo.db")

#zmienna laczy nas z nowoutworzona baza todo, db=database

def create_table(connection):
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE task(task text)""")
    # potrójny cudzyslow zeby python wzial wszystko co wyrzuci sql
    # jaki string i nie wyrzucilo dzialania programu

    #tworzymy tabele o nazwie task z kolumna o nazwie 
    #task i przechowujaca plik tekstowy

    except:
        pass
    #jak sie nie uda try to idz dalej, wiemy ze jest blad ale nie chcemy nic z tym robic
    #tabela bedzie tworzona tylko przy pierwszym uruchomieniu

def show_tasks(connection):
    cur = connection.cursor()
    cur.execute("""SELECT rowid, task FROM task""")
#wyswietl kolumne task z tabeli task
    result = cur.fetchall()
    #cur.fetchall to wszystkie zwrocne wiersze z tego zapytania
    for row in result:
        print(str(row[0]) + "-" + row[1])
   
    

def add_task(connection):
    print("Dodajemy zadanie")
    task = input("Wpisz treść zadania: ")
    if task == "0":
        print("Powrót do menu")
    else:
        cur = connection.cursor()
        #pobieramy kursor do baazy danych
        cur.execute("""INSERT INTO task(task) VALUES (?)""", (task,))
        connection.commit()
        #zapisywanie trwale do bd
        print("Dodano zadanie!")


def delete_task(connection):
    task_index = int(input("Podaj indeks zadania do usunięcia: "))

    cur = connection.cursor()
    #inicjalizacja kursora w bazie danych
    rows_deleted = cur.execute("""DELETE FROM task WHERE rowid=? """, (task_index, )).rowcount
    #korzystamy funckji liczenia row zeby wiedziec czy jest takie zadanie w bazie
    connection.commit()
    #przekazywanie trwale do bazy

    if rows_deleted == 0:
        print("Takie zadanie nie istnieje!")
    else:
        print("Usunięto zadanie!")

create_table(connection)

while True:

    print()
    print("1. Pokaż zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Wyjdź")

    user_choice = int(input("Wybierz liczbę: "))
    print()

    if user_choice == 1:
            show_tasks(connection)

    if user_choice == 2:
            add_task(connection)

    if user_choice == 3:
            delete_task(connection)

    if user_choice == 4:
            break

    
connection.close()  