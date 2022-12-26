from http.client import FOUND
from tkinter import*
from tkinter import messagebox
from turtle import bgcolor
from tkinter import font
from tkinter import ttk
import sqlite3 as sq
import ast
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



   
root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)




    
    


def signin():

    
    username=user.get()
    password=code.get()
    login = (username, password)
    client.sendto(b'Login:', ('192.168.0.173', 9090))
    client.sendto(username.encode('utf-8'), ('192.168.0.173', 9090))
    client.sendto(b'Password:', ('192.168.0.173', 9090))
    client.sendto(password.encode('utf-8'), ('192.168.0.173', 9090))
    client.sendto(b'\n', ('192.168.0.173', 9090))
    try:
        file=open('Login.txt','r+')
        d=file.read()
        r=ast.literal_eval(d)

        dict2={username:password}
        r.update(dict2)
        file.truncate(0)
        file.close()

        file=open('Login.txt','w')
        w=file.write(str(r))
    except:
        file=open('Login.txt','w')
        pp=str({'Username':'password'})
        file.write(pp)
        file.close()

        
def signup():
    def readAva(n):
       try:
          with open(f"Login.txt", "rb") as f:
            return f.read()
       except IOError as e:
          print(e)
          return False

    with sq.connect("log.db") as con:
       con.row_factory = sq.Row
       cur = con.cursor()


       cur.executescript("""CREATE TABLE IF NOT EXISTS users(
       user TEXT,
       pass BLOB,
       score INTEGER
       )""")
       img = readAva(1)
       if img:
          binary = sq.Binary(img)
          cur.execute("INSERT INTO users VALUES('Пользователь',?,1000)", (binary,))
    new_window_1 = Toplevel()      
    new_window_1.title('Error')
    new_window_1.geometry('400x200+920+520')
    new_window_1.resizable(width=False, height=False)
    frame1 = Frame(new_window_1,height=200, width=400, bg='white')
    frame1.pack(anchor = 'center')
    font6 = font.Font(family='Verdana', size=13, weight='bold')
    error = Label(frame1, text='Ошибка', fg='black', bg='white', font=font6)
    error.place(relx = 0.38, rely= 0.2)
    font7 = font.Font(family='Verdana', size=11)
    error2 = Label(frame1, text='Извините, произошла ошибка.', fg='grey',bg='white', font=font7)
    error2.place(relx = 0.1, rely = 0.4, relwidth=0.8)
    font8 = font.Font(family='Verdana', size=13, weight='bold')
    btn = Button(frame1, text='OK', fg='light slate blue',bg='white', font=font8,command=new_window_1.destroy)
    btn.place(relx=0.45, rely=0.75)
    btn['border']= '0'
    new_window_1.mainloop()     






    

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)


heading=Label(frame,text='Sing in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)
####---------------------------------------------------------
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

####----------------------------------------------------------
def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    if code.get()=='':
        code.insert(0,'Password')

code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
####--------------------------------------------------------
Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don`t have an account?" , fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)
sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup)
sign_up.place(x=200,y=270)


root.mainloop()



