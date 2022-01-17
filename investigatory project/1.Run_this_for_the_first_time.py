#Part-1
#Investigatory project
#-By Sahajbir Singh Luthra
#Class 12-D

import mysql.connector as m
db=m.connect(host="localhost",user="root",passwd="tiger",database="artint")
cur=db.cursor()

cur.execute('create table stationary(icode int primary key,iname varchar(255) NOT NULL,quantity int NOT NULL,price_unit int NOT NULL,vendor varchar(125) NOT NULL,date_of_arrival date NOT NULL,next_delivery date NOT NULL)')
db.close()

