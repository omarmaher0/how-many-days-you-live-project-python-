from tkinter import Tk,Entry,Button,IntVar,messagebox
root = Tk()
root.title('Calculator')
root.geometry('300x380')
var=IntVar()
def n0():
    print(0)
def n1():
    print(1)
def n2():
    print(2)
def n3():
    print(3)
def n4():
    print(4)
def n5():
    print(5)
def n6():
    print(6)
def n7():
    print(7)
def n8():
    print(8)
def n9():
    print(9)
def mul(num1,num2):
    var=num1 * num2
    print(messagebox.showinfo(),'Calculator',var)
b1=Button(root,text='0',width=7,height=3,bd=3,command=n0).place(x=10,y=260)
b2=Button(root,text='.',width=7,height=3,bd=3).place(x=80,y=260)
b3=Button(root,text='+',width=7,height=3,bd=3).place(x=150,y=260)
b4=Button(root,text='=',width=7,height=3,bd=3).place(x=220,y=260)
b5=Button(root,text='1',width=7,height=3,bd=3,command=n1).place(x=10,y=190)
b6=Button(root,text='2',width=7,height=3,bd=3,command=n2).place(x=80,y=190)
b7=Button(root,text='3',width=7,height=3,bd=3,command=n3).place(x=150,y=190)
b8=Button(root,text='-',width=7,height=3,bd=3).place(x=220,y=190)
b9=Button(root,text='4',width=7,height=3,bd=3,command=n4).place(x=10,y=120)
b10=Button(root,text='5',width=7,height=3,bd=3,command=n5).place(x=80,y=120)
b11=Button(root,text='6',width=7,height=3,bd=3,command=n6).place(x=150,y=120)
b12=Button(root,text='x',width=7,height=3,bd=3,command=mul).place(x=220,y=120)
b90=Button(root,text='7',width=7,height=3,bd=3,command=n7).place(x=10,y=50)
b01=Button(root,text='8',width=7,height=3,bd=3,command=n8).place(x=80,y=50)
b110=Button(root,text='9',width=7,height=3,bd=3,command=n9).place(x=150,y=50)
b1110=Button(root,text='/',width=7,height=3,bd=3).place(x=220,y=50)
entry = Entry(root,textvariable=var,font=("default", 20 or 10)).place(x=10,y=5)




root.mainloop()