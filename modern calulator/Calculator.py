from customtkinter import *
from PIL import ImageTk, Image
import pygame

pygame.mixer.init()
app= CTk()
app.title("Calculator")
app.geometry("400x700")
app.resizable(False,False)
sound_play = pygame.mixer.Sound("pop4.mp3")
image_logo = ImageTk.PhotoImage(Image.open(r"C:\Users\HP\OneDrive\Desktop\PythonProject\logocalc.png"))
app.iconphoto(False, image_logo)
entry= CTkEntry(app, placeholder_text='0',font=('Cascadia Code',50),width=400, height=100,justify='right')
def clicks(value):
    sound_play.play()
    if entry.get() == 'ERROR!':
        entry.delete(0, END)
        entry.insert(END, value)
    else:
        entry.insert(END, value)
def backspace():
    sound_play.play()
    if entry.get() == 'ERROR!':
        entry.delete(0, END)
    entry.delete(len(entry.get()) - 1)
def equal():
    sound_play.play()
    if entry.get() == 'ERROR!':
        entry.delete(0, END)
    try:
        res = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0,res)
    except ZeroDivisionError:
        entry.delete(0, END)
        entry.insert(0,'ERROR!')
    except SyntaxError:
        entry.delete(0, END)
        entry.insert(0, 'ERROR!')
def clear():
    sound_play.play()
    entry.delete(0,END)

#All Buttons Here
b1= CTkButton(app, text='1',font=('Cascadia Code',50),hover_color='#135385',width=100, height=100,cursor='hand2',command=lambda:clicks('1'))
b2= CTkButton(app, text='2',font=('Cascadia Code',50),hover_color='#135385',width=100, height=100,cursor='hand2',command=lambda:clicks('2'))
b3= CTkButton(app, text='3',font=('Cascadia Code',50),hover_color='#135385',width=100, height=100,cursor='hand2',command=lambda:clicks('3'))
b4= CTkButton(app, text='4',font=('Cascadia Code',50),hover_color='#135385',width=100, height=100,cursor='hand2',command=lambda:clicks('4'))
b5= CTkButton(app, text='5',font=('Cascadia Code',50),hover_color='#135385',width=100, height=100,cursor='hand2',command=lambda:clicks('5'))
b6= CTkButton(app, text='6',font=('Cascadia Code',50),hover_color='#135385',width=100, height=100,cursor='hand2',command=lambda:clicks('6'))
b7= CTkButton(app, text='7',font=('Cascadia Code',50),hover_color='#135385',width=100, height=100,cursor='hand2',command=lambda:clicks('7'))
b8= CTkButton(app, text='8',font=('Cascadia Code',50),hover_color='#135385',width=100, height=100,cursor='hand2',command=lambda:clicks('8'))
b9= CTkButton(app, text='9',font=('Cascadia Code',50),hover_color='#135385',width=100, height=100,cursor='hand2',command=lambda:clicks('9'))
b0= CTkButton(app, text='0',font=('Cascadia Code',50),hover_color='#135385',width=100, height=100,cursor='hand2',command=lambda:clicks('0'))
b_br1= CTkButton(app, text='(',font=('Cascadia Code',50),width=50, height=100,cursor='hand2',command=lambda:clicks('('))
b_br2= CTkButton(app, text=')',font=('Cascadia Code',50),width=52, height=100,cursor='hand2',command=lambda:clicks(')'))
b_add= CTkButton(app, text='+',font=('Cascadia Code',50),hover_color='#5c5b5a',fg_color='gray',
                 width=100, height=100,cursor='hand2',command=lambda:clicks('+'))
b_sub= CTkButton(app, text='-',font=('Cascadia Code',50),hover_color='#5c5b5a',fg_color='gray',width=100,
                 height=100,cursor='hand2',command=lambda:clicks('-'))
b_multi= CTkButton(app, text='x',font=('Cascadia Code',50),hover_color='#5c5b5a',fg_color='gray',width=100,
                   height=100,cursor='hand2',command=lambda:clicks('*'))
b_div= CTkButton(app, text='÷',font=('Cascadia Code',50),hover_color='#5c5b5a',fg_color='gray',width=100,
                 height=100,cursor='hand2',command=lambda:clicks('/'))
b_point= CTkButton(app, text='.',font=('Cascadia Code',50),width=100,
                   height=100,cursor='hand2',command=lambda:clicks('.'))
b_equal= CTkButton(app, text='=',font=('Cascadia Code',50),hover_color='#6f7d1e',fg_color='#96ab1f',width=100,
                   height=100,cursor='hand2',command=equal)
b_backspace= CTkButton(app, text='⌫',font=('Cascadia Code',50),hover_color='#9c2917',fg_color='red',width=100,
                       height=100,cursor='hand2',command=backspace)
b_clear= CTkButton(app, text='C',font=('Cascadia Code',50),hover_color='#9c2917',fg_color='red',width=100,
                   height=100,cursor='hand2',command=clear)
b_modulo= CTkButton(app, text='%',font=('Cascadia Code',50),hover_color='#5c5b5a',fg_color='gray',width=100,
                    height=100,cursor='hand2',command=lambda:clicks('%'))
#buttons places
b1.place(x=0,y=300)
b2.place(x=100,y=300)
b3.place(x=200,y=300)
b4.place(x=0,y=400)
b5.place(x=100,y=400)
b6.place(x=200,y=400)
b7.place(x=0,y=500)
b8.place(x=100,y=500)
b9.place(x=200,y=500)
b0.place(x=100,y=600)
b_br1.place(x=0,y=600)
b_br2.place(x=49,y=600)
b_add.place(x=300,y=300)
b_sub.place(x=300,y=400)
b_multi.place(x=300,y=500)
b_div.place(x=100,y=200)
b_point.place(x=200,y=600)
b_equal.place(x=300,y=600)
b_backspace.place(x=300,y=200)
b_clear.place(x=200,y=200)
b_modulo.place(x=0,y=200)
entry.place(x=0,y=100)
#mainloop that run the code in loop without using loops
app.mainloop()