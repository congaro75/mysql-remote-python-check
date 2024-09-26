import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Thiết lập kết nối đến MySQL server
        connection = mysql.connector.connect(
            host='123.456.789.1',  # Địa chỉ IP hoặc domain của server MySQL
            user='userdb',      # Tên người dùng MySQL
            password='pass db',        # Mật khẩu MySQL
            database='db name'     # Tên cơ sở dữ liệu
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES")  # Hiển thị các bảng có trong DB
            tables = cursor.fetchall()

            print("Các bảng trong cơ sở dữ liệu:")
            for table in tables:
                print(table[0])

    except Error as e:
        print("Có lỗi xảy ra:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

connect_to_mysql()
