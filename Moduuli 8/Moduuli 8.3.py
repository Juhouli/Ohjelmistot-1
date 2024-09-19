import mysql.connector
import geopy.distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Kahvia666',
         autocommit=True
         )

icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
sql1 = f"SELECT latitude_deg, longitude_deg FROM airpot WHERE ident = '{icao1}'"
kursori1 = yhteys.cursor()
kursori1.execute(sql1)
tulos1 = kursori1.fetchall()
for rivi1 in tulos1:
    lat1= rivi1[0]
    lon1= rivi1[1]
airport1 = (lat1,lon1)

icao2 = input("Anna toisen lentokentän ICAO-koodi: ")
sql2 = f"SELECT latitude_deg, longitude_deg FROM airpot WHERE ident = '{icao2}'"
kursori2 = yhteys.cursor()
kursori2.execute(sql2)
tulos2 = kursori2.fetchall()
for rivi2 in tulos2:
    lat2= rivi2[0]
    lon2= rivi2[1]
airport2 = (lat2,lon2)

print(geopy.distance.ditance(airport1,airport2).km)