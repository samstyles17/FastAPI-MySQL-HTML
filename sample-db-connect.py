import pymysql

# Connect to MySQL
def connect_to_mysql(host, user, password, database):
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if conn.open:
            print('Connected to MySQL database')
            return conn
    except pymysql.Error as e:
        print(f'Error connecting to MySQL: {e}')
        return None

# Close connection
def close_connection(conn):
    if conn:
        conn.close()
        print('Connection closed')

# Example usage
if __name__ == "__main__":
    # Replace these values with your MySQL credentials
    HOST = 'localhost'
    USER = 'harsh'
    PASSWORD = '123456789'
    DATABASE = 'easyapply_test'

    # Connect to MySQL
    conn = connect_to_mysql(HOST, USER, PASSWORD, DATABASE)

    # Close connection
    close_connection(conn)
