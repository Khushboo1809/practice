#! C:\Users\91906\AppData\Local\Programs\Python\Python311\python.exe
print('content-type:text/html\r\n\r\n')
import mysql.connector
import cgi
# print('gg')
# import datetime
con=mysql.connector.connect(host="localhost",user="revision1",password="123456",database="rakhi")
# print('kk')
t=con.cursor()
f=cgi.FieldStorage()
try: 
    d=f.getvalue('cond')
    if d=='ent':
        d1=f.getvalue('t1')
        d2=f.getvalue('t2')
        d3=f.getvalue('t3')
        d4=f.getvalue('t4')
        d5=f.getvalue('t5')
        d6=f.getvalue('t6')
        d7=f.getvalue('t7')
        # print(d1,d2,d3,d4,d5,d6,d7)
        url='insert into revision(form_no,taarikh,reg_no,pre_course,stu_name,course_fee,pic) values(%s,%s,%s,%s,%s,%s,%s)'
        # print(url)
        t.execute(url,(d1,d2,d3,d4,d5,d6,d7))
        con.commit()
        print('successufully insert')
    elif(d=='search'):
        d1=f.getvalue('a1')
        d2=f.getvalue('a2')
        url='select * from revision where'
        # print(url)
        if (d1!=None):
            url=url+" form_no='"+d1+"'"
            # print(url)
        if (d2!=None):
            url=url+" reg_no='"+d2+"'"
        if ((d1!=None) and (d2!=None)):
            url=url+" reg_no='"+d2+"'"
        t.execute(url)
        res=t.fetchall()
        # print(res)
        if res!=[]:
            print('<table id="table3"><tr><th id="sn">Sn</th><th>Form_ no</th><th>Date</th><th>Registration no</th><th>Prev. Course</th><th>Student name</th><th>course_fee</th><th>pic<th>Check</th><th>update</th><th>cancle</th><th id="sn"></th></tr><tbody>')
            
            for a in res:
                if(a[7]==None):
                    k='#'
                else:
                    k=a[7].decode()    
                print('<tr><td id="sn">1</td><td data-label="form_no">'+str(a[1])+"  "+'</td><td data-label="Date">'+str(a[2])+"  "+'</td><td data-label="Reg_no">'+str(a[3])+"  "+'</td><td data-label="Prev.course">'+str(a[4])+"  "+'</td><td data-label="stu_name">'+str(a[5])+"  "+'</td><td data-label="course_fee">'+str(a[6])+"  "+'</td><td data-label="pic" style="width:4rem;height:4rem;"><img style="width:100%;height:100%;" src="'+(k)+'">'  '</td><td data-label="Check"><input type="radio" name="a"></td><td data-label="Update" style="color:blue; cursor:pointer;"><i class="fa" id="upd" data-toggle="tooltip" title="Update">&#xf044;</i></td><td data-label="Delete" style="color: red; cursor:pointer;"><i class="fa" id="del" data-toggle="tooltip" title="Cancel">&#10006;</i></td></tr><td class="sn"></td></tr>')
            print('</tbody></table>')
    else:
        print('hhhu')
        
except Exception as e:
    print('unsucesses',e) 