from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("welcome to great learnig")
window.minsize(width=450, height= 400)
window.maxsize(width = 800, height = 800)
#-------------------
s1 = StringVar()
def edtech():
   if(s1.get()==""):
     messagebox.showwarning("it's empty")
   else:
     messagebox.showinfo("succesful ",s1.get())

e1  = Entry(window,textvariable=s1)
e1.pack()
b1 = Button(window,text="Enter",command=edtech)
b1.pack()
#-------------------
'''
v = IntVar()
def edTech():
    print((v.get()))
r1 = Radiobutton(window,text="yes",value=1,variable=v)
r1.pack()
r2 = Radiobutton(window,text="no ", value=0,variable=v)
r2.pack()
b1 = Button(window,text="Enter",command=edTech)
b1.pack()
'''
#-------------------
'''
lb1 = Listbox(window,width=10)                          //listbox widget
list1 = ["aaa","bbb","ccc","dddd"]
for i in list1:
    lb1.insert(END,i)
lb1.pack()
def edTech():
    lb1.delete(ANCHOR)
b1 = Button(window,text="Remove",command= edTech)
b1.pack()
'''
#-------------------
'''
top = Frame()                                           //frame widg
top.pack()
bottom =Frame()
bottom.pack(side = BOTTOM)

l1 = Label(top, text = "top frame", bg="light blue")
l1.pack()
l2 = Label(bottom, text = "bottom frame", bg="pink")
l2.pack()
'''
#-------------------
'''
cb1 = Checkbutton(window,text= "happy")
cb1.pack()
'''
#-------------------
'''
l1 = Label(window,text = "enter your name", bg= "pink", fg= "red",bd = 4)
l1.place(x= 10,y = 20)
l2 = Label(window,text = "________________", bg= "light green", fg= "green",bd = 4)
l2.place(x= 300,y = 20)
v = StringVar()
e1 = Entry(window,font=("Corbel",18), width = 10, bd = 3,textvariable=v) //entry
e1.place(x= 150, y = 20)
def edTech():                                                       //function
    x = v.get()
    print(x)
    l2.config(text = x,bg = "yellow" )
b1 = Button(window,text="Enter",highlightbackground = "sky blue", fg = "blue",command= edTech) //button
b1.place(x= 200, y= 60)
'''
#-------------------
#e1 = Entry(window,width = 20,bd = 6,font = ("calibri",20))         // entry widget
#e1.pack()
#------------------
#b1 = Button(window,text="Enter", fg ="red",bg = "black")          //   button widget
#b1.pack()
#-------------------
#i1=PhotoImage(file = "photo2.png")                                // photo
#il1 = Label(window,image = i1,width=400,height=380)
#il1.pack()
#-------------------
#l1 = Label(window,text = "hi shivani",bg = "yellow",fg = "red")    //simple text
#l1.place(x= 150, y= 80)
#l1.pack()
#-------------------

window.mainloop()
