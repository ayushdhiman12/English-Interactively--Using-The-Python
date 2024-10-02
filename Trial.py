from tkinter import *
import importlib
import sys

lan = ''
with open("lan") as file:
    lan = file.readline()

if lan == 'az':
    exp = ["Burada müxtəlif sözləri öyrənmək mümkündür.",
           "Əgər Siz istirahət eləmək istəyirsinizsə, bu oyun(iks nolik) Sizə uyğun ola bilər.",
           "Burada Siz idiomları(frazeoloji birləşmələri) oyrənərsiniz.",
           "Səviyyəni seçin.",
           ['Asan', 'Orta', 'Çətin'],
           ["Əsas", "Main"],
           ["Burada söz izah olunur.", "İstifadəçı bura sözünü ingiliscə yazır.",
            "Cavabı yazdıqca bu düyməyə basmaq lazımdır.",
            'Yuxarıda "Great" göstərlibsə, bura basın',
            "Bu düymə cavabını yuxarıda göstərir.",
            "Öz sözünü əlavə eləmək istəyirsinizsə, bu düyməyə basmaq lazımdır."],
           "Fasilə - vacibdir. Oyunu başlamaq üçün düyməyə basın(Siz kompyuter ilə oynayırsınız).",
           "Yeni oyun başlamaq üçün bura basmaq lazımdır",
           "Burada idiom göstərilir",
           "Idiomın düz mənasını göstərilən düyməyə basırsınız",
           ["Burada Siz sözünü ingiliscə yazırsınız", "Burada sözünü izah eləyirsiniz",
            "Əlavə eləmək üçün bura basırsınız. Diqqətli olun! Yazdıqlarınızda səhv olmamalıdır!", "Mahnı"]
           ,["Bura Siz idiomı ingiliscə yazırsınız","Bura idiomın izahını ingiliscə yazırsınız"]]
    font = ("Times Azeri", 22)
elif lan == 'ru':
    exp = ["Здесь можно выучить различные слова.",
           "Если Вы хотите отдохнуть, то эта игра(крестики нолики) может Вам подойти.",
           "Здесь Вы выучите идиомы(фразеологизмы).",
           "Выберите уровень",
           ["Лёгкий", "Средний", "Тяжёлый"],
           ["Главный", "Main"],
           ['Слово объясняется здесь.', "Сюда пользователь пишет слово по-английски.",
            "После написания слова нажмите сюда",
            'Если наверху появилось "Great", нажмите сюда',
            "Эта кнопка показывает ответ наверху.",
            "Если Вы хотите добавить своё слово, нажмите сюда"],
           "Перерыв - важная вещь. Для начала игры нажмите на любую кнопку(Игра идёт с компьютером). ",
           "Для начала новой игры нажмите сюда",
           "Здесь показывается идиома",
           "Нажимаете кнопку, которая показывает правильное значение идиомы",
           ["Здесь Вы пишите слово по-английски", "Здесь описываете его",
            "Для добавления нажмите сюда. Будьте внимательны! В написанном не должно быть ошибок!", 'Песня']
           ,["Сюда Вы пишите идиому по-английски","Сюда Вы пишите значение идиомы по-английски"]]
    font = ("Times", 22)

root = Tk()
root.title("GDV Project")
root['bg'] = 'bisque2'
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("{}x{}".format(width, height))

image1 = PhotoImage(file='vocabulary.png')
image2 = PhotoImage(file="game .png")
image3 = PhotoImage(file='idioms.png')
r = PhotoImage(file='r.png')
pl = PhotoImage(file='plus.png')

easy = PhotoImage(file='easy.png')
medium = PhotoImage(file='medium.png')
hard = PhotoImage(file='hard.png')

def back1():
    root.destroy()
    try:
        importlib.reload(sys.modules['MainWindow'])
    except KeyError:
        pass
    import MainWindow
    MainWindow.choose()


def back2():
    root.destroy()
    try:
        importlib.reload(sys.modules['MainWindow'])
    except KeyError:
        pass
    import MainWindow
    MainWindow.choose2()


def back3():
    root.destroy()
    try:
        importlib.reload(sys.modules['MainWindow'])
    except KeyError:
        pass
    import MainWindow
    MainWindow.choose2(1)

def back4():
    root.destroy()
    try:
        importlib.reload(sys.modules['sizes'])
    except KeyError:
        pass
    import sizes
    sizes.start()

def back5():
    root.destroy()
    try:
        importlib.reload(sys.modules['OX2'])
    except KeyError:
        pass
    import OX2
    OX2.start()

def back6():
    root.destroy()
    try:
        importlib.reload(sys.modules['Idioms'])
    except KeyError:
        pass
    import Idioms
    Idioms.start()

def back7():
    root.destroy()
    try:
        importlib.reload(sys.modules['Add'])
    except KeyError:
        pass
    import Add
    Add.start()

def f():
    gdv = Label(root, text=' GDV Project \nLearn English', anchor=CENTER, font=('Times', 66), fg='red3', bg='bisque2')
    gdv.grid(row=0, column=0, sticky='nsew', padx=(int(width//4) + 40), pady=int(height//32))

    ins = Label(root, text="Dili seçin \n Выберите язык", font=('Times', 66), bg='bisque2', fg='steelblue')
    ins.grid(row=1, column=0, sticky='nsew')

    backb = Button(root,  text='Back\nНазад\nArxaya', font=("Times", 35), fg='red', height=3, width=1, bg='bisque2', command=back1)
    backb.grid(row=2, column=0, sticky='nsew', padx=int(width//2.45))

def s():
    gdv = Label(root, text=' GDV Project \nLearn English', anchor=CENTER, font=('Times', 57), fg='red3', bg='bisque2')
    gdv.grid(row=0, column=0, sticky='nsew', padx=(int(width//4) + 90), pady=int(height//32), columnspan=3)
    bt1 = Button(root, text='Learning Words', font=("Times", 28), fg='steelblue')
    bt1.grid(row=1, column=0)
    bt1.configure(image=image1, compound=BOTTOM, height=int(width//5.6), bg='pink')

    bt2 = Button(root, text='Game for Resting', font=("Times", 28), fg='steelblue')
    bt2.grid(row=1, column=1)
    bt2.configure(image=image2, compound=BOTTOM, height=int(width//5.6), bg='pink')

    bt3 = Button(root, text='Learning Idioms', font=("Times", 28), fg='steelblue')
    bt3.grid(row=1, column=2)
    bt3.configure(image=image3, compound=BOTTOM, height=int(width//5.6), bg='pink')

    lb1 = Label(root, text=exp[0], font=font, fg='steelblue', wraplength=320)
    lb1.grid(row=2, column=0, pady=15)

    lb2 = Label(root, text=exp[1], font=font, fg='steelblue', wraplength=320)
    lb2.grid(row=2, column=1, pady=15)

    lb3 = Label(root, text=exp[2], font=font, fg='steelblue', wraplength=320)
    lb3.grid(row=2, column=2, pady=15)

    backb = Button(root,  text='Back', font=font, fg='red', bg='bisque2', command=back2)
    backb.grid(row=3, column=1)

def t():
    global font
    t, s = font
    s = 40
    font = t, s

    gdv = Label(root, text=' GDV Project \nLearn English', anchor=CENTER, font=('Times', 57), fg='red3', bg='bisque2')
    gdv.grid(row=0, column=0, sticky='nsew', padx=(int(width//4) + 90), pady=int(height//32), columnspan=3)
    lab = Label(root, text=exp[3], font=font, fg='steelblue', bg='bisque2')
    lab.grid(row=1, column=0, columnspan=3)

    but1 = Button(root, text='Easy', font=("Times", 40), fg='green', compound=BOTTOM, bg='pink')
    but1.grid(row=2, column=0, pady=24)
    but1.configure(image=easy, compound=BOTTOM, height=int(width//5.5))

    but2 = Button(root, text='Medium', font=("Times", 40), fg='steelblue', compound=BOTTOM, bg='pink')
    but2.grid(row=2, column=1)
    but2.configure(image=medium, compound=BOTTOM, height=int(width//5.5))

    but3 = Button(root, text='Hard', font=("Times", 40), fg='red', compound=BOTTOM, bg='pink')
    but3.grid(row=2, column=2)
    but3.configure(image=hard, compound=BOTTOM, height=int(width//5.5))

    s = 28
    font = t, s
    lb1 = Label(root, text=exp[4][0], font=font, fg='steelblue', bg='bisque2')
    lb1.grid(row=3, column=0)

    lb2 = Label(root, text=exp[4][1], font=font, fg='steelblue', bg='bisque2')
    lb2.grid(row=3, column=1)

    lb3 = Label(root, text=exp[4][2], font=font, fg='steelblue', bg='bisque2')
    lb3.grid(row=3, column=2)

    backb = Button(root,  text='Back', font=font, fg='red', bg='bisque2', command=back3)
    backb.grid(row=4, column=1)

def ft():
    global font
    var = StringVar()
    var.set(exp[5][1])

    frame2 = Frame(root, bg='bisque2')
    frame2.grid(row=1,column=0)

    gdv = Label(root, text=' GDV Project \nLearn English', anchor=CENTER, font=('Times', 47), fg='red3', bg='bisque2')
    gdv.grid(row=0, column=0, sticky='nsew', padx=(width//4 + 90), pady=int(height//32), columnspan=3)

    lb2 = Label(frame2, borderwidth=5, width=int(width//47.479), bg='green', text=exp[5][0])
    lb2.grid(row=0, column=0, sticky='n', pady=16, padx=25)
    lb2.config(font=font)

    l = Label(frame2, text=exp[6][0], font=font, fg='steelblue')
    l.grid(row=1, column=0)

    lb3 = Entry(frame2, textvariable=var, width=int(width//39.5), borderwidth=5, bg='green')
    lb3.grid(row=2, column=0, sticky='n', pady=25, padx=25)
    lb3.config(font=font)

    l1 = Label(frame2, text=exp[6][1], font=font, fg='steelblue')
    l1.grid(row=3, column=0,)

    frame = Frame(root, bg='bisque2')
    frame.grid(row=1, column=1, pady=16)

    b1 = Button(frame, text='Try', font=("Times", 35), width=5, height=2, bg='white')
    b1.grid(row=0, column=0, padx=18)

    l2 = Label(frame, text=exp[6][2], font=font, fg='steelblue', wraplength=170)
    l2.grid(row=1, column=0, sticky='ns')

    b2 = Button(frame, image=r, width=140, height=140, bg='white')
    b2.grid(row=0, column=1, padx=18)

    l3 = Label(frame, text=exp[6][3], font=font, fg='steelblue', wraplength=170)
    l3.grid(row=1, column=1, sticky='ns')

    b3 = Button(frame, text='Hint', font=("Times", 35), width=5, height=2, bg='white')
    b3.grid(row=0, column=2, sticky='w', padx=18)

    l4 = Label(frame, text=exp[6][4], font=font, fg='steelblue', wraplength=170)
    l4.grid(row=1, column=2, sticky='ns')

    b6 = Button(frame, image=pl, width=140, height=140, bg='white')
    b6.grid(row=0, column=3, sticky='w', padx=18)

    l5 = Label(frame, text=exp[6][5], font=font, fg='steelblue', wraplength=170)
    l5.grid(row=1, column=3, sticky='ns')

    backb = Button(root,  text='Back', font=font, fg='red', bg='bisque2', command=back4)
    backb.grid(row=4, column=0, columnspan=4)

def ox():
    gdv = Label(root, text=' GDV Project \nLearn English', anchor=CENTER, font=('Times', 47), fg='red3', bg='bisque2')
    gdv.grid(row=0, column=0, sticky='nsew', padx=(width//4 + 90), pady=int(height//32), columnspan=3)

    ml = Label(root, text=exp[7], font=font, fg='steelblue', wraplength=800)
    ml.grid(row=1, column=0, sticky='e', padx=int(width//6.3), pady=25)

    newgame = Button(root, text='New Game', height=1, width=10, font=("Times", 22), fg='red')
    newgame.grid(row=3, column=0, pady=15)

    ml2 = Label(root, text=exp[8], font=font, fg='steelblue', wraplength=800)
    ml2.grid(row=2, column=0)

    backb = Button(root,  text='Back', font=font, fg='red', bg='bisque2', command=back5)
    backb.grid(row=4, column=0, columnspan=4)

def id():
    gdv = Label(root, text=' GDV Project \nLearn English', anchor=CENTER, font=('Times', 47), fg='red3', bg='bisque2')
    gdv.grid(row=0, column=0, sticky='nsew', padx=(width//4 + 90), pady=int(height//32), columnspan=3)

    lb2 = Label(root, borderwidth=5, bg='lawngreen', wraplength=1200, text="All in all")
    lb2.grid(row=1, column=0, sticky='nsew', padx=int(width//10), pady=16)
    lb2.config(font=("Times", 33))

    e = Label(root, text=exp[9], font=font, fg='steelblue')
    e.grid(row=2, column=0)

    bt1 = Button(root, text='Considering everything', font=("Times", 26), borderwidth=2)
    bt1.grid(row=3, column=0, sticky='nsew', padx=int(width//10), pady=15)

    e = Label(root, text=exp[10], font=font, fg='steelblue', wraplength=500)
    e.grid(row=4, column=0)

    next = Button(root, text='NEXT', bg='white', font=("Times", 27), fg='green')
    next.grid(row=1, column=1, sticky='ew', padx=15)

    lb = Label(root, text=exp[6][3], font=font, fg='steelblue', wraplength=1700)
    lb.grid(row=2, column=1)

    b6 = Button(root, image=pl, width=140, height=140, bg='white')
    b6.grid(row=3, column=1, sticky='w', padx=240, pady=15)

    l5 = Label(root, text=exp[6][5], font=font, fg='steelblue', wraplength=600)
    l5.grid(row=4, column=1, sticky='ns')


    backb = Button(root,  text='Back', font=font, fg='red', bg='bisque2', command=back6)
    backb.grid(row=5, column=0, columnspan=4, pady=15)

def last():
    gdv = Label(root, text=' GDV Project \nLearn English', anchor=CENTER, font=('Times', 47), fg='red3', bg='bisque2')
    gdv.grid(row=0, column=0, sticky='nsew', padx=(width//4 + 90), pady=int(height//32), columnspan=3)

    frame = Frame(root, bg='orange2')
    frame.grid(row=1, column=0, sticky='nsew', padx=int(width//8))

    word = Label(frame, text='Word:', fg='steelblue', font=('Times', 33))
    word.grid(row=0, column=0, padx=20, pady=30, sticky='nsew')

    word_var = StringVar()
    word_var.set("Song")
    word_entry = Entry(frame, borderwidth=3, font=font, textvariable=word_var, fg='steelblue')
    word_entry.grid(row=0, column=1, sticky='nsew', pady=30)

    expl = Label(frame, text='Explain:', fg='steelblue', font=('Times', 33))
    expl.grid(row=1, column=0, padx=20, sticky='nsew', pady=15)

    exp_var = StringVar()
    exp_var.set(exp[11][-1])
    exp_entry = Entry(frame, borderwidth=3, font=font, textvariable=exp_var, fg='steelblue')
    exp_entry.grid(row=1, column=1, sticky='nsew', pady=15)

    lab = Label(frame, text=exp[11][0], font=font, fg='steelblue', wraplength=600)
    lab.grid(row=0, column=2, padx=15 )

    lab1 = Label(frame, text=exp[11][1], font=font, fg='steelblue', wraplength=600)
    lab1.grid(row=1, column=2, padx=15)

    lab1 = Label(root, text=exp[11][2], font=font, fg='steelblue', wraplength=600)
    lab1.grid(row=2, column=0, pady=25)

    add = Button(root, text='Add', fg='red2', font=("Times", 33))
    add.grid(row=3, column=0)

    backb = Button(root,  text='Back', font=font, fg='red', bg='bisque2', command=back7)
    backb.grid(row=5, column=0, columnspan=4, pady=15)

def alast():
    gdv = Label(root, text=' GDV Project \nLearn English', anchor=CENTER, font=('Times', 47), fg='red3', bg='bisque2')
    gdv.grid(row=0, column=0, sticky='nsew', padx=(width//4 + 90), pady=int(height//32), columnspan=3)

    frame = Frame(root, bg='orange2')
    frame.grid(row=1, column=0, sticky='nsew', padx=int(width//8))

    word = Label(frame, text='Word:', fg='steelblue', font=('Times', 33))
    word.grid(row=0, column=0, padx=20, pady=30, sticky='nsew')

    word_var = StringVar()
    word_var.set("Once in a blue moon")
    word_entry = Entry(frame, borderwidth=3, font=font, textvariable=word_var, fg='steelblue')
    word_entry.grid(row=0, column=1, sticky='nsew', pady=30)

    expl = Label(frame, text='Explain:', fg='steelblue', font=('Times', 33))
    expl.grid(row=1, column=0, padx=20, sticky='nsew', pady=15)

    exp_var = StringVar()
    exp_var.set("Rarely")
    exp_entry = Entry(frame, borderwidth=3, font=font, textvariable=exp_var, fg='steelblue')
    exp_entry.grid(row=1, column=1, sticky='nsew', pady=15)

    lab = Label(frame, text=exp[12][0], font=font, fg='steelblue', wraplength=600)
    lab.grid(row=0, column=2, padx=15 )

    lab1 = Label(frame, text=exp[12][1], font=font, fg='steelblue', wraplength=600)
    lab1.grid(row=1, column=2, padx=15)

    lab1 = Label(root, text=exp[11][2], font=font, fg='steelblue', wraplength=600)
    lab1.grid(row=2, column=0, pady=25)

    add = Button(root, text='Add', fg='red2', font=("Times", 33))
    add.grid(row=3, column=0)

    backb = Button(root,  text='Back', font=font, fg='red', bg='bisque2', command=back7)
    backb.grid(row=5, column=0, columnspan=4, pady=15)


lb = Label(root, text='Everything made by GDV(Grechkin Dmitry Vladimirovich)', font=("Times", 12), fg='red2', bg='bisque2')
lb.grid(row=7, column=0)

if __name__ == '__main__':
    root.mainloop()

def start():
    root.mainloop()

