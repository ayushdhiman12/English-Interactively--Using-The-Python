from tkinter import *
import sqlite3
import webbrowser
import importlib
import sys

with open('dir', 'r') as file:
    dir = file.readline()

database = ''
with open('db', 'r') as file:
    database = file.readline()
db = sqlite3.connect(database)

root = Tk()
root.configure(bg='bisque2')
yt = PhotoImage(file='yt.png')
qs = PhotoImage(file='qs.png')
def open_link():
    webbrowser.open_new(url='https://www.youtube.com/channel/UCxepMapUxIGMTN9f9KYSP3A')


def ask():
    root.destroy()
    try:
        importlib.reload(sys.modules['Trial'])
    except KeyError:
        pass
    import Trial
    if database == 'idioms':
        Trial.alast()
    else:
        Trial.last()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.title('GDV Project')
root.geometry("{}x{}".format(width, height))

# mainLabel = Label(root, bg='bisque2')
# mainLabel.grid(row=0, column=0, sticky='nsew')

gdv = Label(root, text=' GDV Project \nLearn English', anchor=CENTER, font=('Times', 66), fg='red3', bg='bisque2')
gdv.grid(row=0, column=0, sticky='nsew', padx=(int(width//4) + 40), pady=int(height//32))

intro = Frame(root, width=300, height=150, bg='bisque2')
intro.grid(row=2, column=0)

link = Button(intro, image=yt, width=100, height=100)
link.grid(row=0, column=0, pady=18, padx=10)
link.config(command=open_link)

qst = Button(intro, image=qs, width=100, height=100, command=ask)
qst.grid(row=0, column=1, pady=18, padx=10)

mainFrame = Frame(root, width=400, height=300, bg="orange2")
mainFrame.grid(row=1, sticky='nsew', padx=int(width//8.5))

word = Label(mainFrame, text='Word:', fg='steelblue', font=('Times', 33))
word.grid(row=0, column=0, padx=20, pady=30, sticky='nsew')

word_var = StringVar()
word_entry = Entry(mainFrame, borderwidth=3, font=("Times", 33), width=int(width//40), textvariable=word_var, fg='steelblue')
word_entry.grid(row=0, column=1, sticky='nsew', pady=30)

exp = Label(mainFrame, text='Explain:', fg='steelblue', font=('Times', 33))
exp.grid(row=1, column=0, padx=20, sticky='nsew')

exp_var = StringVar()
exp_entry = Entry(mainFrame, borderwidth=3, font=("Times Azeri", 33), width=int(width//40), textvariable=exp_var, fg='steelblue')
exp_entry.grid(row=1, column=1, sticky='nsew')

def change(var):
    var = list(str(var))
    wr2 = ''
    for i in var:
        if i == '?':
            var[var.index(i)] = '%'
        if i == "ö":
            var[var.index(i)] = '>'
        if i == "ü":
            var[var.index(i)] = '^'
        if i == "ı":
            var[var.index(i)] = '@'
        if i == 'ş':
            var[var.index(i)] = '$'
        if i == "ğ":
            var[var.index(i)] = '&'
        if i == "ç":
            var[var.index(i)] = "#"
    for i in var:
        wr2 += i
    return wr2

change(exp_var.get())
def adD():
    global exp_var
    global word_var
    global db
    db.execute('INSERT INTO easy VALUES ("{}", "{}");'.format(str(word_var.get()), change(exp_var.get())))
    db.commit()
    word_var.set('')
    exp_var.set('')

buttonframe = Frame(mainFrame, bg="orange2")
buttonframe.grid(row=2, column=1, sticky='w', padx=int(width//8), pady=15)

add = Button(buttonframe, text='Add', fg='red2', font=("Times", 33), command=adD)
add.grid(row=0, column=0, padx=10)

def back():
    root.destroy()
    global dir
    try:
        importlib.reload(sys.modules[dir])
    except KeyError:
        pass
    if dir == 'sizes':
        import sizes
        sizes.start()
    elif dir == 'Idioms':
        import Idioms
        Idioms.start()



back = Button(buttonframe, text='Back', fg='red2', font=("Times", 33), command=back)
back.grid(row=0, column=1)

if __name__ == "__main__":
    root.mainloop()

def start():
    root.mainloop()
