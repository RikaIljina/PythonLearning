import mysql.connector
from mysql.connector import errorcode
import csv

csv_folder = r''                        # add folder here

print(mysql.connector)


mydb = mysql.connector.connect(
host="localhost",
port="3306",
user="root",
password="",                            # add password
database="plantsapp",
)

my_cursor = mydb.cursor(buffered=True)
my_cursor.execute("SHOW DATABASES")


#my_cursor.execute("CREATE DATABASE PlantsApp")
#my_cursor.execute("SHOW DATABASES")


def insert_into_plant_family_table():
    with open(csv_folder+'\Plant_Family_Table.csv', 'r', encoding='utf-8', newline='') as csv_file:
        next(csv_file)
        cf = csv.reader(csv_file, delimiter=';', quotechar='"')
        for line in cf:
            print(line[0])
            my_cursor.execute("INSERT INTO plant_family_table (PlantType) VALUES(%s)", (line[0],))
            mydb.commit()

    my_cursor.execute("SELECT * FROM Plant_Family_Table")
    result = my_cursor.fetchall()
    print(result)


def create_plant_database_table():
    my_cursor.execute("CREATE TABLE plant_database (PlantID INTEGER AUTO_INCREMENT PRIMARY KEY, PlantName VARCHAR(40), "
                      "PlantTypeID INTEGER REFERENCES plant_family_table(PlantTypeID), GoodNeighbours TEXT, "
                      "BadNeighbours TEXT, SowDateInStart DATE, SowDateInEnd DATE, SowDateOutStart DATE, "
                      "SowDateOutEnd DATE, PlantOutDate DATE, HarvestDateStart DATE, HarvestDateEnd DATE,"
                      "Comment TEXT)")

    my_cursor.execute("SELECT * FROM plant_database")
    result = my_cursor.fetchall()
    print(result)


def insert_into_plant_database_table():
    my_cursor.execute("ALTER TABLE plant_database AUTO_INCREMENT = 1")
    with open(csv_folder + '\plant_database.csv', 'r', encoding='utf-8', newline='') as csv_file:
        next(csv_file)
        cf = csv.reader(csv_file, delimiter=';', quotechar='"')
        for line in cf:
            lines = []
            for i in range(1, 13):
                lines.append(line[i] if line[i] is not '' else None)

            lines_tuple = tuple(lines)

            my_cursor.execute("INSERT INTO plant_database (PlantName, PlantTypeID_fk, GoodNeighbours, BadNeighbours, "
                              "SowDateInStart, SowDateInEnd, SowDateOutStart, SowDateOutEnd, PlantOutDate, "
                              "HarvestDateStart, HarvestDateEnd, Comment) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, "
                              "%s, %s, %s)", lines_tuple)

            mydb.commit()

#insert_into_plant_database_table()


def create_varieties_table():

    my_cursor.execute("CREATE TABLE variety_database (SortID INTEGER AUTO_INCREMENT PRIMARY KEY, PlantTypeID_fk "
                      "INTEGER REFERENCES plant_family_table(PlantTypeID), PlantID_fk INTEGER REFERENCES "
                      "plant_database(PlantID), PlantName VARCHAR(40), PlantSort VARCHAR(50), LastHarvest DATE, "
                      "AvgHarvest INTEGER(6), PlantHarvestRatio FLOAT(6,2), GermRate FLOAT(6,2), GermTime INTEGER, "
                      "FirstHarvestTime DATE, MinTempOutside FLOAT(2,2), MinTempGreenhouse FLOAT(2,2), SowDateIn DATE, "
                      "SowDateOut DATE, PlantOutDate DATE, Comment TEXT, Property TEXT)")

    mydb.commit()
    my_cursor.execute("SELECT * FROM variety_database")
    result = my_cursor.fetchall()
    print(result)

# create_varieties_table()


def insert_into_varieties_table():
    my_cursor.execute("ALTER TABLE variety_database AUTO_INCREMENT = 1")
    with open(csv_folder + '\sorts_database.csv', 'r', encoding='utf-8', newline='') as csv_file:
        next(csv_file)
        cf = csv.reader(csv_file, delimiter=';', quotechar='"')
        for line in cf:
            print(line)
            lines = []
            for i in range(1, 18):
                if i == 1:
                    ex_statement = "SELECT PlantTypeID_fk FROM plantsapp.plant_database WHERE PlantID = %s"
                    value = int(line[2])
                    insert_value = (value,)
                    print(insert_value)
                    my_cursor.execute(ex_statement, insert_value)
                    result = my_cursor.fetchall()
                    print(result)
                    lines.append(result[0][0])
                    continue
                if i == 2:
                    lines.append(int(line[2]))
                    continue
                lines.append(line[i] if line[i] is not '' else None)
                print(lines)

            lines_tuple = tuple(lines)

            print(lines_tuple, len(lines_tuple))

            my_cursor.execute("INSERT INTO variety_database (PlantTypeID_fk, PlantID_fk, PlantName, PlantSort, "
                              "LastHarvest, AvgHarvest, PlantHarvestRatio, GermRate, GermTime, FirstHarvestTime, "
                              "MinTempOutside, MinTempGreenhouse, SowDateIn, SowDateOut, PlantOutDate, Comment,"
                              "Property) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                              lines_tuple)



            mydb.commit()


#insert_into_varieties_table()


def create_plantbase_table():

    my_cursor.execute("CREATE TABLE plantbase (BasePlantID INTEGER AUTO_INCREMENT PRIMARY KEY, PlantTypeID_fk INTEGER(4),"
                      " PlantID_fk INTEGER(4), PlantSort_fk INTEGER(4), AmountBought INTEGER(5), Price INTEGER(4), "
                      "AmountHarvested INTEGER(6))")
    my_cursor.execute("ALTER TABLE plantbase AUTO_INCREMENT = 1")

    mydb.commit()
    my_cursor.execute("SELECT * FROM plantbase")
    result = my_cursor.fetchall()
    print(result)

#create_plantbase_table()


def insert_into_plantbase_table():
    my_cursor.execute("ALTER TABLE plantbase AUTO_INCREMENT = 1")
    with open(csv_folder + '\plantbase.csv', 'r', encoding='utf-8', newline='') as csv_file:
        next(csv_file)
        cf = csv.reader(csv_file, delimiter=';', quotechar='"')
        for line in cf:
            print(line)
            lines = []
            for i in range(1, 7):
                if i == 1:
                    ex_statement = "SELECT PlantTypeID FROM plantsapp.plant_family_table WHERE PlantType = %s"
                    value = str(line[1])
                    insert_value = (value,)
                    print(insert_value)
                    my_cursor.execute(ex_statement, insert_value)
                    result = my_cursor.fetchall()
                    print(result)
                    lines.append(result[0][0])
                    continue
                if i == 2:
                    ex_statement = "SELECT PlantID FROM plantsapp.plant_database WHERE PlantName = %s"
                    value = str(line[2])
                    insert_value = (value,)
                    print(insert_value)
                    my_cursor.execute(ex_statement, insert_value)
                    result = my_cursor.fetchall()
                    print(result)
                    lines.append(result[0][0])
                    continue
                if i == 3:
                    if line[3] is not "":
                        ex_statement = "SELECT SortID FROM plantsapp.variety_database WHERE PlantSort = %s"
                        value = str(line[3])
                        insert_value = (value,)
                        print(insert_value)
                        my_cursor.execute(ex_statement, insert_value)
                        result = my_cursor.fetchall()
                        print(result)
                        lines.append(result[0][0])
                    else:
                        lines.append(None)
                    continue
                lines.append(line[i] if line[i] is not '' else None)
                print(lines)

            lines_tuple = tuple(lines)

            print(lines_tuple, len(lines_tuple))

            my_cursor.execute("INSERT INTO plantbase (PlantTypeID_fk, PlantID_fk, PlantSort_fk, AmountBought, Price, "
                              "AmountHarvested) VALUES (%s, %s, %s, %s, %s, %s)",
                              lines_tuple)

            mydb.commit()


insert_into_plantbase_table()

my_cursor.close()
mydb.close()




# QR code for each plant and variety to scan with app
