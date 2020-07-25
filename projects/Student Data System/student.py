import os

from flask import Flask

from tkinter import *
from tkinter import ttk
import pymysql

app = Flask(__name__)



class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Data System")
        self.root.geometry("1300x750+0+0")

        # variables to store
        self.rollno_var = StringVar()
        self.name_var = StringVar()
        self.dob_var = StringVar()
        self.gender_var = StringVar()
        self.email_var = StringVar()
        self.contact_var = StringVar()
        self.optser_var= StringVar()
        self.txtser_var= StringVar()

        Title = Label(self.root, text="Student Data System", bd=10, relief=GROOVE, font=("times new roman", 40, "bold"),
                      bg="turquoise", fg="black")
        Title.pack(side=TOP, fill=X)

        Frame1 = Frame(self.root, bd=4, relief=RIDGE, bg="turquoise")
        Frame1.place(x=20, y=100, width=420, height=630)

        ftitle = Label(Frame1, text="Manage Student", bg="turquoise", fg="black", font=("times new roman", 20, "bold"))
        ftitle.grid(row=0, columnspan=2, pady=20)

        rollno = Label(Frame1, text="Roll No", bg="turquoise", fg="black", font=("times new roman", 20, "bold"))
        rollno.grid(row=1, column=0, pady=10, padx=10, sticky="w")

        txt_roll = Entry(Frame1, textvariable=self.rollno_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        name = Label(Frame1, text="Name", bg="turquoise", fg="black", font=("times new roman", 20, "bold"))
        name.grid(row=2, column=0, pady=10, padx=10, sticky="w")

        txt_name = Entry(Frame1, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        dob = Label(Frame1, text="D.O.B", bg="turquoise", fg="black", font=("times new roman", 20, "bold"))
        dob.grid(row=3, column=0, pady=10, padx=10, sticky="w")

        txt_dob = Entry(Frame1, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        gender = Label(Frame1, text="Gender", bg="turquoise", fg="black", font=("times new roman", 20, "bold"))
        gender.grid(row=4, column=0, pady=10, padx=10, sticky="w")

        optgen = ttk.Combobox(Frame1, textvariable=self.gender_var, width=21, height=20, font=("times new roman", 14),
                              state="readonly")
        optgen["values"] = ("Male", "Female", "Other")
        optgen.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        email = Label(Frame1, text="Email", bg="turquoise", fg="black", font=("times new roman", 20, "bold"))
        email.grid(row=5, column=0, pady=10, padx=10, sticky="w")

        txt_email = Entry(Frame1, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_email.grid(row=5, column=1, pady=10, padx=10, sticky="w")

        contact = Label(Frame1, text="Contact", bg="turquoise", fg="black", font=("times new roman", 20, "bold"))
        contact.grid(row=6, column=0, pady=10, padx=10, sticky="w")

        txt_con = Entry(Frame1, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_con.grid(row=6, column=1, pady=10, padx=10, sticky="w")

        add = Label(Frame1, text="Address", bg="turquoise", fg="black", font=("times new roman", 20, "bold"))
        add.grid(row=7, column=0, pady=10, padx=10, sticky="w")

        self.txt_add = Text(Frame1, width=26, height=4)
        self.txt_add.grid(row=7, column=1, pady=10, padx=10, sticky="w")

        btnfrm = Frame(Frame1, bg="turquoise")
        btnfrm.place(x=20, y=540, width=420, height=100)

        addbtn = Button(btnfrm, text="Add", fg="black", font=10, command=self.add_data).grid(row=0, column=0, pady=10,
                                                                                             padx=10, sticky="w")
        updatebtn = Button(btnfrm, text="Update", fg="black", font=10, command=self.update_data).grid(row=0, column=1,
                                                                                                      pady=10, padx=10,
                                                                                                      sticky="w")
        deletebtn = Button(btnfrm, text="Delete", fg="black", font=10,command=self.delete_data).grid(row=0, column=2, pady=10, padx=10,
                                                                            sticky="w")
        clearbtn = Button(btnfrm, text="Clear", fg="black", font=10, command=self.clear_data).grid(row=0, column=3,
                                                                                                   pady=10, padx=10,
                                                                                                   sticky="w")

        Frame2 = Frame(self.root, bd=4, relief=RIDGE, bg="turquoise")
        Frame2.place(x=480, y=100, width=1000, height=630)

        search = Label(Frame2, text="Search", bg="turquoise", fg="black", font=("times new roman", 20, "bold"))
        search.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        optser = ttk.Combobox(Frame2,textvariable=self.optser_var, width=15, height=20, font=("times new roman", 14), state="readonly")
        optser["values"] = ("name", "roll_no", "contact")
        optser.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        txt_ser = Entry(Frame2,textvariable=self.txtser_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_ser.grid(row=0, column=2, pady=10, padx=10, sticky="w")

        serabtn = Button(Frame2, text="Search", fg="black", font=10,command=self.search_data).grid(row=0, column=3, pady=10, padx=10, sticky="w")
        showallbtn = Button(Frame2, text="Show all", fg="black", font=10,command=self.fetch_data).grid(row=0, column=4, pady=10, padx=10,
                                                                               sticky="w")

        stdtable = Frame(Frame2, bd=4, relief=RIDGE, bg="turquoise")
        stdtable.place(x=20, y=70, width=780, height=550)
        scrollx = Scrollbar(stdtable, orient="horizontal")
        scrolly = Scrollbar(stdtable, orient="vertical")
        self.tableview = ttk.Treeview(stdtable,
                                      column=("roll no", "name", "dob", "gender", "email", "contact", "address"),
                                      xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(fill=X, side=BOTTOM)
        scrolly.pack(fill=Y, side=RIGHT)
        scrollx.configure(command=self.tableview.xview)
        scrolly.configure(command=self.tableview.yview)
        self.tableview.heading("roll no", text="Roll No")
        self.tableview.heading("name", text="Name")
        self.tableview.heading("dob", text="D.O.B")
        self.tableview.heading("gender", text="Gender")
        self.tableview.heading("email", text="Email")
        self.tableview.heading("contact", text="Contact")
        self.tableview.heading("address", text="Address")
        self.tableview.column("roll no", width=100)
        self.tableview.column("name", width=100)
        self.tableview.column("dob", width=100)
        self.tableview.column("gender", width=100)
        self.tableview.column("email", width=100)
        self.tableview.column("contact", width=100)
        self.tableview.column("address", width=100)
        self.tableview["show"] = "headings"
        self.tableview.pack(fill=BOTH, expand=1)
        self.tableview.bind("<ButtonRelease-1>", self.get_data)
        self.fetch_data()



    def add_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stddata")
        cur = con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (self.rollno_var.get(),
                                                                          self.name_var.get(),
                                                                          self.dob_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.email_var.get(),
                                                                          self.contact_var.get(),
                                                                          self.txt_add.get("1.0", END)))
        con.commit()
        self.fetch_data()
        self.clear_data()
        con.close()

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stddata")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.tableview.delete(*self.tableview.get_children())
            for row in rows:
                self.tableview.insert("", END, values=row)
            con.commit()
        con.close()

    def clear_data(self):
        self.rollno_var.set("")
        self.name_var.set("")
        self.dob_var.set("")
        self.gender_var.set("")
        self.email_var.set("")
        self.contact_var.set("")
        self.txt_add.delete("1.0", END)

    def get_data(self, ab):
        cursor = self.tableview.focus()
        content = self.tableview.item(cursor)
        row = content["values"]
        self.rollno_var.set(row[0])
        self.name_var.set(row[1])
        self.dob_var.set(row[2])
        self.gender_var.set(row[3])
        self.email_var.set(row[4])
        self.contact_var.set(row[5])
        self.txt_add.delete("1.0", END)
        self.txt_add.insert(END, row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stddata")
        cur = con.cursor()
        cur.execute("update students set  name=%s,dob=%s,gender=%s,email=%s,contact=%s,address=%s where roll_no= %s ", (
                                                                          self.name_var.get(),
                                                                          self.dob_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.email_var.get(),
                                                                          self.contact_var.get(),
                                                                          self.txt_add.get("1.0", END),
                                                                          self.rollno_var.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear_data()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stddata")
        cur = con.cursor()
        cur.execute("delete  from students where roll_no=%s",self.rollno_var.get())

        con.commit()
        con.close()
        self.fetch_data()
        self.clear_data()
        

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stddata")
        cur = con.cursor()
        cur.execute("select * from students where %s = %s" %(self.optser_var.get(),self.txtser_var.get()))
        rows = cur.fetchall()
        if len(rows) != 0:
            self.tableview.delete(*self.tableview.get_children())
            for row in rows:
                self.tableview.insert("", END, values=row)
            con.commit()
        con.close()




root = Tk()
obj = Student(root)
root.mainloop()

port = int(os.getenv("PORT",8080))
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=port)
    # app.run(host='127.0.0.1', port=8001, debug=True)
