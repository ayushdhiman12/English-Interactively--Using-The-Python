import sqlite3
from tkinter import *
import random
import webbrowser
import sys
import importlib

con = ''
with open('db', 'r') as file:
    con = file.readline()

db = sqlite3.connect(con)
with open('score.txt', 'r') as file:
    score = str(file.readline())

wr = ''
wr2 = ''

a = db.execute("SELECT * FROM easy").fetchall()

dictionary = {}

for i in a:
    word, definiton = i
    dictionary[definiton] = word

def change(var):
    global wr2
    var = list(str(var).lower())
    for i in var:
        if i == '%':
            var[var.index(i)] = 'ə'
        if i == ">":
            var[var.index(i)] = 'ö'
        if i == "^":
            var[var.index(i)] = 'ü'
        if i == "@":
            var[var.index(i)] = 'ı'
        if i == '$':
            var[var.index(i)] = 'ş'
        if i == "&":
            var[var.index(i)] = 'ğ'
        if i == "#":
            var[var.index(i)] = "ç"
    wr2 = ''
    for i in  var:
        wr2 += i
    wr2 = wr2.capitalize()

def  cwr():
    global wr
    wr = random.choice(list(dictionary.keys()))
    change(wr)

def slb2():
    global lb2
    global lb
    global wr
    global lb3
    global var
    global score
    global scorel
    cwr()
    lb['bg'] = 'bisque2'
    lb3.destroy()
    lb2['text'] = wr2
    lb.config(text='Learning English', fg='steelblue')
    lb3 = Entry(root, textvariable=var, borderwidth=5, bg='green')
    lb3.grid(row=2, column=0, columnspan=2, padx=50, sticky='nsew', pady=16)
    lb3.config(font=("Times", 44))
    var.set('')
    scorel.destroy()
    scorel = Label(Frame, text='Score: {}'.format(score), font=("Times", 33), height=1, fg='red', bg='bisque2')
    scorel.grid(row=0, column=3, sticky='nsew', padx=39)

def help():
    global dictionary
    global lb
    global scorel
    global wr
    global score
    lb3.destroy()
    lb.config(text='The word is: {}'.format(dictionary[wr]), fg='steelblue', wraplength=1500)
    score = int(score) - 3
    with open('score.txt', 'w') as file:
        print(score, file=file, end='')
    scorel.destroy()
    scorel = Label(Frame, text='Score: {}'.format(score), font=("Times", 33), height=1, fg='red', bg='bisque2')
    scorel.grid(row=0, column=3, sticky='nsew', padx=39)

root = Tk()
root.configure(bg='bisque2')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("{}x{}".format(width, height))
root.title('GDV Project')

r = PhotoImage(file='r.png')
qs = PhotoImage(file='qs.png')
pl = PhotoImage(file='plus.png')

lb = Label(root, text='Learning English', borderwidth=5, bg='bisque2', fg='steelblue', anchor=CENTER)
lb.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=50, pady=16)
lb.config(font=("Times", 66))

lb2 = Label(root, borderwidth=5, bg='green', wraplength=1200)
lb2.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=50)
lb2.config(font=("Times", 29))
cwr()
lb2['text'] = wr2

curs = db.cursor()
string = list(curs.execute("SELECT translate FROM easy"))
cwr()

var = StringVar()
def do():
    global var
    global scorel
    global wr
    global dictionary
    global lb
    global lb2
    global score
    s = var.get()
    if s.lower() == dictionary[wr].lower():
        lb['text'] = "Great!"
        lb['fg'] = "spring green"
        lb['bg'] = 'coral1'
        score = int(score) + 1
        lb3.destroy()
        with open('score.txt', 'w') as file:
            print(score, file=file, end='')
        var.set('')
        scorel.destroy()
        scorel = Label(Frame, text='Score: {}'.format(score), font=("Times", 33), height=1, fg='red', bg='bisque2')
        scorel.grid(row=0, column=3, sticky='nsew', padx=39)

    else:
        lb['text'] = 'Wrong!'
        lb['bg'] = 'Red'
        lb['fg'] = 'yellow'

lb3 = Entry(root, textvariable=var, borderwidth=5, bg='green')
lb3.grid(row=2, column=0, columnspan=2, padx=50, sticky='nsew', pady=16)
lb3.config(font=("Times", 44))

Frame = Frame(root, borderwidth=10, bg='bisque2')
Frame.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=30)

b1 = Button(Frame, text='Try', font=("Times", 35), width=5, height=2, command=do, bg='white')
b1.grid(row=0, column=0, sticky='nsew', padx=15)

b2 = Button(Frame, image=r, width=130, height=2, command=slb2, bg='white')
b2.grid(row=0, column=1, sticky='nsew', padx=15)

b3 = Button(Frame, text='Hint', font=("Times", 35), width=5, height=2, command=help, bg='white')
b3.grid(row=0, column=2, sticky='nsew', padx=15)

def ask():
    root.destroy()
    try:
        importlib.reload(sys.modules['Trial'])
    except KeyError:
        pass
    import Trial
    Trial.ft()


b4 = Button(Frame, image=qs, height=2, width=130, bg='white', command=ask)
b4.grid(row=0, column=4, sticky='nsew', padx=15)

def back():
    root.destroy()
    try:
        importlib.reload(sys.modules['MainWindow'])
    except KeyError:
        pass
    import MainWindow
    MainWindow.start()


b5 = Button(Frame,  text='Back', font=("Times", 35), height=2, width=5, command=back, bg='white')
b5.grid(row=0, column=5, sticky='nsew', padx=15)

def open_link():
    webbrowser.open_new(url='https://www.youtube.com/channel/UCxepMapUxIGMTN9f9KYSP3A')

def add():
    root.destroy()
    with open('dir', 'w') as file:
        print('sizes', file=file, end='')
    try:
        importlib.reload(sys.modules['Add'])
    except KeyError:
        pass
    import Add
    Add.start()

b6 = Button(Frame, image=pl, width=130, height=2, bg='white', command=add)
b6.grid(row=0, column=6, sticky='nsew', padx=15)

scorel = Label(Frame, text='Score: {}'.format(score), font=("Times", 33), fg='red2', bg='white')
scorel.grid(row=0, column=3, sticky='nsew', padx=36)

root.rowconfigure(0,  weight=0)
root.rowconfigure(1, weight=0)
root.rowconfigure(2, weight=0)
root.rowconfigure(3, weight=0)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

scorel.destroy()
slb2()
db.close()
if __name__ == '__main__':
    root.mainloop()

# def start():
#     global root
#     slb2()
#     root.mainloop()
def start():
    global root
    root.destroy
    slb2()
    root.mainloop
