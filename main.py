from tkinter import *

import tk as tk

def ButtonClick(Numbers):
    global operator
    operator = operator + str(Numbers)
    text_Input.set(operator)
def ButtonClear():
    global operator
    operator = ""
    text_Input.set("")
def Equality():
    global operator
    equal = str(eval(operator))
    text_Input.set(equal)
    operator = ""



calc = Tk()
calc.title("calculator")
operator=""
text_Input = StringVar()
txtDisplay = Entry(calc, font=("arial", 20, "bold"), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="cyan", justify="right").grid(columnspan=4)
#row 1
btn7 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="7",command=lambda:ButtonClick(7), bg="cyan").grid(row=1, column=0)
btn8 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="8",command=lambda:ButtonClick(8), bg="cyan" ).grid(row=1, column=1)
btn9 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="9",command=lambda:ButtonClick(9), bg="cyan", ).grid(row=1, column=2)
Addition = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="+",command=lambda:ButtonClick("+"),  bg="cyan").grid(row=1, column=3)
#row 2
btn4 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="4",command=lambda:ButtonClick(4),  bg="cyan").grid(row=2, column=0)
btn5 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="5",command=lambda:ButtonClick(5), bg="cyan" ).grid(row=2, column=1)
btn6 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="6",command=lambda:ButtonClick(6), bg="cyan", ).grid(row=2, column=2)
soustract = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="-",command=lambda:ButtonClick("-"),  bg="cyan").grid(row=2, column=3)

#row 3
btn1 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="1",command=lambda:ButtonClick(1),  bg="cyan").grid(row=3, column=0)
btn2 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="2",command=lambda:ButtonClick(2), bg="cyan" ).grid(row=3, column=1)
btn3 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="3",command=lambda:ButtonClick(3), bg="cyan", ).grid(row=3, column=2)
Multiply = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="*",command=lambda:ButtonClick("*"),  bg="cyan").grid(row=3, column=3)
#row 4
btn0 = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="0",command=lambda:ButtonClick(0),  bg="cyan").grid(row=4, column=0)
btnAC = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="AC",command=lambda:ButtonClear(), bg="cyan" ).grid(row=4, column=1)
btnequal = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="=",command=lambda:Equality(), bg="cyan", ).grid(row=4, column=2)
Divide = Button(calc, padx=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="/",command=lambda:ButtonClick("/"),  bg="cyan").grid(row=4, column=3)





calc.mainloop()


