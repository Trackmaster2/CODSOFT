import tkinter
from tkinter import *

calculation = ""

def add_to_cal(symbol):
    global calculation
    calculation += str(symbol)
    entry.delete(0,"end")
    entry.insert(0,calculation)
def eval_cal():
    global calculation
    try:
        result= str(eval(calculation))
        calculation = ""
        entry.delete(0,"end")
        entry.insert(0,result)
    except:
        clear()
        entry.insert(0,"error")
def clear():
    global calculation
    calculation = ""
    entry.delete(0, "end")


root = Tk()
root.title("Arithematic Calculator")
root.geometry("500x400")
root.configure(bg="#17161b")


entry = tkinter.Entry(root,width=50)
entry.grid(columnspan=5)
entry.pack(pady=15,padx=15)
frame1 = Frame(root,bg="black")
button1 = Button(frame1,text = "9",width=5,height=2,command=lambda :add_to_cal(9))
button1.pack(side=LEFT,padx=7,pady=10)

button1 = Button(frame1,text = "8",width=5,height=2,command=lambda :add_to_cal(8))
button1.pack(side=LEFT,padx=7,pady=10)

button1 = Button(frame1,text = "7",width=5,height=2,command=lambda :add_to_cal(7))
button1.pack(side=LEFT,padx=7,pady=10)

button1 = Button(frame1,text = "+",width=5,height=2,command=lambda :add_to_cal("+"))
button1.pack(side=LEFT,padx=7,pady=10)

frame1.pack()

frame2 = Frame(root,bg="black")
button1 = Button(frame2,text = "6",width=5,height=2,command=lambda :add_to_cal(6))
button1.pack(side=LEFT,padx=7,pady=10)

button1 = Button(frame2,text = "5",width=5,height=2,command=lambda :add_to_cal(5))
button1.pack(side=LEFT,padx=7,pady=10)

button1 = Button(frame2,text = "4",width=5,height=2,command=lambda :add_to_cal(4))
button1.pack(side=LEFT,padx=7,pady=10)
button1 = Button(frame2,text = "_",width=5,height=2,command=lambda :add_to_cal("-"))
button1.pack(side=LEFT,padx=7,pady=10)


frame2.pack()
frame3 = Frame(root,bg="black")
button1 = Button(frame3,text = "3",width=5,height=2,command=lambda :add_to_cal(3))
button1.pack(side=LEFT,padx=7,pady=10)

button1 = Button(frame3,text = "2",width=5,height=2,command=lambda :add_to_cal(2))
button1.pack(side=LEFT,padx=7,pady=10)

button1 = Button(frame3,text = "1",width=5,height=2,command=lambda :add_to_cal(1))
button1.pack(side=LEFT,padx=7,pady=10)
button1 = Button(frame3,text = "*",width=5,height=2,command=lambda :add_to_cal("*"))
button1.pack(side=LEFT,padx=7,pady=10)

frame3.pack()

frame4 = Frame(root,bg="black")
button1 = Button(frame4,text = "(",width=5,height=2,command=lambda :add_to_cal("("))
button1.pack(side=LEFT, padx=7,pady=10)

button1 = Button(frame4,text = "0",width=5,height=2,command=lambda :add_to_cal(0))
button1.pack(side=LEFT, padx=7,pady=10)

button1 = Button(frame4,text = ")",width=5,height=2,command=lambda :add_to_cal(")"))
button1.pack(side=LEFT, padx=7,pady=10)

button1 = Button(frame4,text = "/",width=5,height=2,command=lambda :add_to_cal("/"))
button1.pack(side=LEFT, padx=7,pady=10)
frame4.pack()

frame5 = Frame(root,bg="black")
button1 = Button(frame5,text = "=",width=10,height=2,command=eval_cal,bg="orange")
button1.pack(side=LEFT, padx=7,pady=10)

button1 = Button(frame5,text = "C",width=10,height=2,command=clear,bg="#3697f5")
button1.pack(side=LEFT, padx=7,pady=10)


frame5.pack()




root.mainloop()
