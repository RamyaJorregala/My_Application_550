import tkinter as tk
from tkinter import *
import mysql.connector

root = tk.Tk()
root.title("Student Management System")
root.geometry("800x400")
root.config(bg="purple")

conn=mysql.connector.connect(host="localhost",port="3307",user="root",password="root",database="student_db")
cursr=conn.cursor()


myFont = ('times', 14, 'bold')
def clearFields():
    tf1.delete(0, END)
    tf2.delete(0, END)
    tf3.delete(0, END)
    tf4.delete(0, END)

def addOperation():
    try:
        username = tf1.get()
        password = tf2.get()
        email = tf3.get()
        mobile = tf4.get()

        sqlQuery = "INSERT INTO student VALUES (%s,%s,%s,%s)"
        values = (username, password, email, mobile)

        cursr.execute(sqlQuery, values)
        conn.commit()

        text.insert(END, "Record Added Successfully\n")
        clearFields()


    except Exception as ex:
        text.insert(END, str(ex) + "\n")
        conn.rollback()
      
def updateOperation():
    try:
        username = tf1.get()
        password = tf2.get()
        email = tf3.get()
        mobile = tf4.get()

        sqlQuery = "UPDATE student SET password=%s, email=%s, mobile=%s WHERE uname=%s"
        values = (password, email, mobile, username)

        cursr.execute(sqlQuery, values)
        conn.commit()

        text.insert(END, "Record Updated Successfully\n")
        clearFields()

    except Exception as ex:
        text.insert(END, str(ex) + "\n")
        conn.rollback()


    
def deleteOperation():
    try:
        username = tf1.get()

        sqlQuery = "DELETE FROM student WHERE uname=%s"
        values = (username,)

        cursr.execute(sqlQuery, values)
        conn.commit()

        text.insert(END, "Record Deleted Successfully\n")
        clearFields()

    except Exception as ex:
        text.insert(END, str(ex) + "\n")
        conn.rollback()
 
userLabel = tk.Label(root, text="USERNAME:")
userLabel.config(bg="white", font=myFont)
userLabel.place(x=150, y=80)

tf1 = tk.Entry(root)
tf1.place(x=350, y=85)

pwdLabel = tk.Label(root, text="PASSWORD:")
pwdLabel.config(bg="white", font=myFont)
pwdLabel.place(x=150, y=130)

tf2 = tk.Entry(root, show="*")
tf2.place(x=350, y=135)

emailLabel = tk.Label(root, text="EMAIL:")
emailLabel.config(bg="white", font=myFont)
emailLabel.place(x=150, y=180)

tf3 = tk.Entry(root)
tf3.place(x=350, y=185)

mobLabel = tk.Label(root, text="MOBILE:")
mobLabel.config(bg="white", font=myFont)
mobLabel.place(x=150, y=230)

tf4 = tk.Entry(root)
tf4.place(x=350, y=235)

btn = tk.Button(root, text="ADD", command=addOperation)
btn.config(bg="white", fg="black", font=myFont)
btn.place(x=150, y=290)

btn = tk.Button(root, text="UPDATE", command=updateOperation)
btn.config(bg="white", fg="black", font=myFont)
btn.place(x=250, y=290)

btn = tk.Button(root, text="DELETE", command=deleteOperation)
btn.config(bg="white", fg="black", font=myFont)
btn.place(x=390, y=290)

text=tk.Text(root,height=10,width=50)
text.config(bg="white",fg="black",font=myFont)
text.place(x=100,y=350)

root.mainloop()

conn.close()