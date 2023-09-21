#! C:\Users\kumar\AppData\Local\Programs\Python\Python311\python.exe
import cgi
import mysql.connector
print("content-type: text/html\r\n\r\n")
con = mysql.connector.connect(
    host="localhost", user="learnKhushi", password="learnKhushi", database="practice")
f = cgi.FieldStorage()
t = con.cursor()
dd = f.getvalue('t1')
# print(con)
try:
    var = f.getvalue('t1')
    # print(var)
    if var == 'insert':
        w1 = f.getvalue('x1')
        w2 = f.getvalue('x2')
        w3 = f.getvalue('x3')
        w4 = f.getvalue('x4')
        w5 = f.getvalue('x5')
        # url = "insert into form values(%s,%s,%s,%s)"
        url = "INSERT INTO form (username,uid,password,address,pincode) VALUES (%s,%s,%s,%s,%s)"
        t.execute(url, (w1, w2, w3, w4, w5))
        con.commit()
        print("inserted done")
        #  username,userid, pssword,address and pincode
    # elif dd == 'search':
    #     g1 = f.getvalue('x1')
    #     g2 = f.getvalue('x2')
    #     url = 'select * from form where'
    #     # print(url)

    #     if g1 != None:
    #         url = url + "username= '"+g1+"'"
    #     if g1 == None and g2 != None:
    #         url = url+"username='"+g1+"'"
    #     if g1 != None and g2 == None:
    #         url = url+"userid='"+g2+"'"
    #     t.execute(url)
    #     res = t.fetchall()
    #     print(res)
        # if res == []:
        #     print("Records not found")
        # elif g1 == 'userid':
        #     print('< input id="t1" type="text" / > < br / > < br / > < i class ="fa fa-user" > </i > <label for ="" > password < /label > < input id="t3" type="text" / >< br / > < br / > < i class="fa fa-user" > </i > <label for ="" > Address < /label >< input id="t4" type="textarea" / >< br / > < br / >< i class="fa fa-user" > </i > <label for ="" > PinCode < /label >< input id="t5" type="number" / >< br / > < br / >  < input type="button" value="Update" / > < br / > < br / >')
    elif (dd == 'search'):
        t1 = f.getvalue('x1')
        t2 = f.getvalue('x2')
        url = 'select * from form where '
        if (t1 != None):
            url = url+'username="'+t1+'"'
        if (t2 != None and t1 != None):
            url = url+'and userid="'+t2+'"'
        if (t2 != None and t1 == None):
            url = url+'userid="'+t2+'"'
        t.execute(url)
        rs = t.fetchall()
        if (rs != []):
            b = 0
            print('<table><thead><th>Sno.</th><th>User Name</th><th>User ID</th><th>Password</th><th>Address</th><th>Pincode</th></thead>')
            for a in rs:
                b = b+1
                print('<tr><td>'+str(b)+'</td><td>'+str(a[1])+'</td><td>'+str(a[2])+'</td><td>' +
                      str(a[3])+'</td><td>'+str(a[4])+'</td><td>'+str(a[5])+'</td></tr>')
            print('</table>')
        else:
            print(0)
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
