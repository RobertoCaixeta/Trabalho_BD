import mysql.connector


con = mysql.connector.connect(
    host= 'localhost',
    database='trabalho_bd',
    user='root',
    password='Imcormrorcro123*'
)

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado no banco ", linha)

if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão encerrada")