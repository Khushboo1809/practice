#! C:\Users\kumar\AppData\Local\Programs\Python\Python311\python.exe
import cgi
import mysql.connector
print("content-type: text/html\r\n\r\n")
con = mysql.connector.connect(
    host="localhost", user="learnKhushi", password="learnKhushi", database="practice")
f = cgi.FieldStorage()
t = con.cursor
d1 = f.getvalue('t1')
try:
    var = f.getvalue('t1')
    if var == 'insert':
        a1: f.getvalue('')
        a1: f.getvalue('')
        a1: f.getvalue('')
        a1: f.getvalue('')
except Exception as e:

    print("error", e)
