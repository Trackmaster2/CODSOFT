import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("to do list")

def add_task():TO DO LIST.py
    if task != '':
     listbox.insert(tkinter.END,task)
     entry.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="warning",message="YOU MUST ENTER A TASK!!")

def delete_task():
    try:
       task_index = listbox.curselection()[0]
       listbox.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="warning", message="YOU MUST SELECT A TASK!!")




frame = tkinter.Frame(root)
frame.pack()


listbox = tkinter.Listbox(frame, height=3, width=55)
listbox.pack(side=tkinter.LEFT)

scrollbar = tkinter.Scrollbar(frame)
scrollbar.pack(side=tkinter.RIGHT ,fill=tkinter.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview())


entry = tkinter.Entry(root,width=50)
entry.pack()


add_task_button = tkinter.Button(root,text="add task",width=30, command=add_task)
add_task_button.pack()

delete_task_button = tkinter.Button(root,text="delete task",width=30,command=delete_task)
delete_task_button.pack()



root.mainloop()

