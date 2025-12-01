from tkinter import *
import mysql.connector
import random
import tkinter.messagebox as msg
class BankDetails:
    def __init__(self,root):
        self.root=root
        self.root.title("page")
        self.root.geometry("600x600")
        self.root.config(bg="red")
        n = Label(text="Welcome to Our Bank", fg="blue", font=("Bold", 30))
        n.place(x=97, y=200)
        b = Button(text="Click Here", bg="white", fg="black", font=("Bold", 20), command=self.mainmenu)
        b.place(x=200, y=370)
    def mainmenu(self):
        self.mainmenu =Tk()
        self.mainmenu.title("welcome")
        self.mainmenu.geometry("600x600")
        self.mainmenu.config(bg="red")
        title1= Label(self.mainmenu, text="Mainmenu", bg="red", fg="black", font=("Bold", 20))
        title1.pack()
        b1=Button(self.mainmenu,text="Register",bg="white",fg="black",font=("Bold",20),command=self.registration)
        b1.place(x=230,y=200)
        b2 = Button(self.mainmenu,text="Deposit", bg="white", fg="black", font=("Bold", 20), command=self.deposit)
        b2.place(x=230, y=300)
        b3 = Button(self.mainmenu,text="withdraw", bg="white", fg="black", font=("Bold", 20), command=self.withdraw)
        b3.place(x=230, y=400)
        self.mainmenu.mainloop()
    def registration(self):
        self.registration=Tk()
        self.registration.title("Registration")
        self.registration.geometry("600x600")
        self.registration.config(bg="red")
        title=Label(self.registration,text="Register",bg="red",fg="black",font=("Bold",20))
        title.pack()
        fullname=Label(self.registration,text="Full Name",bg="white",fg="black",font=("Bold",15))
        fullname.place(x=20,y=90)
        self.fullname_entry=Entry(self.registration,font=("Bold",15))
        self.fullname_entry.place(x=150,y=90)
        mobile=Label(self.registration, text="Mobile", bg="white", fg="black", font=("Bold", 15))
        mobile.place(x=20,y=150)
        self.mobile_entry = Entry(self.registration, font=("Bold", 15))
        self.mobile_entry.place(x=150, y=150)
        addrs = Label(self.registration, text="Address", bg="white", fg="black", font=("Bold", 15))
        addrs.place(x=20, y=210)
        self.addrs_entry = Entry(self.registration, font=("Bold", 15))
        self.addrs_entry.place(x=150, y=210)
        aadhar = Label(self.registration, text="Aadhar", bg="white", fg="black", font=("Bold", 15))
        aadhar.place(x=20, y=270)
        self.aadhar_entry = Entry(self.registration, font=("Bold", 15))
        self.aadhar_entry.place(x=150, y=270)
        bal = Label(self.registration, text="min bal", bg="white", fg="black", font=("Bold", 15))
        bal.place(x=20, y=330)
        self.bal_entry = Entry(self.registration, font=("Bold", 15))
        self.bal_entry.place(x=150, y=330)
        self.bal_entry.insert(0,500)
        submit=Button(self.registration,text="Register",bg="white",fg="black",font=("Bold",15),command=self.regis)
        submit.place(x=160,y=380)
        self.registration.mainloop()
    def regis(self):
        mydb=mysql.connector.connect(host="localhost",user="root",password="123456",database="bdt")
        mycur=mydb.cursor()
        fullname=self.fullname_entry.get()
        mobile=self.mobile_entry.get()
        addrs=self.addrs_entry.get()
        aadhar=self.aadhar_entry.get()
        bal=500
        if not fullname:
            msg.showinfo("Error", "enter full name")
        if not mobile:
            msg.showinfo("Error", "enter mobile number")
        if not addrs:
            msg.showinfo("Error", "enter full name")
        if not aadhar:
            msg.showinfo("Error", "enter mobile number")
        account_number = self.generate_account_number()
        msg.showinfo("Success", f"Account created for {fullname} with balance Rs.{bal}\nAccount Number: {account_number}")
        mycur.execute("insert into dtls1 values(%s,%s,%s,%s,%s,%s)",(fullname, mobile, addrs, aadhar, bal, account_number))
        mydb.commit()
    def generate_account_number(self):
        return str(random.randint(1000000000,9999999999))
        self.generate_account_number.mainloop()
        c = 0
        for i in mycur:
            c = c + 1
        if c >= 1:
            msg.showinfo("valid", "Registration sucessfull")
        mydb.commit()
    def deposit(self):
        self.deposit = Tk()
        self.deposit.title("Deposit")
        self.deposit.geometry("600x600")
        self.deposit.config(bg="red")
        title = Label(self.deposit, text="Deposit", bg="red", fg="black", font=("Bold", 20))
        title.pack()
        account_number = Label(self.deposit, text="Enter Account No:", bg="white", fg="black", font=("Bold", 15))
        account_number.place(x=20, y=90)
        self.account_number_entry1 = Entry(self.deposit, font=("Bold", 15))
        self.account_number_entry1.place(x=200, y=90)
        bal = Label(self.deposit, text="Current Balance", bg="white", fg="black", font=("Bold", 15))
        bal.place(x=20, y=150)
        self.bal_entry1 = Entry(self.deposit, font=("Bold", 15))
        self.bal_entry1.place(x=200, y=150)
        self.bal_entry1.insert(0, 500)
        amount = Label(self.deposit, text="Amount Depositing", bg="white", fg="black", font=("Bold", 15))
        amount.place(x=20, y=210)
        self.amount_entry1 = Entry(self.deposit, font=("Bold", 15))
        self.amount_entry1.place(x=200, y=210)
        submit = Button(self.deposit, text="Deposit", bg="white", fg="black", font=("Bold", 15),command=self.dep)
        submit.place(x=160, y=270)
        self.deposit.mainloop()
    def dep(self):
        mydb=mysql.connector.connect(host="localhost",user="root",password="123456",database="bdt")
        mycur=mydb.cursor()
        account_number=self.account_number_entry1.get()
        bal=self.bal_entry1.get()
        amount=self.amount_entry1.get()
        deposit_amount=int(amount)
        mycur.execute("select bal from dtls1 where account_number=%s", (account_number,))
        c=0
        for bal in mycur:
            c=bal[0]
            if c>=1:
                cb=c+deposit_amount
                mycur.execute("update dtls1 set bal=%s where account_number= %s",(cb,account_number))
                msg.showinfo("Success",f"Rs. {amount} deposited successfully. New balance: Rs. {cb}")
            else:
                msg.showinfo("Failed", "Wrong Account number")
        mydb.commit()
    def withdraw(self):
        self.withdraw = Tk()
        self.withdraw.title("Withdraw")
        self.withdraw.geometry("600x600")
        self.withdraw.config(bg="red")
        title = Label(self.withdraw, text="Withdraw", bg="red", fg="black", font=("Bold", 20))
        title.pack()
        account_number = Label(self.withdraw, text="Enter Account Number", bg="white", fg="black", font=("Bold", 15))
        account_number.place(x=20, y=150)
        self.account_number_entry2 = Entry(self.withdraw, font=("Bold", 15))
        self.account_number_entry2.place(x=250, y=150)
        bal = Label(self.withdraw, text="Current Balance", bg="white", fg="black", font=("Bold", 15))
        bal.place(x=20, y=210)
        self.bal_entry2 = Entry(self.withdraw, font=("Bold", 15))
        self.bal_entry2.place(x=250, y=210)
        withdraw=Label(self.withdraw, text="Amount Withdrawing", bg="white", fg="black", font=("Bold", 15))
        withdraw.place(x=20, y=270)
        self.withdraw_entry2 = Entry(self.withdraw, font=("Bold", 15))
        self.withdraw_entry2.place(x=250, y=270)
        submit = Button(self.withdraw, text="Withdraw", bg="white", fg="black", font=("Bold", 15),command=self.wtdw)
        submit.place(x=160, y=330)
        self.withdraw.mainloop()
    def wtdw(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="123456", database="bdt")
        mycur = mydb.cursor()
        account_number = self.account_number_entry2.get()
        bal = self.bal_entry2.get()
        withdraw = self.withdraw_entry2.get()
        withdraw_amount = int(withdraw)
        mycur.execute("select bal from dtls1 where account_number=%s", (account_number,))
        c = 0
        for bal in mycur:
            c = bal[0]
            if c >= 1:
                cb = c - withdraw_amount
                mycur.execute("update dtls1 set bal=%s where account_number= %s", (cb, account_number))
                msg.showinfo("Success", f"Rs. {withdraw} withdrawed successfully. New balance: Rs. {cb}")
            else:
                msg.showinfo("Failed", "Wrong Account number")
        mydb.commit()
root=Tk()
l=BankDetails(root)
root.mainloop()