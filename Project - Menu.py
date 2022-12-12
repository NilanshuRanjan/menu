import mysql.connector as mc

db = mc.connect(host="localhost", user="root",
                password="nilanshu123A",
                database="restaurant")
cur = db.cursor()

user_type = input("enter O if ur owner and C if a customer")


def owner():
    while True:

        if input("\npress n to logout") == "n":
            break

        work = input("enter 1 to create a menu"
                     "\nenter 2 to view the menu"
                     "\nenter 3 to add a row in the menu"
                     "\nenter 4 to remove a item from the menu: ")
        print("")
        if work == "1":
            cur.execute("create table menu(sno int(3), dish varchar(20), price integer)")
            print("Menu table made successfully")
            db.commit()
        if work == "2":
            cur.execute("Select * from menu")
            table = cur.fetchall()
            for i in table:
                print(i, "\n")
        if work == "3":
            while True:
                sno = input("\nenter the serial number of the dish: ")
                dname = input("enter the name of the dish: ")
                price = input("enter the price of the dish: ")
                val = (sno, dname, price)
                cur.execute("insert into menu values(%s,%s,%s)", val)
                print("Row added successfully")
                db.commit()
                if input("press n to stop adding: ") == "n":
                    break
        if work == "4":
            while True:
                dishn = int(input("\nenter the dish sno that is to be removed: "))
                cur.execute("delete from menu where sno='%d'" % dishn)
                print("data removed successfully")
                db.commit()
                if input("press n to stop removing items: ") == "n":
                    break


def customer():
    print("\nWelcome to our beloved restaurant\n")
    cur.execute("select * from menu")
    rec = cur.fetchall()
    for i in rec:
        print(i)
    bill = []
    while True:
        order = int(input("\nWhat would you like to have sir: "))
        amt = int(input("how much would you like to have sir: "))
        for i in rec:
            if i[0] == order:
                bill.append([i[1], amt, amt * i[2]])

        if input("press n to stop ordering: ") == "n":
            break
    print("\nYour bill sir\n")
    total = 0
    # print(bill)
    for i in bill:
        print(i[0], " | ", i[1], " | ", "$", i[2])
        total = total + i[2]
    print("\nTotal cost is = $", total)
    print("# Soaf ke paise alag se lagenge #")
    print("\n Thanks for visiting")


if user_type == "o":
    pw = int(input("enter the password: "))
    if pw == 10001:
        owner()
    else:
        print("Call the police we have an intruder")

elif user_type == "c":
    customer()

else:
    print("Get out of here weirdo")
