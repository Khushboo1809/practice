#! C:\Users\kumar\AppData\Local\Programs\Python\Python311\python.exe
import cgi
import mysql.connector
print("content-type: text/html\r\n\r\n")
con = mysql.connector.connect(
    host="localhost", user="learnKhushi", password="learnKhushi", database="practice")
# print(con)
t = con.cursor()
try:
    f = cgi.FieldStorage()
    var = f.getvalue('t1')
    # print(var)
    if var == 'insert':
        w1 = f.getvalue('x1')
        w2 = f.getvalue('x2')
        w3 = f.getvalue('x3')
        w4 = f.getvalue('x4')
        # url = "insert into form values(%s,%s,%s,%s)"
        url = "INSERT INTO form (username,uid,password,address,pincode) VALUES (%s,%s,%s,%s,%s)"
        t.execute(url, (w1, w2, w3, w4))
        con.commit()
        print("inserted done")
    else:
        a = f.getvalue('a1')
        b = f.getvalue('a2')
        # url = "select username from form where username=%s and password=%s"
        # t.execute(url, (a, b))
        #  (these two lines are correct and another way of writing this same line is given below)
        url = 'select username from form where username=\'' + \
            str(a)+'\'and password=\''+str(b)+'\''
        # print(url)
        t.execute(url)
        res = t.fetchall()
        if res != '':
            print("successfully loged in")
        else:
            print("username or passwd wrong")
except Exception as e:

    print("error", e)
