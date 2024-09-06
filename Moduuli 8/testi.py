import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Kahvia666',
         autocommit=True
         )

#Hakee ja palauttaa Goal taulun sisällön
def hae_goal(goal):

    #SQL-koodi, joka halutaan lähettää suoritettavaksi
    sql_kysely = f"select * from goal where name = '{goal}'"

    #Luodaan "kursori", jonka kautta tietokantaa halutaan käyttää
    kursori = yhteys.cursor()

    #Lähetetään kysely suoritettavaksi
    kursori.execute(sql_kysely)

    #Haetaan kyselyn tulos:
    tulos = kursori.fetchall()

    return tulos

#kutsutaan funktiota tietyn goalin hakemiseksi
goalit = hae_goal("HOT")
for g in goalit:
    print(g)