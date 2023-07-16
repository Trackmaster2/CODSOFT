import tkinter
from tkinter import*
from random import randint

root = Tk()
root.title("Password Generator")
root.geometry("500x400")


def new_rand():
    pass_entry.delete(0,END)
    pass_len = int(entry2.get())
    password = ''
    for x in range(pass_len):
        password += chr(randint(33, 126))
    pass_entry.insert(0,password)


frame1 = tkinter.Frame(root,width=50)
entry1 = tkinter.Entry(frame1,width=30)
entry1.pack(side = RIGHT,pady=30,padx=20)
label = tkinter.Label(frame1,text="Enter User Name:")
label.pack(side = RIGHT)
frame1.pack()

frame2 = tkinter.Frame(root,width=50)
entry2 = tkinter.Entry(frame2,width=30)
entry2.pack(side = RIGHT,pady=30,padx=20)
label = tkinter.Label(frame2,text="Enter Password Length:")
label.pack(side = RIGHT)
frame2.pack()

frame3 = tkinter.Frame(root,width=50)
pass_entry = tkinter.Entry(frame3,width=30)
pass_entry.pack(side=RIGHT,pady=30,padx=20)
label = tkinter.Label(frame3,text="Generated Password:")
label.pack(pady=30,padx=20)
frame3.pack()

button1 = tkinter.Button(root,text="Generate Password",command=new_rand)
button1.pack()










root.mainloop()