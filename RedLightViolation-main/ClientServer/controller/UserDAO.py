from ClientDAO import *
import sys

sys.path.insert(0, 'D:/TraficRedLight/ClientServer/models')
from User import *

def checkLogin(username, password):
    connection = connect_to_mysql()

    if connection:
        user = User()
        query = "SELECT * FROM user WHERE username = %s and password = %s"
        try:
            cursor = connection.cursor()
            cursor.execute(query, (username, password))
            results = cursor.fetchall()

            if results:
                for row in results:
                    user.set_idUser(str(row[0]))
                    user.set_username(str(row[1]))
                    user.set_password(str(row[2]))
                    user.set_fullname(str(row[3]))
                    user.set_email(str(row[4]))
                    user.set_tel(str(row[5]))
            # print(user.get_fullname())
            
            return user
        except Exception as e:
            # print((str(user.get_idAdmin)))
            print(f"Error: {e}")
            return None
    close_connection(connection)

def get_user_by_id(idUser):
    connection = connect_to_mysql()

    if connection:
        user = User()
        query = "SELECT * FROM user WHERE iduser = %s"
        try:
            cursor = connection.cursor()
            cursor.execute(query, (idUser,))
            results = cursor.fetchall()

            if results:
                for row in results:
                    user.set_idUser(str(row[0]))
                    user.set_username(str(row[1]))
                    user.set_password(str(row[2]))
                    user.set_fullname(str(row[3]))
                    user.set_email(str(row[4]))
                    user.set_tel(str(row[5]))
            # print(user.get_fullname())
            
            return user
        except Exception as e:
            # print((str(user.get_idAdmin)))
            print(f"Error: {e}")
            return None
    close_connection(connection)

if __name__ == "__main__":
    # user = checkLogin('huutuan', '1234567')
    user = get_user_by_id('user01')
    # print(user.get_username())