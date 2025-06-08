import dbscript
import os
dbs=dbscript
Databse=input("Datenbank verbinden (wenn nicht existiert dann wird erstellt): ")
dbs.dbui(dbn=Databse)
os.system('cls')
print("Datenbank verbunden! exit für exit")
while True:
    ocae=0
    io=input("SQL: ")
    io2=io.lower()
    if io2=="exit":
        break
    if io2=="cls":
        os.system('cls')
        ocae=1
    if io2=="file":
        io=input("Name? ")
        try:
            querys=list()
            with open(io,'r') as sqlfile:
                rawfile=sqlfile.read().strip()
                querys=rawfile.split(";")
            for query in querys:
                if not query=="\n":
                    dbs.dbui(dbn=Databse, query=query+";")
        except:
            print("Datei geht nicht.")
        ocae=1
    if ocae==0:
        dbs.dbui(Databse,io)