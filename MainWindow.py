from tkinter import *
import webbrowser
import sys
import importlib

def open_link():
    webbrowser.open_new(url='https://www.youtube.com/channel/UCxepMapUxIGMTN9f9KYSP3A')
def set(lev):
    with open('lan', 'r') as file:
        lan = file.readline()
    with open('db', 'w') as file2:
        print('{}{}'.format(lev, lan), end='', file=file2)


root = Tk()

# root.attributes('-fullscreen',True)

img1 = PhotoImage(file='azeri.png')
img2 = PhotoImage(file='russian.png')
image1 = PhotoImage(file='vocabulary.png')
image2 = PhotoImage(file="game .png")
image3 = PhotoImage(file='idioms.png')
easy = PhotoImage(file='easy.png')
medium = PhotoImage(file='medium.png')
hard = PhotoImage(file='hard.png')
yt = PhotoImage(file='yt.png')
qs = PhotoImage(file='qs.png')

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("{}x{}".format(width, height))
root.title('GDV Project')

mainLabel = Label(root, bg='bisque2')
mainLabel.grid(row=0, column=0, sticky='nsew')

gdv = Label(mainLabel, text=' GDV Project \nLearn English', anchor=CENTER, font=('Times', 66), fg='red3', bg='bisque2')
gdv.grid(row=0, column=0, sticky='nsew', padx=(width//4 + 40), pady=height//32)

buttonFrame = Frame(mainLabel, borderwidth=6, height=340, width=520,  bg='bisque2')
buttonFrame.grid(row=1, column=0, columnspan=2, padx=30)

intro = Frame(mainLabel, width=500, height=150, bg='bisque2')
intro.grid(row=2, column=0)

link = Button(intro, image=yt, width=100, height=100)
link.grid(row=0, column=0, pady=18, padx=10)
link.config(command=open_link)


def ask1():
    root.destroy()
    try:
        importlib.reload(sys.modules['Trial'])
    except KeyError:
        pass
    import Trial
    Trial.f()

def ask2():
    root.destroy()
    try:
        importlib.reload(sys.modules['Trial'])
    except KeyError:
        pass
    import Trial
    Trial.s()

def ask3():
    root.destroy()
    try:
        importlib.reload(sys.modules['Trial'])
    except KeyError:
        pass
    import Trial
    Trial.t()



qst = Button(intro, image=qs, width=100, height=100, command=ask1)
qst.grid(row=0, column=1, pady=18, padx=10)
# link.config()

def OX():
    root.destroy()
    # import OX2
    try:
        importlib.reload(sys.modules['OX2'])
    except KeyError:
        pass
    import OX2
    OX2.start()

def easylev():
    root.destroy()
    set('easy_')
    try:
        importlib.reload(sys.modules['sizes'])
    except KeyError:
        pass
    import sizes
    sizes.start()

def mediumlev():
    root.destroy()
    set('medium_')
    try:
        importlib.reload(sys.modules['sizes'])
    except KeyError:
        pass
    import sizes
    sizes.start()

def hardlev():
    root.destroy()
    with open('db', 'w') as file2:
        print('hard', end='', file=file2)
    try:
        importlib.reload(sys.modules['sizes'])
    except KeyError:
        pass
    import sizes
    sizes.start()

def idioms():
    root.destroy()
    with open('db', 'w') as file3:
        print('idioms', end='', file=file3)
    try:
        importlib.reload(sys.modules['Idioms'])
    except KeyError:
        pass
    import Idioms
    Idioms.start()

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

def choose2(i = 0): #No TAB
    global buttonFrame
    global image1
    global image2
    global image3
    global mainLabel
    global height
    global width
    global open_link
    global intro
    buttonFrame.config(width=800)

    def levels():
        bt1.configure(text='Easy', fg='green', image=easy, command=easylev)
        bt2.configure(text='Medium', fg='steelblue', image=medium, command=mediumlev)
        bt3.configure(text='Hard', fg='red', image=hard, command=hardlev)

        gdv = Label(mainLabel, text=' GDV Project \nLearn English', anchor=CENTER, font=('Times', 66), fg='red3', bg='bisque2')
        gdv.grid(row=0, column=0, sticky='nsew', padx=(int(width//4) + 40), pady=int(height//32))

        link = Button(intro, image=yt, width=100, height=100)
        link.grid(row=0, column=0, pady=25)
        link.config(command=open_link)

        qst = Button(intro, image=qs, width=100, height=100, command=ask3)
        qst.grid(row=0, column=1, pady=25)

    bt1 = Button(buttonFrame, text='Learning Words', font=("Times", 40), fg='steelblue', command=levels)
    bt1.grid(row=0, column=0)
    bt1.configure(image=image1, compound=BOTTOM, height=int(width//5.5), bg='pink')

    bt2 = Button(buttonFrame, text='Game for Resting', font=("Times", 40), fg='steelblue', command=OX)
    bt2.grid(row=0, column=1, padx=30)
    bt2.configure(image=image2, compound=BOTTOM, height=int(width//5.5), bg='pink')

    bt3 = Button(buttonFrame, text='Learning Idioms', font=("Times", 40), fg='steelblue', command=idioms)
    bt3.grid(row=0, column=2)
    bt3.configure(image=image3, compound=BOTTOM, height=int(width//5.5), bg='pink')

    if i != 0:
        bt1.invoke()

    gdv = Label(mainLabel, text=' GDV Project \nLearn English', anchor=CENTER, font=('Times', 66), fg='red3', bg='bisque2')
    gdv.grid(row=0, column=0, sticky='nsew', padx=(int(width//4) + 40), pady=int(height//32))

    link = Button(intro, image=yt, width=100, height=100)
    link.grid(row=0, column=0, pady=25)
    link.config(command=open_link)

    qst = Button(intro, image=qs, width=100, height=100, command=ask2)
    qst.grid(row=0, column=1, pady=25)




def choose():
    global buttonFrame
    global img1
    global img2
    global width
    global but2
    global but1
    global choose2
    global link

    def ru():
        with open('lan', 'w') as file:
            print('ru', end='', file=file)
        but1.destroy()
        but2.destroy()
        choose2()

    def az():
        with open('lan', 'w') as file:
            print('az', end='', file=file)
        but1.destroy()
        but2.destroy()
        choose2()


    but1 = Button(buttonFrame, text='Azərbaycan Dili', font=("Times Azeri", 14), bg='orange')
    but1.grid(row=0, column=0, pady=5, padx=7)
    but1.config(compound=TOP, image=img1, width=int(width//5), height=int(width//5), borderwidth=3, command=az)

    but2 = Button(buttonFrame, text='Русский Язык', font=("Times", 14), bg='orange')
    but2.grid(row=0, column=1, pady=5, padx=7)
    but2.config(compound=TOP, image=img2, width=int(width//5), height=int(width//5), borderwidth=3, command=ru)


if __name__ == '__main__':
    choose()
    root.mainloop()


def start():
    global lan
    choose2()
    root.mainloop()

