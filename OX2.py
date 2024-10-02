from tkinter import *
import sys
import importlib


import random
labels = ['label1', 'label2', 'label3', 'label4', 'label5', 'label6', 'label7', 'label8', 'label9']
turn = 0

def check():
    global labels
    global opponent
    global main_label
    if len(labels) != 0:
        if main_label['text'] == 'Play':
            opponent()
def player_wins():
    global main_label
    main_label.configure(font=('Times', 44), text='Player Wins')
def computer_wins():
    global main_label
    main_label.configure(font=('Times', 44), text='Computer Wins')
def end2():
    global label1
    global label2
    global label3
    global label4
    global label5
    global label6
    global label7
    global label8
    global label9
    global turn
    global result

    t1 = label1['textvariable']
    t2 = label2['textvariable']
    t3 = label3['textvariable']
    t4 = label4['textvariable']
    t5 = label5['textvariable']
    t6 = label6['textvariable']
    t7 = label7['textvariable']
    t8 = label8['textvariable']
    t9 = label9['textvariable']

    if t1 == t2 == t3 != '':
        result(t1)
    if t4 == t5 == t6 != '':
        result(t4)
    if t7 == t8 == t9 != '':
        result(t7)
    if t1 == t4 == t7 != '':
        result(t7)
    if t2 == t5 == t8 != '':
        result(t2)
    if t3 == t6 == t9 != '':
        result(t6)
    if t1 == t5 == t9 != '':
        result(t1)
    if t3 == t5 == t7 != '':
        result(t7)
def result(int):
    global player_wins
    global computer_wins

    if int == 'x':
        player_wins()

    elif int == 'o':
        computer_wins()
def opponent():
    global label1
    global label2
    global label3
    global label4
    global label5
    global label6
    global label7
    global label8
    global label9
    global labels
    global main_label
    global turn
    c = random.choice(labels)
    if c == 'label1':
        label1.configure(height=155, width=145, image=imgo)
        try:
            labels.remove('label1')
        except ValueError:
            label1.configure(fg='red', font=("Time",31), text='ERROR')
        label1['textvariable'] = 'o'


    if c == 'label2':
        label2.configure(height=155, width=145, image=imgo)
        try:
            labels.remove('label2')
        except ValueError:
            label2.configure(fg='red', font=("Time",31), text='ERROR')
        label2['textvariable'] = 'o'


    if c == 'label3':
        label3.configure(height=155, width=145, image=imgo)
        try:
            labels.remove('label3')
        except ValueError:
            label3.configure(fg='red', font=("Time",31), text='ERROR')
        label3['textvariable'] = 'o'


    if c == 'label4':
        label4.configure(height=155, width=145, image=imgo)
        try:
            labels.remove('label4')
        except ValueError:
            label4.configure(fg='red', font=("Time",31), text='ERROR')
        label4['textvariable'] = 'o'


    if c == 'label5':
        label5.configure(height=155, width=145, image=imgo)
        try:
            labels.remove('label5')
        except ValueError:
            label5.configure(fg='red', font=("Time",31), text='ERROR')
        label5['textvariable'] = 'o'


    if c == 'label6':
        label6.configure(height=155, width=145, image=imgo)
        try:
            labels.remove('label6')
        except ValueError:
            label6.configure(fg='red', font=("Time",31), text='ERROR')
        label6['textvariable'] = 'o'


    if c == 'label7':
        label7.configure(height=155, width=145, image=imgo)
        try:
            labels.remove('label7')
        except ValueError:
            label7.configure(fg='red', font=("Time",31), text='ERROR')
        label7['textvariable'] = 'o'


    if c == 'label8':
        label8.configure(height=155, width=145, image=imgo)
        try:
            labels.remove('label8')
        except ValueError:
            label8.configure(fg='red', font=("Time",31), text='ERROR')
        label8['textvariable'] = 'o'


    if c == 'label9':
        label9.configure(height=155, width=145, image=imgo)
        try:
            labels.remove('label9')
        except ValueError:
            label9.configure(fg='red', font=("Time",31), text='ERROR')
        label9['textvariable'] = 'o'


    turn += 1
    end2()

def end():
    global label1
    global label2
    global label3
    global label4
    global label5
    global label6
    global label7
    global label8
    global label9
    global turn

    t1 = label1['textvariable']
    t2 = label2['textvariable']
    t3 = label3['textvariable']
    t4 = label4['textvariable']
    t5 = label5['textvariable']
    t6 = label6['textvariable']
    t7 = label7['textvariable']
    t8 = label8['textvariable']
    t9 = label9['textvariable']

    if t1 == t2 == t3 != '':
        result(t1)
    if t4 == t5 == t6 != '':
        result(t4)
    if t7 == t8 == t9 != '':
        result(t7)
    if t1 == t4 == t7 != '':
        result(t7)
    if t2 == t5 == t8 != '':
        result(t2)
    if t3 == t6 == t9 != '':
        result(t6)
    if t1 == t5 == t9 != '':
        result(t1)
    if t3 == t5 == t7 != '':
        result(t7)
    # print(turn)
    if turn != 8:
        turn += 1
    else:
        if t1 == t2 == t3 != '':
            result(t1)
        if t4 == t5 == t6 != '':
            result(t4)
        if t7 == t8 == t9 != '':
            result(t7)
        if t1 == t4 == t7 != '':
            result(t7)
        if t2 == t5 == t8 != '':
            result(t2)
        if t3 == t6 == t9 != '':
            result(t3)
        if t1 == t5 == t9 != '':
            result(t1)
        if t3 == t5 == t7 != '':
            result(t7)

mainLabel = Tk()
width = mainLabel.winfo_screenwidth()
height = mainLabel.winfo_screenheight()
mainLabel.geometry("{}x{}".format(width, height))
mainLabel.title('GDV programming')

def but1():
    global label1
    label1.configure(height=155, width=145, image=imgx)
    try:
        labels.remove('label1')
        label1['textvariable'] = 'x'
    except ValueError:
        label1.configur(fg='red', font=("Time",31), text='ERROR')

    end()
    check()
def but2():
    global label2
    label2.configure(height=155, width=145, image=imgx)
    try:
        labels.remove('label2')
    except ValueError:
        label2.configure(fg='red', font=("Time",31), text='ERROR')
    label2['textvariable'] = 'x'
    end()
    check()
def but3():
    global label3
    label3.configure(height=155, width=145, image=imgx)
    try:
        labels.remove('label3')
        label3['textvariable'] = 'x'
    except ValueError:
        label3.configure(fg='red', font=("Time",31), text='ERROR')
    end()
    check()
def but4():
    global label4
    label4.configure(height=155, width=145, image=imgx)
    try:
        labels.remove('label4')
        label4['textvariable'] = 'x'
    except ValueError:
        label4.configure(fg='red', font=("Time",31), text='ERROR')
    end()
    check()
def but5():
    global label5
    label5.configure(height=155, width=145, image=imgx)
    try:
        labels.remove('label5')
        label5['textvariable'] = 'x'
    except ValueError:
        label5.configure(fg='red', font=("Time",31), text='ERROR')
    end()
    check()
def but6():
    global label6
    label6.configure(height=155, width=145, image=imgx)
    try:
        labels.remove('label6')
        label6['textvariable'] = 'x'
    except ValueError:
        label6.configure(fg='red', font=("Time",31), text='ERROR')
    end()
    check()
def but7():
    global label7
    label7.configure(height=155, width=145, image=imgx)
    try:
        labels.remove('label7')
    except ValueError:
        label7.configure(fg='red', font=("Time",31), text='ERROR')
    label7['textvariable'] = 'x'
    end()
    check()
def but8():
    global label8
    label8.configure(height=155, width=145, image=imgx)
    try:
        labels.remove('label8')
        label8['textvariable'] = 'x'
    except ValueError:
        label8.configure(fg='red', font=("Time",31), text='ERROR')
    end()
    check()
def but9():
    global label9
    label9.configure(height=155, width=145, image=imgx)
    try:
        labels.remove('label9')
        label9['textvariable'] = 'x'

    except ValueError:
        label9.configure(fg='red', font=("Time",31), text='ERROR')
    end()
    check()
imgo = PhotoImage(file='o.png')
imgx = PhotoImage(file='x.png')
qs = PhotoImage(file='qs.png')


main_label = Label(mainLabel, font=("Time", 44), text='Play')
main_label.grid(row=0, column=0, sticky='nsew', padx=430, pady=20)

mainLabel.configure(background='orange')
game_desk = Frame(mainLabel)
game_desk.grid(row=1, column=0, padx=400)

def new_game():
    global label1
    global label2
    global label3
    global label4
    global label5
    global label6
    global label7
    global label8
    global label9
    global labels
    global main_label
    global turn
    global but1

    turn = 0
    try:
        main_label.destroy()
    except TclError:
        pass
    try:
        label1.destroy()
    except TclError:
        pass
    try:
        label2.destroy()
    except TclError:
        pass
    try:
        label3.destroy()
    except TclError:
        pass
    try:
        label4.destroy()
    except TclError:
        pass
    try:
        label5.destroy()
    except TclError:
        pass
    try:
        label6.destroy()
    except TclError:
        pass
    try:
        label7.destroy()
    except TclError:
        pass
    try:
        label8.destroy()
    except TclError:
        pass
    try:
        label9.destroy()
    except TclError:
        pass

    label1 = Button(sector1, height=10, width=20, relief='raised', command=but1, textvariable='')
    label1.grid(row=0, column=0, sticky='nsew')

    label2 = Button(sector2, height=10, width=20, relief='raised', command=but2, textvariable='')
    label2.grid(row=0, column=0, sticky='nsew')

    label3 = Button(sector3, height=10, width=20, relief='raised', command=but3, textvariable='')
    label3.grid(row=0, column=0, sticky='nsew')

    label4 = Button(sector4, height=10, width=20, relief='raised', command=but4, textvariable='')
    label4.grid(row=0, column=0, sticky='nsew')

    label5 = Button(sector5, height=10, width=20, relief='raised', command=but5, textvariable='')
    label5.grid(row=0, column=0, sticky='nsew')

    label6 = Button(sector6, height=10, width=20, relief='raised', command=but6, textvariable='')
    label6.grid(row=0, column=0, sticky='nsew')

    label7 = Button(sector7, height=10, width=20, relief='raised', command=but7, textvariable='')
    label7.grid(row=0, column=0, sticky='nsew')

    label8 = Button(sector8, height=10, width=20, relief='raised', command=but8, textvariable='')
    label8.grid(row=0, column=0, sticky='nsew')

    label9 = Button(sector9, height=10, width=20, relief='raised', command=but9, textvariable='')
    label9.grid(row=0, column=0, sticky='nsew')

    labels = ['label1', 'label2', 'label3', 'label4', 'label5', 'label6', 'label7', 'label8', 'label9']
    main_label = Label(mainLabel, font=("Time", 44), text='Play')
    main_label.grid(row=0, column=0,  sticky='nsew', padx=430, pady=20)

sector1 = LabelFrame(game_desk, borderwidth=2)
sector1.grid(row=0, column=0, sticky='nsew')
label1 = Button(sector1, height=10, width=20, relief='raised', command=but1, compound=CENTER, textvariable='')
label1.grid(row=0, column=0, sticky='nsew')
sector2 = LabelFrame(game_desk, borderwidth=2)
sector2.grid(row=0, column=1, sticky='nsew')
label2 = Button(sector2, height=10, width=20, relief='raised', command=but2, compound=CENTER, textvariable='')
label2.grid(row=0, column=0, sticky='nsew')
sector3 = LabelFrame(game_desk, borderwidth=2)
sector3.grid(row=0, column=2, sticky='nsew')
label3 = Button(sector3, height=10, width=20, relief='raised', command=but3, compound=CENTER, textvariable='')
label3.grid(row=0, column=0, sticky='nsew')
sector4 = LabelFrame(game_desk, borderwidth=2, width=40, height=40)
sector4.grid(row=1, column=0, sticky='nsew')
label4 = Button(sector4, height=10, width=20, relief='raised', command=but4, compound=CENTER, textvariable='')
label4.grid(row=0, column=0, sticky='nsew')
sector5 = LabelFrame(game_desk, borderwidth=2)
sector5.grid(row=1, column=1, sticky='nsew')
label5 = Button(sector5, height=10, width=20, relief='raised', command=but5, compound=CENTER, textvariable='')
label5.grid(row=0, column=0, sticky='nsew')
sector6 = LabelFrame(game_desk, borderwidth=2)
sector6.grid(row=1, column=2, sticky='nsew')
label6 = Button(sector6, height=10, width=20, relief='raised', command=but6, compound=CENTER, textvariable='')
label6.grid(row=0, column=0, sticky='nsew')
sector7 = LabelFrame(game_desk, borderwidth=2, width=40, height=40)
sector7.grid(row=2, column=0, sticky='nsew')
label7 = Button(sector7, height=10, width=20, relief='raised', command=but7, compound=CENTER, textvariable='')
label7.grid(row=0, column=0, sticky='nsew')
sector8 = LabelFrame(game_desk, borderwidth=2)
sector8.grid(row=2, column=1, sticky='nsew')
label8 = Button(sector8, height=10, width=20, relief='raised', command=but8, compound=CENTER, textvariable='')
label8.grid(row=0, column=0, sticky='nsew')
sector9 = LabelFrame(game_desk, borderwidth=2)
sector9.grid(row=2, column=2, sticky='nsew')
label9 = Button(sector9, height=10, width=20, relief='raised', command=but9, compound=CENTER, textvariable='')
label9.grid(row=0, column=0, sticky='nsew')
button_frame = LabelFrame(borderwidth=10, text=' GDV PROJECT ', font=('Times',  33), fg='green', bg='pink2')
button_frame.grid(row=1, column=0, sticky='nw', padx=30, pady=95)
newgame = Button(button_frame, text='New Game', height=1, width=8, font=("Times", 22))
newgame.grid(row=2, column=0, padx=15, pady=10)
newgame.configure(command=new_game, fg='red')

for i in range(3):
    mainLabel.rowconfigure(i, weight=2)
    mainLabel.columnconfigure(i, weight=2)

def ask():
    mainLabel.destroy()
    try:
        importlib.reload(sys.modules['Trial'])
    except KeyError:
        pass
    import Trial
    Trial.ox()

def back():
    mainLabel.destroy()
    try:
        importlib.reload(sys.modules['MainWindow'])
    except KeyError:
        pass
    import MainWindow
    MainWindow.start()

qt = Button(button_frame, text='Back', height=1, width=8, font=("Times", 22), fg='red', command = back)
qt.grid(row=2, column=1, padx=15, pady=10)

qst = Button(button_frame, image=qs, command=ask)
qst.grid(row=3, column=0, columnspan=2)

new_game()
# mainLabel.mainloop()
if __name__ == '__main__':
    mainLabel.mainloop()

if __name__ != '__main__':
    pass

def start():
    mainLabel.mainloop()
