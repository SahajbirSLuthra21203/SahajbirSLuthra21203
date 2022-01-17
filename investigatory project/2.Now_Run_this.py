#PART-2

import mysql.connector as m
import datetime as dt
from time import sleep
date=dt.date.today()
db=m.connect(host="localhost",user="root",passwd="tiger",database="artint")
cur=db.cursor()

def data():
    l=[("icode","iname","qty","price","vendor","doa","next_delivery")]
    cur.execute("select * from stationary")
    rec=cur.fetchall()
    for i in rec:
        l.append(i)
    return l
    
#the functions we use are:
#1.ADD NEW PRODUCTS
def add_new():
    n=int(input("enter the no. of new products:"))
    for i in range(n):
        print()
        print(f'enter the information of item {i+1}')
        icode=int(input("enter the item code:"))
        iname=input("enter the item name:")
        qty=int(input("enter the quantity:"))
        price=int(input("enter the price per unit(Rs):"))
        vend=input("enter the vendor name:")
        y=input("is the date of arrival today?:(y/n)")
        if y in ["y","Y"]:
            doa=dt.date.today()
        else:
            doa=input("enter the date of arrival(yyyy-mm-dd):")
        nd=input("enter the next date of delivery(yyyy-mm-dd):") 
        stmt=f"insert into stationary values({icode},'{iname}',{qty},{price},'{vend}','{doa}','{nd}')"
        cur.execute(stmt)
        db.commit()

#2.DISPLAY THE LIST
def display():
    cur.execute("select * from stationary")
    rec=cur.fetchall()
    l=("icode","iname","qty","price","vendor","doa","next_delivery")
    for i in l:
        print(i,end="\t")
    print()
    for i in rec:
        for j in i:
            print(j,end="\t")
        print()

#3.CHANGE EXISTING RECORDS:
def change():
    icode=int(input("enter the icode of the product to change:"))
    print("enter the option no. of the column you want to change:")
    print("1.Item Name")
    print("2.Quantity")
    print("3.Price")
    print("4.Vendor Name")
    print("5.Date of arrival")
    print("6.Next Delivery")
    print()
    a=int(input("enter option here-->"))
    if a==1:
        iname=input("enter the new name:")
        cur.execute(f"update stationary set iname='{iname}' where icode={icode}")
        db.commit()
        print("record changed")

    elif a==2:
        qty=int(input("enter the new quantity:"))
        cur.execute(f"update stationary set quantity={qty} where icode={icode}")
        db.commit()
        print("record changed")

    elif a==3:
        price=int(input("enter the new price:"))
        cur.execute(f"update stationary set price_unit={price} where icode={icode}")
        db.commit()
        print("record changed")

    elif a==4:
        vendor=input("enter the new name of vendor:")
        cur.execute(f"update stationary set vendor='{vendor}' where icode={icode}")
        db.commit()
        print("record changed")

    elif a==5:
        year=input("enter new year(yyyy):")
        month=input("enter new month(mm):")
        day=input("enter new day(dd):")
        yyyy=int(year)
        mm=int(month)
        dd=int(day)
        new=dt.date(yyyy,mm,dd)
        cur.execute(f"update stationary set date_of_arrival='{new}' where icode={icode}")
        db.commit()
        print("record changed")

    elif a==6:
        year=input("enter new year(yyyy):")
        month=input("enter new month(mm):")
        day=input("enter new year(dd):")
        yyyy=int(year)
        mm=int(month)
        dd=int(day)
        new=dt.date(yyyy,mm,dd)
        cur.execute(f"update stationary set next_delivery='{new}' where icode={icode}")
        db.commit()
        print("record changed")
    else:
        print("invalid input")

#4.SEARCH:
def search():
    print("enter the option number on the basis of which you want to search:")
    print("1.Item code")
    print("2.Item Name")
    print("3.Quantity")
    print("4.Price")
    print("5.Vendor Name")
    print("6.Date of arrival")
    print("7.Next Delivery")
    print()
    a=int(input("enter option here-->"))
    if a==1:
        icode=int(input("enter the item code:"))
        print(("icode","iname","qty","price","vendor","doa","next_delivery"))
        for i in range(1,len(data())):
            if icode==data()[i][0]:
                print(data()[i])

    elif a==2:
        iname=input("enter the item name:")
        print(("icode","iname","qty","price","vendor","doa","next_delivery"))
        for i in range(1,len(data())):
            if iname==data()[i][1]:
                print(data()[i])
    elif a==3:
        qty=int(input("enter the quantity:"))
        print(("icode","iname","qty","price","vendor","doa","next_delivery"))
        for i in range(1,len(data())):
            if qty==data()[i][2]:
                print(data()[i])

    elif a==4:
        price=int(input("enter the price:"))
        print(("icode","iname","qty","price","vendor","doa","next_delivery"))
        for i in range(1,len(data())):
            if price==data()[i][3]:
                print(data()[i])
    elif a==5:
        vendor=input("enter the vendor's name:")
        print(("icode","iname","qty","price","vendor","doa","next_delivery"))
        for i in range(1,len(data())):
            if vendor==data()[i][4]:
                print(data()[i])
    elif a==6:
        year=input("enter new year(yyyy):")
        month=input("enter new month(mm):")
        day=input("enter new day(dd):")
        print(("icode","iname","qty","price","vendor","doa","next_delivery"))
        yyyy=int(year)
        mm=int(month)
        dd=int(day)
        new=dt.date(yyyy,mm,dd)
        for i in range(1,len(data())):
            if vendor==data()[i][5]:
                print(data()[i])
    elif a==7:
        year=input("enter new year(yyyy):")
        month=input("enter new month(mm):")
        day=input("enter new day(dd):")
        print(("icode","iname","qty","price","vendor","doa","next_delivery"))
        yyyy=int(year)
        mm=int(month)
        dd=int(day)
        new=dt.date(yyyy,mm,dd)
        for i in range(1,len(data())):
            if vendor==data()[i][6]:
                print(data()[i])
    else:
        print("invalid input")

#5.NEW ARRIVAL:
def new_arrival():
    n=int(input("enter the no. of type of products:"))
    for i in range(n):
        print(f"for item no. {i+1},is it new?(y/n)")
        confirm=input("enter here-->")
        if confirm in ["y","Y"]:
            print(f'enter the information of item {i+1}:')
            icode=int(input("enter the item code:"))
            iname=input("enter the item name:")
            qty=int(input("enter the quantity:"))
            price=int(input("enter the price per unit(Rs):"))
            vend=input("enter the vendor name:")
            doa=dt.date.today()
            nd=input("enter the next date of delivery(yyyy-mm-dd):") 
            stmt=f"insert into stationary values({icode},'{iname}',{qty},{price},'{vend}','{doa}','{nd}')"
            cur.execute(stmt)
            db.commit()
        elif confirm in ["n","N"]:
            icode=int(input("pls enter the icode of the product to change:"))
            qty=int(input("enter the quantity:"))
            for i in range(1,len(data())):
                if icode==data()[i][0]:
                    qty+=data()[i][2]
            cur.execute(f"update stationary set quantity={qty} where icode={icode}")
            db.commit()
            new=dt.date.today()
            cur.execute(f"update stationary set date_of_arrival='{new}' where icode={icode}")
            db.commit()
            year=input("enter the year(yyyy) for next delivery:")
            month=input("enter new month(mm) for next delivery:")
            day=input("enter new day(dd) for next delivery:")
            yyyy=int(year)
            mm=int(month)
            dd=int(day)
            new=dt.date(yyyy,mm,dd)
            cur.execute(f"update stationary set next_delivery='{new}' where icode={icode}")
            db.commit()
            print("record(s) added/changed")

#6.PURCHASE:
def purchase():
    bill=[["Sno.","iname","qty","price"]]
    total=0
    n=int(input("enter the no. of types of products purchased:"))
    for i in range(n):
        print()
        print(f"enter the info. for item no. {i+1}")
        icode=int(input("enter the item code:"))
        qty=int(input("enter the quantity of the item purchased:"))
        for j in range(1,len(data())):
            if icode==data()[j][0]:
                
                new=(data()[j][2])-qty
                if new < 0:
                    print("quantity not available")
                    inn=input("do you still want to purchase the product of this quantity?(y/n):")
                    if inn in ["y","Y"]:
                        new=data()[j][2]
                        qty=data()[j][2]
                        cur.execute(f"update stationary set quantity=0 where icode={icode}")
                        
                elif new==0:
                    cur.execute(f"update stationary set quantity=0 where icode={icode}")
                    print(f"NOTE: no. of {data()[j][1]} present=0")
                else:
                    cur.execute(f"update stationary set quantity={new} where icode={icode}")
                db.commit()
                bill+=[[(i+1),data()[j][1],qty,qty*(data()[j][3])]]
                total+=qty*(data()[j][3])
                
                    
    print("BILL:")
    for k in bill:
        print(k)
        print()
    print("Total AMOUNT=",total)

#7.DELETE RECORDS
def delete():
    print("enter the option number on the basis of which you want to delete:")
    print("1.Item code")
    print("2.Item Name")
    print("3.Quantity")
    print("4.Price")
    print("5.Vendor Name")
    print("6.Date of arrival")
    print("7.Next Delivery")
    print()
    a=int(input("enter option here-->"))
    if a==1:
        icode=int(input("enter the item code:"))
        cur.execute(f"delete from stationary where icode={icode}")
        db.commit()
        print("record changed")

    elif a==2:
        iname=input("enter the item name:")
        cur.execute(f"delete from stationary where iname='{iname}'")
        db.commit()
        print("record changed")

    elif a==3:
        qty=int(input("enter the quantity:"))
        cur.execute(f"delete from stationary where quantity={qty}")
        db.commit()
        print("record changed")

    elif a==4:
        price=int(input("enter the item code:"))
        cur.execute(f"delete from stationary where price={price}")
        db.commit()
        print("record changed")

    elif a==5:
        vendor=input("enter the vendor name:")
        cur.execute(f"delete from stationary where vendor='{vendor}'")
        db.commit()
        print("record changed")

    elif a==6:
        year=input("enter year(yyyy):")
        month=input("enter month(mm):")
        day=input("enter day(dd):")
        yyyy=int(year)
        mm=int(month)
        dd=int(day)
        new=dt.date(yyyy,mm,dd)
        cur.execute(f"delete from stationary where date_of_arrival='{new}'")
        db.commit()
        print("record changed")

    elif a==6:
        year=input("enter year(yyyy):")
        month=input("enter month(mm):")
        day=input("enter day(dd):")
        yyyy=int(year)
        mm=int(month)
        dd=int(day)
        new=dt.date(yyyy,mm,dd)
        cur.execute(f"delete from stationary where next_delivery='{new}'")
        db.commit()
        print("record changed")
    else:
        print("invalid input")

def notify(today):
    l=[data()[0]]
    for i in range(1,len(data())):
        if today== data()[i][6]:
            print(f"NOTE:-Delivery for {data()[i][1]} scheduled for today(IGNORE if product(s) delivered).")
            print()
    print()
    
#menu
try:
    print('Welcome to "Stationery Shop Database Management System"')
    sleep(1)
    print("A Project by Sahajbir Singh Luthra")
    print("Class XII-D")
    print("Roll No. 14744830")
    print()
    sleep(1)
    print("OBJECTIVE:To form a program capable of managing a stationery shop database\
 using python,MySQL and MySQL connectivity with python")
    sleep(1)
    print()
    print("here are the tasks you can perform:")
    x=True
    while x:
        sleep(1)
        notify(dt.date.today())
        print("1.DISPLAY the contents of the table")
        print("2.ADD new products")
        print("3.CHANGE any existing records")
        print("4.NEW ARRIVAL")
        print("5.SEARCH in existing records")
        print("6.PURCHASE")
        print("7.DELETE from existing records")
        r=int(input("enter option number-->"))
        if r==1:
            display()
        elif r==2:
            add_new()
        elif r==3:
            change()
        elif r==4:
            new_arrival()
        elif r==5:
            search()
        elif r==6:
            purchase()
        elif r==7:
            delete()
        print()
        print()
        inu=input("do you still want to continue?(y/n)")
        print()
        if inu in ["n","N"]:
            x=False
            sleep(1)
            print("Thank You")
            exit()
except:
    print("something wrong occurred")
    print("please try again")
    exit()
        
        
        
