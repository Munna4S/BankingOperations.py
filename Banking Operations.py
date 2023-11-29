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
ch=int(input("Enter ur Choice:"))
if ch == 0:
  ro="create table surendra6(accountnumber int unique,cname varchar(30),bal float(20),address varchar(50))"
  cur.execute(ro)
  con.commit()
else: