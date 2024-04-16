from mysql.connector import (connection)

# conectando ao mysql
cnx = connection.MySQLConnection(user='root', password='senha',
    host='127.0.0.1') #host é o defaut do mysql

mycursor = cnx.cursor(buffered=True)

# criando database
mycursor.execute("CREATE DATABASE teste")
mycursor.execute("USE teste")

# criando tabela
mycursor.execute("CREATE TABLE testeTabela (idTabela INT UNIQUE NOT NULL, nome VARCHAR(50), PRIMARY KEY(idTabela))")

# adicionando valores à tabela
sql = "INSERT INTO testeTabela (idTabela, nome) VALUES (%s, %s)"
val = [
        (11, "Games"),
        (12, "Gomes"),
        (13, "Mega Games")
    ]
mycursor.executemany(sql, val)
cnx.commit()

# mostrando tabela
mycursor.execute("SELECT nome FROM testeTabela")

for x in mycursor:
  print(x)

# apagando database e desconectando do mysql
mycursor.execute("DROP DATABASE teste")
cnx.close()