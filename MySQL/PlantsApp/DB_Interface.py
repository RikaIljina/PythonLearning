import mysql.connector


class DB_Interface:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            database="plantsapp"
        )

        self.my_cursor = self.mydb.cursor(buffered=True)

    def check_databases(self):
        self.my_cursor.execute("SHOW TABLES")
        self.mydb.commit()
        print(self.my_cursor.fetchall())

    def get_plant_types(self):
        self.my_cursor.execute("SELECT PlantType, PlantTypeID FROM plant_family_table")
        self.mydb.commit()
        return self.my_cursor.fetchall()

    def get_plants(self, pt_id):
        self.my_cursor.execute("SELECT PlantName FROM plant_database WHERE PlantTypeID_fk = %s", (pt_id, ))
        self.mydb.commit()
        return self.my_cursor.fetchall()

    def get_neighbours(self, plant_name):
        self.my_cursor.execute("SELECT GoodNeighbours FROM plant_database WHERE PlantName = %s", (plant_name,))
        self.mydb.commit()
        return self.my_cursor.fetchall()
