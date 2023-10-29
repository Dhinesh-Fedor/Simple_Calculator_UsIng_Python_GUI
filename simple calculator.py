from tkinter import *
root = Tk()
root.title("Desktop Calculator")
root.geometry("330x377")
root.resizable(0,0)
root.iconbitmap(r"E:\tkinter\tkinter projects\icon for simple calculator\icons8-calculator-48.ico")

frame = Frame(root,height=400,width=325,highlightcolor="black",highlightbackground="black",highlightthickness=3)
frame.pack(expand=True)

b = StringVar()
a=""
def click(num):
    global a
    a = a + str(num)
    b.set(a)

def clear():
    global a
    a=""
    b.set(a)

def delete():
    global a
    a = a[:-1]
    b.set(a)

def result():
    global a
    try:
        a = str(eval(a))
        b.set(a)


    except:
        clear()
        b.set("ERROR")



c = Entry(frame,textvariable=b,font=("Calculator",36,"bold"),fg="brown",border=2,borderwidth=3,bg="#bccd95",width=10,justify=RIGHT)
c.grid(row=0,column=0,columnspan=4,padx=1,pady=1)
c.pack(ipadx=60,ipady=10)


frame2 = Frame(root,height=400,width=325,bg="grey",border=1,highlightcolor="black",highlightbackground="black",highlightthickness=4)
frame2.pack()

#1st row
b1 = (Button(frame2,text="7",height=3,width=10,bd=1,fg="white",bg="#50524c",command=lambda : click(7))).grid(row=0,column=0,padx=1,pady=1)
b2 = (Button(frame2,text="8",height=3,width=10,bd=1,fg="white",bg="#50524c",command=lambda : click(8))).grid(row=0,column=1,padx=1,pady=1)
b3 = (Button(frame2,text="9",height=3,width=10,bd=1,fg="white",bg="#50524c",command=lambda : click(9))).grid(row=0,column=2,padx=1,pady=1)
b4 = (Button(frame2,text="/",height=3,width=10,bd=1,fg="black",bg="#ECEAE2",command=lambda : click("/"))).grid(row=0,column=3,padx=1,pady=1)

#2nd row
b5 = (Button(frame2,text="4",height=3,width=10,bd=1,fg="white",bg="#50524c",command=lambda : click(4))).grid(row=1,column=0,padx=1,pady=1)
b6 = (Button(frame2,text="5",height=3,width=10,bd=1,fg="white",bg="#50524c",command=lambda : click(5))).grid(row=1,column=1,padx=1,pady=1)
b7 = (Button(frame2,text="6",height=3,width=10,bd=1,fg="white",bg="#50524c",command=lambda : click(6))).grid(row=1,column=2,padx=1,pady=1)
b8 = (Button(frame2,text="*",height=3,width=10,bd=1,fg="black",bg="#ECEAE2",command=lambda : click("*"))).grid(row=1,column=3,padx=1,pady=1)

#3rd row
b9 = (Button(frame2,text="1",height=3,width=10,bd=1,fg="white",bg="#50524c",command=lambda : click(1))).grid(row=2,column=0,padx=1,pady=1)
b10 = (Button(frame2,text="2",height=3,width=10,bd=1,fg="white",bg="#50524c",command=lambda : click(2))).grid(row=2,column=1,padx=1,pady=1)
b11 = (Button(frame2,text="3",height=3,width=10,bd=1,fg="white",bg="#50524c",command=lambda : click(3))).grid(row=2,column=2,padx=1,pady=1)
b12 = (Button(frame2,text="-",height=3,width=10,bd=1,fg="black",bg="#ECEAE2",command=lambda : click("-"))).grid(row=2,column=3,padx=1,pady=1)

#4th row
b13 = (Button(frame2,text="(",height=3,width=10,bd=1,fg="black",bg="#ECEAE2",command=lambda : click("("))).grid(row=3,column=0,padx=1,pady=1)
b14 = (Button(frame2,text="0",height=3,width=10,bd=1,fg="white",bg="#50524c",command=lambda : click(0))).grid(row=3,column=1,padx=1,pady=1)
b15 = (Button(frame2,text=")",height=3,width=10,bd=1,fg="black",bg="#ECEAE2",command=lambda : click(")"))).grid(row=3,column=2,padx=1,pady=1)
b16 = (Button(frame2,text="+",height=3,width=10,bd=1,fg="black",bg="#ECEAE2",command=lambda : click("+"))).grid(row=3,column=3,padx=1,pady=1)

#5th row
b17 = (Button(frame2,text=".",height=3,width=10,bd=1,fg="white",bg="#50524c",command=lambda : click("."))).grid(row=4,column=0,padx=1,pady=1)
b18 = (Button(frame2,text="Del",height=3,width=10,bd=1,fg="black",bg="#ECEAE2",command=delete)).grid(row=4,column=1,padx=1,pady=1)
b19 = (Button(frame2,text="Clear",height=3,width=10,bd=1,fg="black",bg="#ECEAE2",command=clear)).grid(row=4,column=2,padx=1,pady=1)
b20 = (Button(frame2,text="=",height=3,width=10,bd=1,fg="black",bg="#ECEAE2",command=result)).grid(row=4,column=3,padx=1,pady=1)





root.mainloop()