from math import cos, factorial, sin, sqrt, tan
from tkinter import DISABLED, END, NORMAL, Button, Entry, Label, Tk, mainloop
from tkmacosx import *

# var. func has 2 states: 0 -> No error in the calculator and -1 -> Error state
func = 0
# Used to prevent recursion loop in button_equal()
switch = True

# Creating the main display window and adding the output box and a memory to store an output.
window = Tk()
window.title('Calculator')
window.resizable(False,False) # .resizable(width{bool}, height{bool})

# Adds the output box, where the user can see what they've entered into the calculator.
Display = Entry(window, borderwidth=0, font='SF 22')
Display.grid(row=0, column=1, columnspan=3, sticky='EW')

# Used to store any output in button_mem()
Memory = Label(window, fg='lightgrey', bg='white', font='SF 22')


# Takes in any digit from 0 to 9 and a decimal point ('.').
def button_click(number):
    # When the calculator is started up, the default output shows '0'. As soon as the user will type any number that's
    # not a decimal point, that digit will replace the zero. It makes more sense for the user to see '9' instead of
    # '09'.
    if Display.get() == '0' and number != '.':
        Display.delete(0, END)
    # elif block will run ONLY on the specific case that the user pressed buttonInvertSign before entering any digit,
    # then clicking any digit.
    elif Display.get() == '-0':
        Display.delete(1, END)
    # if type(number) == str, it means the var. number is in [+, -, ÷, ×, .]. The != '.' leaves the possibilities of
    # var. number being [+, -, ÷, ×]
    if type(number) == str and number != '.':
        # Returns buttonDecimal to normal state since the user could add more than one decimal numbers at once. eg.
        # 8.9 + 3.4 × 4.2
        buttonDecimal.config(state=NORMAL)
        # I haven't found a fix to this issue where if the user clicks any math operation when the output is just
        # '0', it gives and IndexError because len(Display.get())-1 = 0. So the .delete() won't work with negative
        # indexes. If I find a fix ill add it later. Till the time I've made that situation into a separate case.
        try:
            # If the user clicked on '+' then changed their mind and clicked '-', instead of the output showing '+-'
            # and giving an error, it removes the '+' and replaces it with '-'.
            if Display.get()[len(Display.get()) - 1] in '+-/×':
                Display.delete(len(Display.get()) - 1, END)
            # The following indented code just inserts whatever operation was clicked and highlights the button that
            # was clicked, so it's easier for the user to know what operation they're doing.
            if number == '+':
                Display.insert(END, '+')
                buttonAdd.config(bg='white', fg='orange')
                buttonSub.config(bg='orange', fg='white')
                buttonMul.config(bg='orange', fg='white')
                buttonDiv.config(bg='orange', fg='white')
            elif number == '-':
                Display.insert(END, '-')
                buttonSub.config(bg='white', fg='orange')
                buttonAdd.config(bg='orange', fg='white')
                buttonMul.config(bg='orange', fg='white')
                buttonDiv.config(bg='orange', fg='white')
            elif number == '×':
                Display.insert(END, '×')
                buttonMul.config(bg='white', fg='orange')
                buttonAdd.config(bg='orange', fg='white')
                buttonSub.config(bg='orange', fg='white')
                buttonDiv.config(bg='orange', fg='white')
            elif number == '÷':
                Display.insert(END, '/')
                buttonDiv.config(bg='white', fg='orange')
                buttonAdd.config(bg='orange', fg='white')
                buttonSub.config(bg='orange', fg='white')
                buttonMul.config(bg='orange', fg='white')
        except IndexError:
            Display.insert(0, '0')
            if number == '+':
                Display.insert(END, '+')
                buttonAdd.config(bg='white', fg='orange')
                buttonSub.config(bg='orange', fg='white')
                buttonMul.config(bg='orange', fg='white')
                buttonDiv.config(bg='orange', fg='white')
            elif number == '-':
                Display.insert(END, '-')
                buttonSub.config(bg='white', fg='orange')
                buttonAdd.config(bg='orange', fg='white')
                buttonMul.config(bg='orange', fg='white')
                buttonDiv.config(bg='orange', fg='white')
            elif number == '×':
                Display.insert(END, '×')
                buttonMul.config(bg='white', fg='orange')
                buttonAdd.config(bg='orange', fg='white')
                buttonSub.config(bg='orange', fg='white')
                buttonDiv.config(bg='orange', fg='white')
            elif number == '÷':
                Display.insert(END, '/')
                buttonDiv.config(bg='white', fg='orange')
                buttonAdd.config(bg='orange', fg='white')
                buttonSub.config(bg='orange', fg='white')
                buttonMul.config(bg='orange', fg='white')
    elif number == '.':
        # Disables buttonDecimal because 8.90 is a number but 8.9.0 is not.
        buttonDecimal.config(state=DISABLED)
        Display.insert(END, number)
    elif number == 'π':
        Display.insert(END, '3.1415926535897932')
    else:
        Display.insert(END, number)

def button_fact():
    """p = 1
    ans = round(eval(Display.get().replace('×','*').replace('π','3.1415926535897932').replace('^','**')))
    for i in range(2,ans+1):
        p *= i
    Display.delete(0,END)
    Display.insert(0,p)"""
    p = factorial(round(eval(Display.get().replace('×', '*').replace('π', '3.1415926535897932').replace('^', '**'))))
    Display.delete(0, END)
    Display.insert(0, p)
    buttonAdd.config(bg='orange', fg='white')
    buttonSub.config(bg='orange', fg='white')
    buttonMul.config(bg='orange', fg='white')
    buttonDiv.config(bg='orange', fg='white')


def button_root():
    global func
    ans = eval(Display.get().replace('×', '*').replace('π', '3.1415926535897932').replace('^', '**'))
    try:
        ans = sqrt(ans)
        Display.delete(0, END)
        Display.insert(0, ans)
    # Square root of negative numbers has no real solution. So button_root() changes the var. func to -1 (error
    # state).
    except ValueError:
        func = -1
        button_equal()
    buttonAdd.config(bg='orange', fg='white')
    buttonSub.config(bg='orange', fg='white')
    buttonMul.config(bg='orange', fg='white')
    buttonDiv.config(bg='orange', fg='white')


def button_equal():
    global func, switch
    # Error state: disables all buttons and highlights buttonClear with a pink background. This prevents the user
    # from doing anything until they clear the error output.
    if func == -1:
        Display.delete(0, END)
        Display.insert(0, 'Error')
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
        buttonExp.config(state=DISABLED)
        buttonPi.config(state=DISABLED)
        buttonMem.config(state=DISABLED)
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
    # Switch is only there to prevent a recursion loop of button_equal(). It is used only for the except case.
    elif switch:
        # If there are no problems with the given input, it simply calculates it and shows the value in the output box.
        try:
            ans = eval(Display.get().replace('×', '*').replace('π', '3.1415926535897932').replace('^', '**'))
            Display.delete(0, END)
            Display.insert(0, ans)
        # If the user tried to divide by 0, or there is any SyntaxError, it will change var. func to -1 and makes the
        # program run button_equal() again, without the user clicking anything. Here, var. switch is flipped to
        # false, so the elif block runs only once and doesn't cause a recursion loop. It is reset to True after the
        # user receives the error message
        except (ZeroDivisionError, SyntaxError, NameError):
            switch = False
            func = -1
            button_equal()
            switch = True
    func = 0
    buttonAdd.config(bg='orange', fg='white')
    buttonSub.config(bg='orange', fg='white')
    buttonMul.config(bg='orange', fg='white')
    buttonDiv.config(bg='orange', fg='white')


def button_del():
    Display.delete(len(Display.get()) - 1, END)
    # If the user deletes an output like '-9', instead of just showing '-', which can be confusing to see,
    # it replaces '-9' with '0'.
    if len(Display.get()) == 0 or Display.get() == '-':
        Display.delete(0, END)
        Display.insert(0, '0')


# Resets everything to normal and clears the output box. Then adds '0' to the output box. (Reset to defaults)
def button_clear():
    Display.delete(0, END)
    Display.insert(0, '0')
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
    buttonExp.config(state=NORMAL)
    buttonPi.config(state=NORMAL)
    buttonMem.config(state=NORMAL)
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
    # Calculates the data in the output box, then inverts the sign on the output.
    p = str(eval(Display.get()))
    # Converts negative numbers to positive
    if p[0] == '-':
        Display.delete(0, END)
        Display.insert(0, '' + p[1:])
    # Converts positive numbers to negative
    else:
        Display.delete(0, END)
        Display.insert(0, '-' + p)
    buttonAdd.config(bg='orange', fg='white')
    buttonSub.config(bg='orange', fg='white')
    buttonMul.config(bg='orange', fg='white')
    buttonDiv.config(bg='orange', fg='white')


def button_mem():
    # Adds data to memory
    if buttonMem['text'] == 'M':
        Memory.grid(row=0, column=4, columnspan=2, sticky='EW')
        Memory.config(text=eval(Display.get()))
        buttonMem.config(text='M+')
    # Once the memory is called back in the output box, it clears the memory.
    else:
        button_click(Memory['text'])
        buttonMem.config(text='M')
        Memory.grid_forget()

def button_expand():
    if buttonExpand['text'] != 'x':    
        buttonPi.grid(row=5, column=5)
        buttonExp.grid(row=4, column=5)
        buttonRoot.grid(row=3, column=5)
        buttonFact.grid(row=2, column=5)
        buttonMem.grid(row=1, column=5)
        buttonSin.grid(row=1, column=6)
        buttonCos.grid(row=2, column=6)
        buttonTan.grid(row=3, column=6)
        buttonExpand.config(text='x')
    else:
        buttonPi.grid_forget()
        buttonExp.grid_forget()
        buttonRoot.grid_forget()
        buttonFact.grid_forget()
        buttonMem.grid_forget()
        buttonSin.grid_forget()
        buttonCos.grid_forget()
        buttonTan.grid_forget()
        buttonExpand.config(text='+')

def button_sin():
    inp = eval(Display.get())
    Display.delete(0,END)
    Display.insert(0,sin(inp))
def button_cos():
    inp = eval(Display.get())
    Display.delete(0,END)
    Display.insert(0,cos(inp))
def button_tan():
    inp = eval(Display.get())
    Display.delete(0,END)
    Display.insert(0,tan(inp))


# DIGITS 0 TO 9
button1 = Button(window, pady=5, bg='grey', fg='white', text='1', font='SF 18', command=lambda: button_click(1))
button2 = Button(window, pady=5, bg='grey', fg='white', text='2', font='SF 18', command=lambda: button_click(2))
button3 = Button(window, pady=5, bg='grey', fg='white', text='3', font='SF 18', command=lambda: button_click(3))
button4 = Button(window, pady=5, bg='grey', fg='white', text='4', font='SF 18', command=lambda: button_click(4))
button5 = Button(window, pady=5, bg='grey', fg='white', text='5', font='SF 18', command=lambda: button_click(5))
button6 = Button(window, pady=5, bg='grey', fg='white', text='6', font='SF 18', command=lambda: button_click(6))
button7 = Button(window, pady=5, bg='grey', fg='white', text='7', font='SF 18', command=lambda: button_click(7))
button8 = Button(window, pady=5, bg='grey', fg='white', text='8', font='SF 18', command=lambda: button_click(8))
button9 = Button(window, pady=5, bg='grey', fg='white', text='9', font='SF 18', command=lambda: button_click(9))
button0 = Button(window, pady=5, bg='grey', fg='white', text='0', font='SF 18', command=lambda: button_click(0))

button1.grid(row=2, column=1)
button2.grid(row=2, column=2)
button3.grid(row=2, column=3)
button4.grid(row=3, column=1)
button5.grid(row=3, column=2)
button6.grid(row=3, column=3)
button7.grid(row=4, column=1)
button8.grid(row=4, column=2)
button9.grid(row=4, column=3)
button0.grid(row=5, column=2)

# MATHEMATICAL OPERATIONS
buttonAdd = Button(window, pady=5, bg='orange', fg='white', font='SF 18', text='+', command=lambda: button_click('+'))
buttonSub = Button(window, pady=5, bg='orange', fg='white', font='SF 18', text='-', command=lambda: button_click('-'))
buttonMul = Button(window, pady=5, bg='orange', fg='white', font='SF 18', text='×', command=lambda: button_click('×'))
buttonDiv = Button(window, pady=5, bg='orange', fg='white', font='SF 18', text='÷', command=lambda: button_click('÷'))

buttonAdd.grid(row=1, column=4)
buttonSub.grid(row=2, column=4)
buttonMul.grid(row=3, column=4)
buttonDiv.grid(row=4, column=4)

# OTHER STUFF
buttonDelete = Button(window, pady=5, bg='lightgrey', font='SF 18', text='⌫', command=button_del)
buttonClear = Button(window, pady=5, bg='lightgrey', font='SF 18', text='Clear', command=button_clear)
buttonDecimal = Button(window, pady=5, bg='lightgrey', font='SF 18', text='.', command=lambda: button_click('.'))
buttonEqual = Button(window, pady=5, bg='lightgrey', font='SF 18', text='=', command=button_equal)
buttonInvertSign = Button(window, pady=5, bg='lightgrey', font='SF 18', text='+/-', command=button_pn)
buttonExpand = Button(window, pady=5, font='SF 18', text='+', bg='lightgrey', command=button_expand)

buttonDelete.grid(row=1, column=1)
buttonClear.grid(row=5, column=1)
buttonDecimal.grid(row=1, column=2)
buttonEqual.grid(row=5, column=4)
buttonInvertSign.grid(row=1, column=3)
buttonExpand.grid(row=5,column=3)

# HIDDEN BUTTONS
buttonPi = Button(window, pady=5, font='SF 18', text='π', command=lambda: button_click('π'))
buttonExp = Button(window, pady=5, font='SF 18', text='aˣ', command=lambda: Display.insert(END,'^'))
buttonMem = Button(window, pady=5, font='SF 18', text='M', command=button_mem)
buttonFact = Button(window, pady=5, font='SF 18', text='x!', command=button_fact)
buttonRoot = Button(window, pady=5, font='SF 18', text='√x', command=button_root)
buttonSin = Button(window, pady=5, font='SF 18', text='sin', command=button_sin)
buttonCos = Button(window, pady=5, font='SF 18', text='cos', command=button_cos)
buttonTan = Button(window, pady=5, font='SF 18', text='tan', command=button_tan)


Display.insert(0, '0')

mainloop()
