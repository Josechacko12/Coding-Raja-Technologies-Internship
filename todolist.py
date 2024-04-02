from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('ToDo List')
        self.root.geometry('650x410+300+150')

        self.label=Label(self.root,text='ToDo List',font='ariel,30', width=10,bd=5,bg='black',fg='white')
        self.label.pack(side='top',fill=BOTH)

        self.label2=Label(self.root,text='Add Task',font='ariel', width=10,bd=5,bg='black',fg='white')
        self.label2.place(x=40,y=54)

        self.label3=Label(self.root,text='Tasks',font='ariel', width=10,bd=5,bg='black',fg='white')
        self.label3.place(x=320,y=54)

        self.main_text= Listbox(self.root, height=12,bd=5,width=32,font="ariel,20")
        self.main_text.place(x=280,y=100)

        self.text=Text(self.root,bd=5,height=2,width=20,font='ariel')
        self.text.place(x=20,y=120)

          ################################ ADDTASK ####################################

        def add():
            content=self.text.get(1.0,END)
            self.main_text.insert(END,content)
            with open('data.txt','a') as file:
                file.write(content)
                file.seek(0)
                file.close()
                self.text.delete(1.0,END)

        
        def delete():
            delete_ = self.main_text.curselection()
            look=self.main_text.get(delete_)
            with open('data.txt','r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item=str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)
        with open('data.txt','r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END,ready)
            file.close()

            self.button= Button(self.root,text='Add',font='sarif',width=10,bd=5,bg='black',fg='white',command=add)
            self.button.place(x=30,y=180)

            self.button2= Button(self.root,text='Delete',font='sarif',width=10,bd=5,bg='black',fg='white',command=delete)
            self.button2.place(x=30,y=280)


        

def main():
    root=Tk()
    ui=todo(root)
    root.mainloop()

if __name__ == "__main__":
     main()
