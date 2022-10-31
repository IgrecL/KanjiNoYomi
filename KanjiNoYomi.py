import time, random, os
from tkinter import *

# start session
def start():
    # custom kanji mode
    if varList[6].get():
        file = open(str(os.path.dirname(__file__))+'/custom.txt')
        customKanji = file.readlines()[0]
        file = open(str(os.path.dirname(__file__))+'/kanji.txt')    
        for line in file.readlines():
            split = line.split('|')
            if split[0] in customKanji:
                kanjiList.append(line.split('|'))
    # normal mode
    else:
        # add selected JLPT levels
        for i in range(6):
            if varList[i].get():
                JLPTLevel.append(5-i)
        # add selected kanji to kanjiList
        file = open(str(os.path.dirname(__file__))+'/kanji.txt')
        for line in file.readlines():
            split = line.split('|')
            if int(split[1]) in JLPTLevel:
                kanjiList.append(line.split('|'))
    # delete tkinter widgets
    for i in range(7):
        checkbuttonList[i].destroy()
    titleLabel.destroy()
    startButton.destroy()
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
    progresslabel.configure(text=str(kanjiGoal-len(kanjiList))+'/'+str(kanjiGoal)+'    ')
    window.update()

# global variables
kanji = []
JLPTLevel = []
kanjiList = []

# window
window = Tk()
window.title('')
window.geometry('380x420')
window.resizable(False, False)
window.configure(bg='black')

# starting page
titleLabel = Label(window, text='漢字の読み', bg='black', fg='white', font=('Meiryo',30))
titleLabel.pack(ipady=15)
varList = []
checkbuttonList = []  
for i in range(7):
    if i<=5:
        txt = 'JLPT N'+str(5-i)
    else:
        txt = 'custom'
    var = StringVar(window)
    cb = Checkbutton(window, text=txt, variable=var, width=7, font=('Helvetica',10,'bold'), bd=5, bg='black', fg='white', activebackground='black', activeforeground='white', selectcolor='black')
    cb.pack(pady=2)
    checkbuttonList.append(cb)
    varList.append(var)
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
