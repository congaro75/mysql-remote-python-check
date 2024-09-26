# mysql remote python check
Code python Kết nối mysql từ local tới server

# Cài đặt phần mở rộng

```
pip install mysql-connector-python
```

## Mở file checkremote.py & Khai báo kết nối Mysql server

```
        
        connection = mysql.connector.connect(
            host='123.456.789.1',  # Địa chỉ IP hoặc domain của server MySQL
            user='userdb',      # Tên người dùng MySQL
            password='pass db',        # Mật khẩu MySQL
            database='db name'     # Tên cơ sở dữ liệu
```

## chạy lệnh

```
python checkremote.py
```
