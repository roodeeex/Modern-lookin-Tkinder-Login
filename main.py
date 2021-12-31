from tkinter import *
from tkinter.font import BOLD
from PIL import Image,ImageTk

root =Tk()

root.title('Login ')
root.iconbitmap('login.ico')
def hello():
    try :
        if not e1.get() and not e2.get() :
            button1 = Button(root , image = firstname , bg='#1b1b1b', bd=0,relief =SUNKEN , activebackground="#1b1b1b", command = entry )
            button1.place(x=55 , y=141 , anchor=NW)
            button2 = Button(root , image = lastname , bg='#1b1b1b', bd=0,relief =SUNKEN ,cursor='xterm', activebackground="#1b1b1b", command = entry2 )
            button2.place(x=55 , y=226 , anchor=NW) 
        else :
            if not e1.get():
                button1 = Button(root , image = firstname , bg='#1b1b1b', bd=0,relief =SUNKEN , activebackground="#1b1b1b", command = entry )
                button1.place(x=55 , y=141 , anchor=NW)
            if not e2.get():
                button2 = Button(root , image = lastname , bg='#1b1b1b', bd=0,relief =SUNKEN ,cursor='xterm', activebackground="#1b1b1b", command = entry2 )
                button2.place(x=55 , y=226 , anchor=NW) 
    except :
        button1 = Button(root , image = firstname , bg='#1b1b1b', bd=0,relief =SUNKEN , activebackground="#1b1b1b", command = entry )
        button1.place(x=55 , y=141 , anchor=NW)
        button2 = Button(root , image = lastname , bg='#1b1b1b', bd=0,relief =SUNKEN ,cursor='xterm', activebackground="#1b1b1b", command = entry2 )
        button2.place(x=55 , y=226 , anchor=NW) 

canva = Canvas(root , bg='#1b1b1b', height=500 , width=400)
canva.pack(fill=BOTH , expand=True)

mainb = Button(root , bd=0,bg='#1b1b1b', height=500 , width=400 ,relief  =SUNKEN , activebackground="#1b1b1b",command= hello)
mainb.place(x=0 , y=0)

img= (Image.open("button2.png"))
resized_image1= img.resize((200,200), Image.ANTIALIAS)
root.inactive = ImageTk.PhotoImage(resized_image1)

img2= (Image.open("button1.png"))
resized_image= img2.resize((200,200), Image.ANTIALIAS)
root.active=  ImageTk.PhotoImage(resized_image)

texttrue = Label(root, text='Login succefully' , font=('ariel' , 12 , BOLD) ,bg="#1b1b1b" , bd=0 , fg = '#248503', width=100)
textfuser = Label(root, text='Incorret Username' , font=('ariel' , 12, BOLD) ,bg="#1b1b1b" , bd=0 , fg = '#a91616')
textfpsw = Label(root, text='Incorrect Password ' , font=('ariel' , 12, BOLD) ,bg="#1b1b1b" , bd=0 , fg = '#a91616')
textfboth = Label(root, text='Incorrect Username and Password' , font=('ariel' , 12 , BOLD) ,bg="#1b1b1b" , bd=5 , fg = '#a91616')

def on_enter(event):
    button.config(image=root.active)
def on_leave(enter):
    button.config(image=root.inactive)

def infos():
    print('USERNAME  : ' , e1.get())
    print('PASSWORD  : ' ,  e2.get())
    texttrue.place_forget()
    textfuser.place_forget()
    textfboth.place_forget()
    textfpsw.place_forget()
    if e1.get() == 'admin' and e2.get() == 'admin':
        texttrue.place(x=207 , y=450 , anchor=CENTER)
    else :
        if e1.get() != 'admin' and e2.get() != 'admin':
            textfboth.place(x=207 , y=450 , anchor=CENTER)
        else:
            if e1.get() != 'admin' :
                textfuser.place(x=207 , y=450 , anchor=CENTER)
            else:
                textfpsw.place(x=207 , y=450 , anchor=CENTER)

button = Button(root , image=root.inactive , bg='#1b1b1b' , width= 131 , height= 55  , bd=0,relief  =RIDGE , activebackground="#1b1b1b", command=infos)
button.bind('<Enter>' , on_enter)
button.bind('<Leave>' , on_leave)
button.place(x=123 , y=351)

firstname = PhotoImage(file="firstname.png")
def entry():
    global e1
    e1 = Entry(root , bg="#bdc3e6" , bd=0, font = ('American Captain' , 16 ))
    e1.place( x=88 , y=144 , width= 225 , height= 64)
    e1.focus_force() 

button1 = Button(root , image = firstname , bg='#1b1b1b', bd=0,relief =SUNKEN ,cursor='xterm', activebackground="#1b1b1b", command = entry )
button1.place(x=55 , y=141 , anchor=NW)

lastname = PhotoImage(file="lastname.png")  
def entry2():
    global e2
    e2 = Entry(root , bg="#bdc3e6" , bd=0, font = ('American Captain' , 16 ) , show= '•')
    e2.place( x=88 , y=229, anchor=NW,width= 220 , height= 64)
    e2.focus_force() 

button2 = Button(root , image = lastname , bg='#1b1b1b', bd=0,relief =SUNKEN ,cursor='xterm', activebackground="#1b1b1b", command = entry2 )
button2.place(x=55 , y=226 , anchor=NW)

label= Label(root, text='LOGIN' , font=('American Captain' , 50  ) ,bg="#1b1b1b" , bd=0 , fg = '#5b27c5')
label.place(x=143 , y=32 , anchor=NW)

root.mainloop()
