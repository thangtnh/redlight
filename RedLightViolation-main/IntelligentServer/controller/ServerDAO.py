import MySQLdb

db_host = 'localhost'
db_user = 'root'
db_password = '123456789'
db_database = 'server_intelligent_db'

def connect_to_mysql():
    try:
        connection = MySQLdb.connect(host=db_host, user=db_user, password=db_password, db=db_database)
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def close_connection(connection):
    connection.close()