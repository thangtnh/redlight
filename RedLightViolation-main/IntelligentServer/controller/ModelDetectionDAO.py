from ServerDAO import *
import sys

sys.path.insert(0, 'D:/IntelligentSystem/IntelligentServer/entity')
from TrafficLightModel import *
from PlateDetectModel import *
from CharDetectModel import *

def get_traffic_model():
    connection = connect_to_mysql()
    if connection:
        model = TrafficLightModel()
        query = "SELECT * FROM traffic_light_model WHERE isActive = 1;"
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                for row in results:
                    model.set_idDataset(row[0])
                    model.set_name(row[1])
                    model.set_createDate(row[2])
                    model.set_path(row[3])
                    model.set_accuracy(row[4])
                    model.set_precision(row[5])
                    model.set_recall(row[6])
                    model.set_f1score(row[7])
                    model.set_isActive(row[8])
                    model.set_quantitySample(row[9])
                    model.set_idDataset(row[10])

            return model
        except Exception as e:
            # print((str(user.get_idAdmin)))
            print(f"Error: {e}")
            return None
        

def get_plate_model():
    connection = connect_to_mysql()
    if connection:
        model = TrafficLightModel()
        query = "SELECT * FROM plate_detect_model WHERE isActive = 1;"
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                for row in results:
                    model.set_idDataset(row[0])
                    model.set_name(row[1])
                    model.set_createDate(row[2])
                    model.set_path(row[3])
                    model.set_accuracy(row[4])
                    model.set_precision(row[5])
                    model.set_recall(row[6])
                    model.set_f1score(row[7])
                    model.set_isActive(row[8])
                    model.set_quantitySample(row[9])
                    model.set_idDataset(row[10])

            return model
        except Exception as e:
            # print((str(user.get_idAdmin)))
            print(f"Error: {e}")
            return None
        
def get_char_model():
    connection = connect_to_mysql()
    if connection:
        model = TrafficLightModel()
        query = "SELECT * FROM char_detect_model WHERE isActive = 1;"
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()

            if results:
                for row in results:
                    model.set_idDataset(row[0])
                    model.set_name(row[1])
                    model.set_createDate(row[2])
                    model.set_path(row[3])
                    model.set_accuracy(row[4])
                    model.set_precision(row[5])
                    model.set_recall(row[6])
                    model.set_f1score(row[7])
                    model.set_isActive(row[8])
                    model.set_quantitySample(row[9])
                    model.set_idDataset(row[10])

            return model
        except Exception as e:
            # print((str(user.get_idAdmin)))
            print(f"Error: {e}")
            return None
        
        
if __name__ == "__main__":
    model = get_char_model()
    print(model.get_name())