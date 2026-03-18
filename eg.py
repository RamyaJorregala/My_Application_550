import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Student Management System")
root.geometry("800x400")
root.config(bg="purple")

myFont = ('times', 14, 'bold')



def loginOperation():
    username=tf1.get()
    password=tf2.get()
    if username=="admin" and password=="admin":
        text.insert(END,'Login Success')
    else:
        text.insert(END,'Login Failure')
 
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

btn = tk.Button(root, text="Click Me", command=loginOperation)
btn.config(bg="white", fg="black", font=myFont)
btn.place(x=250, y=290)

text=tk.Text(root,height=10,width=50)
text.config(bg="white",fg="black",font=myFont)
text.place(x=100,y=350)

root.mainloop()



