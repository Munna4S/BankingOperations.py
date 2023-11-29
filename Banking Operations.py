print("="*50)
print("\tBanking Operations ")
print("="*50)
print("\t1.Create account")
print("\t2.Deposit")
print("\t3.Withdraw")
print("\t4.View customer information")
print("\t5.View all customer information")
print("\t6.Exit")
print("="*50)
import cx_Oracle
con=cx_Oracle.connect("system/tiger")
cur=con.cursor()
ch=int(input("Enter ur Choice :"))
if ch == 0:
    ro = "create table surendra9(accountnumber int unique,cname varchar(30),bal float(20),address varchar(50))"
    cur.execute(ro)
    con.commit()
else:
    match(ch):
        case 1:
            def updaterecord():
                while (True):
                    try:
                        con = cx_Oracle.connect("system/tiger")
                        cur = con.cursor()
                        # accept Employee Values Dynamically from KBD
                        print("-" * 50)
                        accountnumber = int(input("Enter accountnumber:"))

                        cname = input("Enter customer Name:")
                        bal = float(input("Enter accountbalance:"))
                        address = input("Enter customer address:")
                        print("-" * 50)
                        iq="insert into surendra2 Values(%d,'%s',%f,'%s')"
                        cur.execute(iq %(accountnumber, cname, bal, address))
                        con.commit()

                        print("-" * 50)
                        ch = input("Do u want to create another record(yes/no):")
                        if (ch.lower() == "no"):
                            break
                    except cx_Oracle.DatabaseError as db:
                        print("Prob in DB:", db)
                    except ValueError:
                        print("Don't enter alnums, strs and symbols for enos")
                # main program
            updaterecord()
        case 2:
            def depositamt():
                while (True):
                    try:
                        con = cx_Oracle.connect("system/tiger")
                        cur = con.cursor()
                        # accept Employee Values Dynamically from KBD

                        print("=" * 50)
                        accountnumber = int(input("enter accountnumber:"))
                        deposit = int(input("Enter amount for deposit:"))
                        uq = "update surendra2 set bal=bal+%f where accountnumber=%d"
                        cur.execute(uq % (deposit, accountnumber))
                        con.commit()
                        print("-" * 50)
                        ch = input("Do u want to deposit again(yes/no):")
                        if (ch.lower() == "no"):
                            break
                    except cx_Oracle.DatabaseError as db:
                        print("Prob in DB:", db)
                    except ValueError:
                        print("Don't enter alnums, strs and symbols for enos")

                # main program
            depositamt()
        case 3:
            def withdraw():
                while (True):
                    try:
                        con = cx_Oracle.connect("system/tiger")
                        cur = con.cursor()
                        # accept Employee Values Dynamically from KBD
                        print("=" * 50)
                        accountnumber = int(input("Enter A/c No :"))
                        withdraw = int(input("Enter amount for withdraw:"))
                        sq="select bal from surendra2 where accountnumber=%d"
                        #res1=cur.execute(sq % accountnumber)
                        cur.execute(sq % accountnumber)
                        res1=cur.fetchone()
                        #for bal in res1:
                        #   for bal1 in bal:
                        if res1[0]<withdraw:
                            print("insuf")
                            break

                        uq = "update surendra2 set bal=bal-%f where accountnumber=%d"
                        cur.execute(uq % (withdraw, accountnumber))
                        con.commit()
                        print("-" * 50)
                        ch = input("Do u want to withdraw  again(yes/no):")
                        if (ch.lower() == "no"):
                            break
                    except cx_Oracle.DatabaseError as db:
                        print("Prob in DB:", db)
                    except ValueError:
                        print("Don't enter alnums, strs and symbols for enos")
                # main program
            withdraw()
        case 4:
            def showcusrecord():
                while (True):
                    try:
                        con = cx_Oracle.connect("system/tiger")
                        cur = con.cursor()
                        # accept Employee Values Dynamically from KBD
                        print("=" * 50)
                        accountnumber = int(input("Enter account number:"))
                        rq = "select * from surendra2 where accountnumber = %d"
                        res=cur.execute(rq %(accountnumber))
                        for row in res:
                            print(row)
                        con.commit()
                        print("-" * 50)
                        ch = input("Do u want to see one more record(yes/no):")
                        if (ch.lower() == "no"):
                            break
                    except cx_Oracle.DatabaseError as db:
                        print("Prob in DB:", db)
                    except ValueError:
                        print("Don't enter alnums, strs and symbols for enos")
            # main program
            showcusrecord()
        case 5:
            def showallrecords():
                while (True):
                    try:
                        con = cx_Oracle.connect("system/tiger")
                        cur = con.cursor()
                        # accept Employee Values Dynamically from KBD
                        print("=" * 50)
                        rq = "select * from surendra3"
                        res = cur.execute(rq)
                        for rec in res:
                            print(rec)
                        con.commit()
                        print("-" * 50)
                        ch = input("Do u want to see all record again(yes/no):")
                        if (ch.lower() == "no"):
                            break
                    except cx_Oracle.DatabaseError as db:
                        print("Prob in DB:", db)
                    except ValueError:
                        print("Don't enter alnums, strs and symbols for enos")
            # main program
            showallrecords()
        case 6:
            print("Thanks for choosing KVR Bank")
            exit()
