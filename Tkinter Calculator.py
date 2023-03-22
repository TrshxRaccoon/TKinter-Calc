from tkinter import *
from tkmacosx import *
from math import *
func = 0
switch = True
window = Tk()
window.title('Calculator')

Display = Entry(window,borderwidth=0,font=('SF 22'))
Display.grid(row=0,column=1,columnspan=3,sticky='EW')
Display.insert(0,'0')

def button_click(number):
    global func
    if Display.get()=='0' and number!='.':
        Display.delete(0,END)
    elif Display.get()=='-0':
        Display.delete(1,END)
    if type(number) == str and number != '.':
        if Display.get()[len(Display.get())-1] in '+-/×':
            Display.delete(len(Display.get())-1,END)
        if number == '+':
            Display.insert(END,'+')
            buttonAdd.config(bg='white',fg='orange')
            buttonSub.config(bg='orange',fg='white')
            buttonMul.config(bg='orange',fg='white')
            buttonDiv.config(bg='orange',fg='white')
        elif number == '-':
            Display.insert(END,'-')
            buttonSub.config(bg='white',fg='orange')
            buttonAdd.config(bg='orange',fg='white')
            buttonMul.config(bg='orange',fg='white')
            buttonDiv.config(bg='orange',fg='white')
        elif number == '×':
            Display.insert(END,'×')
            buttonMul.config(bg='white',fg='orange')
            buttonAdd.config(bg='orange',fg='white')
            buttonSub.config(bg='orange',fg='white')
            buttonDiv.config(bg='orange',fg='white')
        elif number == '÷':
            Display.insert(END,'/')
            buttonDiv.config(bg='white',fg='orange')
            buttonAdd.config(bg='orange',fg='white')
            buttonSub.config(bg='orange',fg='white')
            buttonMul.config(bg='orange',fg='white')
        buttonInvertSign.config(state=DISABLED)
    else:
        Display.insert(END,number)
    func = 0

def button_fact():
    p = 1
    ans = round(eval(Display.get()))
    for i in range(2,ans+1):
        p *= i
    Display.delete(0,END)
    Display.insert(0,p)
    buttonAdd.config(bg='orange',fg='white')
    buttonSub.config(bg='orange',fg='white')
    buttonMul.config(bg='orange',fg='white')
    buttonDiv.config(bg='orange',fg='white')
def button_root():
    ans = sqrt(eval(Display.get()))
    Display.delete(0,END)
    Display.insert(0,ans)
    buttonAdd.config(bg='orange',fg='white')
    buttonSub.config(bg='orange',fg='white')
    buttonMul.config(bg='orange',fg='white')
    buttonDiv.config(bg='orange',fg='white')
def button_exp():
    Display.insert(END,'^')

def button_equal():
    global func,switch
    buttonAdd.config(bg='orange',fg='white')
    buttonSub.config(bg='orange',fg='white')
    buttonMul.config(bg='orange',fg='white')
    buttonDiv.config(bg='orange',fg='white')
    buttonInvertSign.config(state=NORMAL)
    if func == -1:
        Display.delete(0,END)
        Display.insert(0,'Syntax Error')           
        buttonAdd.config(state=DISABLED)
        buttonSub.config(state=DISABLED)
        buttonMul.config(state=DISABLED)
        buttonDiv.config(state=DISABLED)
        buttonFact.config(state=DISABLED)
        buttonRoot.config(state=DISABLED)
        buttonDecimal.config(state=DISABLED)
        buttonDelete.config(state=DISABLED)
        buttonEqual.config(state=DISABLED)
        buttonInvertSign.config(state=DISABLED)
        buttonPi.config(state=DISABLED)
        button0.config(state=DISABLED)
        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)
        buttonClear.config(bg='pink')
    elif switch:
        try:
            ans = eval(Display.get().replace('×','*').replace('π','3.1415926535897932').replace('^','**'))
            Display.delete(0,END)
            Display.insert(0,ans)
        except (ZeroDivisionError,SyntaxError):
            switch = False
            func = -1
            button_equal()
    return True
def button_del():
    Display.delete(len(Display.get())-1,END) 
    if len(Display.get())==0 or Display.get()=='-':
        Display.insert(0,'0')
def button_clear():
    Display.delete(0,END)
    Display.insert(0,'0')
    buttonAdd.config(state=NORMAL)
    buttonSub.config(state=NORMAL)
    buttonMul.config(state=NORMAL)
    buttonDiv.config(state=NORMAL)
    buttonFact.config(state=NORMAL)
    buttonRoot.config(state=NORMAL)
    buttonDecimal.config(state=NORMAL)
    buttonDelete.config(state=NORMAL)
    buttonEqual.config(state=NORMAL)
    buttonInvertSign.config(state=NORMAL)
    buttonPi.config(state=NORMAL)
    button0.config(state=NORMAL)
    button1.config(state=NORMAL)
    button2.config(state=NORMAL)
    button3.config(state=NORMAL)
    button4.config(state=NORMAL)
    button5.config(state=NORMAL)
    button6.config(state=NORMAL)
    button7.config(state=NORMAL)
    button8.config(state=NORMAL)
    button9.config(state=NORMAL)
    buttonClear.config(bg='lightgrey')
def button_pn():
    if Display.get()[0] == '-':
        Display.delete(0,1)
        Display.insert(0,'')
    else:
        Display.insert(0,'-')
def button_pi():
    Display.insert(len(Display.get()),'π')

#DIGITS 0 TO 9
button1 = Button(window,bg='grey',fg='white',text='1',font=('SF 18'),command=lambda: button_click(1))
button2 = Button(window,bg='grey',fg='white',text='2',font=('SF 18'),command=lambda: button_click(2))
button3 = Button(window,bg='grey',fg='white',text='3',font=('SF 18'),command=lambda: button_click(3))
button4 = Button(window,bg='grey',fg='white',text='4',font=('SF 18'),command=lambda: button_click(4))
button5 = Button(window,bg='grey',fg='white',text='5',font=('SF 18'),command=lambda: button_click(5))
button6 = Button(window,bg='grey',fg='white',text='6',font=('SF 18'),command=lambda: button_click(6))
button7 = Button(window,bg='grey',fg='white',text='7',font=('SF 18'),command=lambda: button_click(7))
button8 = Button(window,bg='grey',fg='white',text='8',font=('SF 18'),command=lambda: button_click(8))
button9 = Button(window,bg='grey',fg='white',text='9',font=('SF 18'),command=lambda: button_click(9))
button0 = Button(window,bg='grey',fg='white',text='0',font=('SF 18'),command=lambda: button_click(0))

button1.grid(row=2,column=1)
button2.grid(row=2,column=2)
button3.grid(row=2,column=3)
button4.grid(row=3,column=1)
button5.grid(row=3,column=2)
button6.grid(row=3,column=3)
button7.grid(row=4,column=1)
button8.grid(row=4,column=2)
button9.grid(row=4,column=3)
button0.grid(row=5,column=2)

#MATHEMATICAL OPERATIONS
buttonAdd = Button(window,bg='orange',fg='white',font=('SF 18'),text='+',command=lambda: button_click('+'))
buttonSub = Button(window,bg='orange',fg='white',font=('SF 18'),text='-',command=lambda: button_click('-'))
buttonMul = Button(window,bg='orange',fg='white',font=('SF 18'),text='×',command=lambda: button_click('×'))
buttonDiv = Button(window,bg='orange',fg='white',font=('SF 18'),text='÷',command=lambda: button_click('÷'))
buttonFact = Button(window,font=('SF 18'),text='x!',command=button_fact)
buttonRoot = Button(window,font=('SF 18'),text='√x',command=button_root)

buttonAdd.grid(row=1,column=4)
buttonSub.grid(row=2,column=4)
buttonMul.grid(row=3,column=4)
buttonDiv.grid(row=4,column=4)
buttonFact.grid(row=1,column=5)
buttonRoot.grid(row=2,column=5)

#OTHER STUFF CALCS HAVE LMAO
buttonDelete = Button(window,bg='lightgrey',font=('SF 18'),text='⌫',command=button_del)
buttonClear = Button(window,bg='lightgrey',font=('SF 18'),text='Clear',command=button_clear)
buttonDecimal = Button(window,bg='lightgrey',font=('SF 18'),text='.',command=lambda: button_click('.'))
buttonEqual = Button(window,bg='lightgrey',font=('SF 18'),text='=',command=button_equal)
buttonInvertSign = Button(window,bg='lightgrey',font=('SF 18'),text='-/+',command=button_pn)
buttonPi = Button(window,font='SF 18',text='π',command=button_pi)
buttonExp = Button(window,font=('SF 18'),text='aˣ',command=button_exp)

buttonDelete.grid(row=1,column=1)
buttonClear.grid(row=5,column=1)
buttonDecimal.grid(row=1,column=2)
buttonEqual.grid(row=5,column=4)
buttonInvertSign.grid(row=1,column=3)
buttonPi.grid(row=4,column=5)
buttonExp.grid(row=3,column=5)

mainloop()