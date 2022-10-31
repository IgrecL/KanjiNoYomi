import time, random, os
from tkinter import *

# add or remove JLPT level to session
def check(i):
    if i not in JLPTLevel:
        JLPTLevel.append(i)
    else:
        JLPTLevel.remove(i)

# start session
def start():
    if not kanjiList:
        # delete tkinter widgets in the starting page
        titleLabel.destroy()
        N5.destroy()
        N4.destroy()
        N3.destroy()
        N2.destroy()
        N1.destroy()    
        N0.destroy()  
        startButton.destroy()
        # add selected kanji to kanjiList
        file = open(str(os.path.dirname(__file__))+'/kanji.txt')
        for line in file.readlines():
            split = line.split('|')
            if int(split[1]) in JLPTLevel:
                kanjiList.append(line.split('|'))
        global kanjiGoal
        kanjiGoal = len(kanjiList)
        # selecting first kanji
        nextKanji()
 
# color flash when answering right or wrong
def changeColor(color):
    furiganaLabel.configure(fg=color)
    kanjiLabel.configure(fg=color)
    inputField.configure(fg=color)
    window.update()

# when pressing enter
def validate(e):
    if e.keysym == 'Return':
        furiganaLabel.configure(text=kanji[2])
        correct = ((inputField.get() == '') and (kanji[2] == '')) or ((inputField.get() != '') and ((inputField.get() == kanji[3]) or (inputField.get() == kanji[4]) or (inputField.get() == kanji[5])))
        if correct:
            changeColor('green')
            window.update()
            time.sleep(0.1)
            kanjiList.remove(kanji)
        else:  
            changeColor('red')
            inputField.delete(0,END)
            inputField.insert(0,kanji[3])
            window.update()
            print(kanji[0])
            time.sleep(1)
        nextKanji()    
        changeColor('white')
        
# remove the kanji if correct and choose the next one
def nextKanji():
    if len(kanjiList) == 0:
        quit()
    global kanji
    kanji = kanjiList[random.choice(range(len(kanjiList)))]
    furiganaLabel.configure(text='')
    kanjiLabel.configure(text=kanji[0])
    inputField.delete(0,END)
    progresslabel.configure(text=str(len(kanjiList))+'/'+str(kanjiGoal)+'    ')
    window.update()

# global variables
kanji = []
JLPTLevel = []
kanjiList = []
kanjiGoal = 0

# window
window = Tk()
window.title('')
window.geometry('380x420')
window.resizable(False, False)
window.configure(bg='black')

# starting page
titleLabel = Label(window, text='漢字の読み', bg='black', fg='white', font=('Meiryo',30))
titleLabel.pack(ipady=15)
checkbuttonArray = []  
N5 = Checkbutton(window, text='N5', command=lambda: check(5), font=('Helvetica',10,'bold'), bd=5, bg='black', fg='white', activebackground='black', activeforeground='white', selectcolor='black')
N4 = Checkbutton(window, text='N4', command=lambda: check(4), font=('Helvetica',10,'bold'), bd=5, bg='black', fg='white', activebackground='black', activeforeground='white', selectcolor='black')
N3 = Checkbutton(window, text='N3', command=lambda: check(3), font=('Helvetica',10,'bold'), bd=5, bg='black', fg='white', activebackground='black', activeforeground='white', selectcolor='black')
N2 = Checkbutton(window, text='N2', command=lambda: check(2), font=('Helvetica',10,'bold'), bd=5, bg='black', fg='white', activebackground='black', activeforeground='white', selectcolor='black')
N1 = Checkbutton(window, text='N1', command=lambda: check(1), font=('Helvetica',10,'bold'), bd=5, bg='black', fg='white', activebackground='black', activeforeground='white', selectcolor='black')
N0 = Checkbutton(window, text='N0', command=lambda: check(0), font=('Helvetica',10,'bold'), bd=5, bg='black', fg='white', activebackground='black', activeforeground='white', selectcolor='black')
N5.pack(pady=2)
N4.pack(pady=2)
N3.pack(pady=2)
N2.pack(pady=2)  
N1.pack(pady=2)
N0.pack(pady=2)
startButton = Button(window, command=start, text='START', width=19, bg='black', fg='white', activebackground='black', activeforeground='white', font=('Helvetica',15,'bold'))
startButton.pack(ipady=5, pady=30)

# main page
furiganaLabel = Label(window, bg='black', fg='white', font=('Meiryo',40))
furiganaLabel.pack()
kanjiLabel = Label(window, bg='black', fg='white', font=('Meiryo',140))
kanjiLabel.pack(ipady=20)
inputField = Entry(window, bg='black', fg='white', bd=0, font=('Helvetica',40,'bold'), justify=CENTER)
inputField.focus_set()
inputField.pack()
progresslabel = Label(window, bg='black', fg='white', font=('Meiryo',20))
progresslabel.pack(ipady=100,anchor='e')

window.bind('<KeyRelease>', validate)
window.mainloop()
