import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty",
    database="mydatabase"
)

def insert_record(web_site:str, user_login:str, user_pass:str)->None:
    mycursor = mydb.cursor()
    mycursor.execute('')
    sql = "INSERT INTO pass_manager (website, login, my_password) VALUES (%s, %s, %s)"
    val = (web_site, user_login, user_pass)

    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

    print(mycursor.rowcount, "record inserted.")

def show_selected_record(web_site, user_login)->None:
    mycursor = mydb.cursor()
    if web_site != '' or user_login != '':
        if web_site != '' and user_login != '':
            sql = "SELECT * FROM pass_manager WHERE website = '%s' AND login = '%s"
            val = (web_site, user_login)
        elif web_site == '' and user_login != '':
            sql = "SELECT * FROM pass_manager WHERE login = '%s"
            val = (user_login)
        elif web_site != '' and user_login == '':
            sql = "SELECT * FROM pass_manager WHERE website = '%s'"
            val = (web_site)
        mycursor.execute(sql, val)
    else:
        mycursor.execute("SELECT * FROM pass_manager")

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
def show_all_records():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM pass_manager")
    myresult = mycursor.fetchall()
    return myresult

