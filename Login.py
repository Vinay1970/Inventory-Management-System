from functions import size_changer,connect_database
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


def login_page(window):

    window.title('Dashboard')
    window.geometry('1270x668+0+0')
    window.resizable(0,0)
    window.config(bg = 'white')
    tk_img = size_changer('image/budget.png', 0.07)
    titlelabel = Label(window,
                    compound='left',
                    image= tk_img,
                    text="  Inventory Management System",
                    font=('Times New Roman', 40, 'bold'),
                    bg='#010c48',
                    fg='white',
                    anchor='w',
                    padx=20
                    )
    titlelabel.place(x=0,y=0,relwidth=1)
    leftFrame = Frame(window, bg='white')
    leftFrame.place(x=0,y=80,
                    width=630, 
                height=570)
    
    rightFrame =  Frame(window, bg= 'white')
    rightFrame.place(x=500,y=80, 
                width=630, 
                height=570)

    left_img =size_changer('image/coordinator.png',1)
    leftlabel = Label(leftFrame,
                    image=left_img,
                    bg='white',
                    padx=20
    )
    leftlabel.image = left_img
    leftlabel.place(x=0,y=0)

    right_img = size_changer('image/model.png', .7)
    rightlabel = Label(rightFrame,
                    image=right_img,
                    bg='white'
    )

    rightlabel.place(x=140,y=0)
    bottomlabel = Label(rightFrame,bg='white')
    bottomlabel.place(x=0, y=400, width=630, height=200)

    Label(bottomlabel, text="Username",font=('Arial',16, 'bold'), bg='white').grid(row=0,column=1,padx=(40,0))
    entry_username = Entry(bottomlabel,font=('Arial',16, 'bold'), bg='lightyellow')
    entry_username.grid(row=0, column=3, padx=20)

    Label(bottomlabel, text="Password",font=('Arial',16, 'bold'), bg ='white').grid(row=1, column=1, padx=(40,0))
    entry_password = Entry(bottomlabel,font=('Arial',16, 'bold'), show="*", bg='lightyellow')
    entry_password.grid(row=1, column=3,padx=20)

    def attempt_login():

        username = entry_username.get()
        password = entry_password.get()

        cursor, connection = connect_database()
        if not cursor:
            return

        cursor.execute("SELECT * FROM employee_data WHERE username=%s AND password=%s",
                       (username, password))
        record = cursor.fetchone()

        if record:
            window.destroy()   # close login 
            trfl = True
            return             # call dashboard
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    Button(bottomlabel, text="Login",font=('Arial',16, 'bold'),fg='white',
                           bg = '#010c48', command=attempt_login).grid(row=2, columnspan=5, pady=10)
    Button(bottomlabel, text="Forgot Password",font=('Arial',16, 'bold'),fg='white',
                           bg = '#010c48', command=lambda: forgot_password(entry_username.get())).grid(row=3, columnspan=5)

    window.mainloop()

def forgot_password(username):
    cursor, connection = connect_database()
    if not cursor:
        return

    cursor.execute("SELECT email, password FROM employee_data WHERE username=%s", (username,))
    record = cursor.fetchone()

    if record:
        email, password = record
        messagebox.showinfo("Password Recovery", f"Password: {password}\nEmail: {email}")
    else:
        messagebox.showerror("Error", "Username not found")

def logout(window):
    # Close the current dashboard window
    window.destroy()
    # Reopen the login page
    login_page(window)

def exit_app(window):
    # Close everything and terminate the program
    window.destroy()

