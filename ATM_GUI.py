from tkinter import *

root = Tk()
root.geometry('315x315')
root.resizable(0, 0)
root.title('Bank System')
root.config(bg='lavender')
var = StringVar()
j = ("Hello,Sir \nWelcome To our Bank System :)")
var.set(j)
Label(root, textvariable=var, relief=GROOVE, font="arial 15 bold", bg="palevioletred1", fg='white').place(x=2, y=20)
Label(root, text="What Do You Want To Do?", relief=GROOVE, font="arial 12 bold", bg="white", fg='aquamarine2').place(
    x=15, y=100)


def ATM():
    atm = Toplevel()
    atm.geometry('500x500')
    atm.title('ATM_System')
    atm.config(bg='lavender')
    Label(atm, text='Welcome to our ATM System:)', relief=GROOVE, font="arial 20 bold", bg="palevioletred1",
          fg='white').pack()
    Label(atm, text="Enter your account num :)", relief=GROOVE, font="arial 12 ", fg='brown').place(x=10, y=60)
    num = IntVar()
    num.set(Entry(atm, relief=GROOVE, font="arial 12 ", bg="white", fg='aquamarine2').place(x=200, y=60))
    Label(atm, text="Enter your Password :)", relief=GROOVE, font="arial 12 ", fg='brown').place(x=10, y=100)
    pas = IntVar()
    pas.set(Entry(atm, relief=GROOVE, font="arial 12 ", bg="white", fg='aquamarine2').place(x=200, y=100))
    f = StringVar()

    def enter(n=num, p=pas):
        P = 2630
        AN = 4532986
        if (num == AN) and (pas == P):
            f.set('Correct account number and password')
            Label(atm, textvariable=f, relief=GROOVE, font="arial 12 ", fg='green', bg='white').place(x=63, y=180)
            # Lb = Listbox(atm)
            # Listbox.insert(1, 'Deposite')
            # Listbox.insert(2, 'Withdraw')
            # Listbox.insert(3, 'Check palance')
            # Listbox.place(x=230,y=140)
            # Button(atm,text="Withdraw", relief=GROOVE,font="arial 12 ",fg='brown',command=withdraw).place(x=10,y=100)
        else:
            f.set('Unvalid account number or password try again PLZ')

            def reset():
                pas.set("")
                num.set("")

            Button(atm, text=' Reset ', bg='palevioletred4', fg='aquamarine2', font='arial 10 bold',
                   command=reset).place(x=215, y=210)
        Label(atm, textvariable=f, relief=GROOVE, font="arial 12 ", fg='green', bg='white').place(x=63, y=180)

    Button(atm, text=' Enter ', bg='palevioletred4', fg='aquamarine2', font='arial 10 bold', command=enter).place(x=215,
                                                                                                                  y=140)

    def Exit():
        atm.destroy()

    Button(atm, text=' Back ', bg='white', fg='palevioletred1', font='arial 10 bold', command=Exit).place(x=440, y=460)


Button(root, text='ATM_System', bg='palevioletred4', fg='aquamarine2', font='arial 10 bold', command=ATM).place(x=50,
                                                                                                                y=150)


def feed_back():
    f = Toplevel()
    f.geometry('500x500')
    f.title('Feed back')
    f.config(bg='lavender')


Button(root, text='Feed Back', bg='palevioletred4', fg='aquamarine2', font='arial 10 bold', command=feed_back).place(
    x=50, y=250)


def create():
    c = Toplevel()
    c.geometry('400x300')
    c.title('Create an account')
    c.config(bg='lavender')
    a = IntVar()
    a.set(Entry(c, relief=GROOVE, font="arial 12 ", bg="white", fg='aquamarine2').place(x=170, y=20))
    Label(c, text=" ID ", relief=GROOVE, font="arial 12 ", fg='brown').place(x=10, y=20)
    Label(c, text=" Name ", relief=GROOVE, font="arial 12 ", fg='brown').place(x=10, y=60)
    b = StringVar()
    b.set(Entry(c, relief=GROOVE, font="arial 12 ", bg="white", fg='aquamarine2').place(x=170, y=60))
    d = IntVar()
    d.set(Entry(c, relief=GROOVE, font="arial 12 ", bg="white", fg='aquamarine2').place(x=170, y=100))
    Label(c, text=" password ", relief=GROOVE, font="arial 12 ", fg='brown').place(x=10, y=100)
    e = IntVar()
    e.set(Entry(c, relief=GROOVE, font="arial 12 ", bg="white", fg='aquamarine2').place(x=170, y=140))
    Label(c, text=" confirm password ", relief=GROOVE, font="arial 12 ", fg='brown').place(x=10, y=140)

    def done():
        Label(c, text="Your account number is 4532263", relief=GROOVE, font="arial 12 ", fg='brown').place(x=100, y=220)

    Button(c, text=' Supmit ', bg='white', fg='palevioletred1', font='arial 10 bold', command=done).place(x=180, y=180)

    def Exit():
        c.destroy()

    Button(c, text=' Back ', bg='white', fg='palevioletred1', font='arial 10 bold', command=Exit).place(x=340, y=260)


Button(root, text='Create an account', bg='palevioletred4', fg='aquamarine2', font='arial 10 bold',
       command=create).place(x=50, y=200)


def Exit():
    root.destroy()


Button(root, text='Exit', bg='white', fg='palevioletred1', font='arial 10 bold', command=Exit).place(x=270, y=278)
root.mainloop()