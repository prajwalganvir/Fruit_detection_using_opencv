
from PIL import ImageTk,Image
import tkinter

f=tkinter.Tk()
f.geometry("1250x700")
# f.configure(bg="#EBEBEB")


f.title("Fruit Detection and Identification")

l1=tkinter.Label(bg="khaki1",width=120,height=40)
l1.place(x=180,y=47)

img=Image.open("Detection.png")
rimg=img.resize((80,80),Image.ANTIALIAS)

pimg=ImageTk.PhotoImage(rimg)

l=tkinter.Label(image=pimg)
l.place(x=230,y=90)


h1=tkinter.Label(text="FRUIT DETECTION AND IDENTIFICATION",font=('cursive',25,'bold'),bg="darkolivegreen1",fg="red2")
h1.place(x=320,y=100,height=65)

b1=tkinter.Button(text="APPLE",font=('cursive',25,'bold'),bg="lightyellow1")
b1.place(x=300,y=230,width=140,height=80)

b2=tkinter.Button(text="MANGO",font=('cursive',25,'bold'),bg="lightyellow1")
b2.place(x=770,y=230,width=140,height=80)

b3=tkinter.Button(text="ORANGE",font=('cursive',25,'bold'),bg="lightyellow1")
b3.place(x=300,y=500,width=140,height=80)


# b3=tkinter.Button(text="ORANGE",font=('cursive',25,'bold'),bg="lightyellow1")
# b3.place(x=300,y=430,width=140,height=80)

# b4=tkinter.Button(text="BANANA",font=('cursive',25,'bold'),bg="lightyellow1")
# b4.place(x=770,y=430,width=140,height=80)

b4=tkinter.Button(text="BANANA",font=('cursive',25,'bold'),bg="lightyellow1")
b4.place(x=770,y=500,width=140,height=80)

b5=tkinter.Button(text="MIX",font=('cursive',25,'bold'),bg="lightyellow1")
b5.place(x=550,y=360,width=140,height=80)
# b5=tkinter.Button(text="MIX",font=('cursive',25,'bold'),bg="lightyellow1")
# b5.place(x=535,y=550,width=140,height=80)


# l=tkinter.Button(text="Logo")
# l.place(x=200,y=90)

f.mainloop()       