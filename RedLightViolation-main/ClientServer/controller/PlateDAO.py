from ClientDAO import *
import sys

sys.path.insert(0, 'D:/TraficRedLight/ClientServer/models')
from Plate import *

def add_plate(plate):
    connection = connect_to_mysql()
    if connection:
        query = "INSERT INTO plate(content, idImage) VALUES (%s, %s)"
        try:
            cursor = connection.cursor()
            cursor.execute(query, (plate.get_content(), plate.get_image().get_idImage()))
            connection.commit()
        except Exception as e:
            # print((str(user.get_idAdmin)))
            print(f"Error: {e}")
            return None
    close_connection(connection)

def get_plate_by_image(image):
    connection = connect_to_mysql()
    plate = Plate()
    if connection:
        query = "SELECT * FROM plate WHERE idImage = %s;"
        try:
            cursor = connection.cursor()
            cursor.execute(query, (str(image.get_idImage()), ))

            results = cursor.fetchall()
            if results:
                for row in results:
                    plate.set_idPlate(row[0])
                    plate.set_content(row[1])
                    plate.set_image(image)
                    return plate
         
        except Exception as e:
            # print((str(user.get_idAdmin)))
            print(f"Error: {e}")
            return None
    close_connection(connection)

def delete_plate():
    pass
