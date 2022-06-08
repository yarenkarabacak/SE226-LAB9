import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "PASSW123."
)
cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS MyNewDatabase")

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = 'MyNewDatabase',
    passwd = "Emine_belis.123")

if connection.is_connected():
    db_Info = connection.get_server_info()
    print("Connected to MySQL Server versşon", db_Info)
    cursor = connection.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database='MyNewDatabase',
        passwd="Emine_belis.123")

    mySql_Create_Table_Query = """ CREATE TABLE IF NOT EXISTS MyMovieTable(
                                    Id int(40) NOT NULL,
                                    Movie VARCHAR(50) NOT NULL,
                                    Date VARCHAR(50) NOT NULL,
                                    MCU_Phase VARCHAR(50))"""
    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("MyMovieTable created successfully")

    path = open('//Users//yarenkarabacak//Desktop//Marvel.txt','r')

    mysql_insert_query = """ INSERT INTO MyMovieTable (Id, Movie, Date,
                                                  MCU_Phase) VALUES(%s,%s,%s,%s)"""

    #for line in y:
    #   words = line.split()
    #   records = (words[0],words[1],words[2],words[3])
    #   cursor.execute(mysql_insert_query, records)


    # insertion from file to database
    while path:
        marvel = path.readline()
        if marvel == "":
            break
        splitLines = marvel.split()
        mysql_insert_query = """INSERT INTO Marvel(ID,MOVIE,DATE,MCU_PHASE) VALUES (%s,%s,%s,%s)"""
        record = (splitLines[0], splitLines[1], splitLines[2], splitLines[3])
        cursor.execute(mysql_insert_query, record)
        dataBase.commit()

    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into MyMovieTable")


    #print all
    query = "SELECT * FROM Marvel"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


    #delete movie
    q = "DELETE FROM Marvel WHERE MOVIE = 'TheIncredibleHulk'"
    cursor.execute(q)
    dataBase.commit()

    #print phase2
    query = "SELECT * FROM Marvel WHERE MCU_PHASE = 'Phase2'"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    #changing Thor date
    query = "UPDATE Marvel SET DATE = 'November3,2017' WHERE MOVIE = 'Thor:Ragnarok'"
    cursor.execute(query)
    dataBase.commit()


except mysql.connector.Error as error:
    print("Something went wrong in MySQL: {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")



