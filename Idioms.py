from tkinter import *
import random
import sys
import importlib
import sqlite3

database = ''
with open('db', 'r') as file:
    database = file.readline()

db = sqlite3.connect(database)
curs = db.cursor()

dictionary = {}
for i in curs.execute('SELECT * FROM easy'):
    idiom, definiton = i
    dictionary[idiom] = definiton

wr = ''
ans = ''
l = [1, 2, 3]

def choose():
    global wr
    global ans
    global l
    global lb2
    wr = random.choice(list(dictionary))
    ans = dictionary[wr]
    r = random.choice(l)
    l.remove(r)
    lb2['text'] = wr
    if r == 1:
        global bt1
        bt1['text'] = ans
    if r == 2:
        global bt2
        bt2['text'] = ans
    if r == 3:
        global bt3
        bt3['text'] = ans #new with answer

val = list(dictionary.values())

def othetrs(): #chooses others
    global ans
    global val
    try:
        val.remove(ans)
    except ValueError:
        pass
    try:
        b = random.choice(val)
        val.remove(b)
    except ValueError:
        b = random.choice(val)
        val.remove(b)
    return b

def setothers():
    global l
    global othetrs
    global ans
    for ro in l:
        if ro == 1:
            global bt1
            bt1['text'] = othetrs()
        if ro == 2:
            global bt2
            bt2['text'] = othetrs()
        if ro == 3:
            global bt3
            bt3['text'] = othetrs() # sets the others

def next():
    global val
    global dictionary
    global choose
    global setothers
    global lb
    global l
    l = [1,2,3]
    val = list(dictionary.values())
    choose()
    setothers()
    lb.config(fg='steelblue', text='Learning English', bg='bisque2')

def do():
    global bt1
    global ans
    global lb
    if bt1['text'] == ans:
        lb['text'] = "Great!"
        lb['fg'] = "spring green"
        lb['bg'] = 'coral1'
    else:
        lb['text'] = 'Wrong!'
        lb['bg'] = 'Red'
        lb['fg'] = 'yellow'
def do1():
    global bt2
    global ans
    global lb
    if bt2['text'] == ans:
        lb['text'] = "Great!"
        lb['fg'] = "spring green"
        lb['bg'] = 'coral1'
    else:
        lb['text'] = 'Wrong!'
        lb['bg'] = 'Red'
        lb['fg'] = 'yellow'
def do2():
    global bt2
    global ans
    global lb
    if bt3['text'] == ans:
        lb['text'] = "Great!"
        lb['fg'] = "spring green"
        lb['bg'] = 'coral1'
    else:
        lb['text'] = 'Wrong!'
        lb['bg'] = 'Red'
        lb['fg'] = 'yellow'


root = Tk()
root.configure(bg='bisque2')
root.title("GDV Project")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("{}x{}".format(width, height))

lb = Label(root, text='Learning English', borderwidth=5, fg='steelblue', width=12, bg='bisque2')
lb.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=int(width//3.5), pady=16)
lb.config(font=("Times", 66))

lb2 = Label(root, borderwidth=5, bg='lawngreen', wraplength=1200)
lb2.grid(row=1, column=0, columnspan=2, sticky='nsew', padx=int(width//10), pady=16)
lb2.config(font=("Times", 33))

bt1 = Button(root, text='', font=("Times", 28), borderwidth=2, command=do)
bt1.grid(row=2, column=0, columnspan=2, sticky='nsew', padx=int(width//10))

bt2 = Button(root, text='', font=("Times", 28), borderwidth=2, command=do1)
bt2.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=int(width//10), pady=25)

bt3 = Button(root, text='', font=("Times", 28), borderwidth=2, command=do2)
bt3.grid(row=4, column=0, columnspan=2, sticky='nsew', padx=int(width//10))

buttonFrame = Frame(root, bg='bisque2', height=250)
buttonFrame.grid(row=5, column=1, sticky='nsew', pady=30)

qs = PhotoImage(file='qs.png')
pl = PhotoImage(file='plus.png')

def add():
    global root
    root.destroy()
    with open('dir', 'w') as file:
        print('Idioms', file=file, end='')
    try:
        importlib.reload(sys.modules['Add'])
    except KeyError:
        pass
    import Add
    Add.start()

def back():
    root.destroy()
    try:
        importlib.reload(sys.modules['MainWindow'])
    except KeyError:
        pass
    import MainWindow
    MainWindow.start()

def ask1():
    root.destroy()
    try:
        importlib.reload(sys.modules['Trial'])
    except KeyError:
        pass
    import Trial
    Trial.id()

qsb = Button(buttonFrame, image=qs, height=130, width=130, bg='white', command=ask1)
qsb.grid(row=0, column=0, sticky='nsew', padx=15)

plb = Button(buttonFrame, image=pl, width=130, height=130, bg='white', command=add)
plb.grid(row=0, column=3, sticky='nsew', padx=15)

next = Button(buttonFrame, text='NEXT', bg='white', font=("Times", 27), fg='green', command=next)
next.grid(row=0, column=1, sticky='nsew', padx=15)

next = Button(buttonFrame, text='BACK', bg='white', font=("Times", 27), fg='green', command=back)
next.grid(row=0, column=2, sticky='nsew', padx=15)


choose()
setothers()


if __name__ == '__main__':
    root.mainloop()

def start():
    root.mainloop()

#new val
#but
#next