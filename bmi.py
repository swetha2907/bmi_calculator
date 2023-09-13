from tkinter import *
window = Tk()
window.title("BMI CALCULATOR APP")
window.geometry("1000x1000")
l1 = Label(window, text = "Welcome to BMI calculator",font = ("bolditalic",50),bg
= "yellow",fg = "Blue")
l1.grid(column=15,row=10)
l2 = Label(window, text = "Check your BMI here",font = ("bold",25),fg = "brown")
l2.grid(column = 15, row = 30)
l3 = Label(window, text = "Enter your height(in m)",font = ("bolditalic",15))
l3.place(relx = 0.2,rely = 0.4)
l4 = Label(window, text = "Enter your weight(in Kg)",font = ("bolditalic",15))
l4.place(relx = 0.2,rely = 0.5)
def gh():
 h = float(E1.get())
 return h
def gw():
 w = float(E2.get())
 return w
E1 = Entry(window,width = 10)
E1.place(relx = 0.5, rely = 0.4, anchor = "center")
E2 = Entry(window,width = 10)
E2.place(relx = 0.5, rely = 0.5,anchor = "center")
def cbmi():
 h = gh()
 w = gw()
 bmi = w/(h**2)
 l7 = Label(window,text = bmi)
 l7.place(relx = 0.5,rely = 0.9)
b = Button(window,text = "TAP HERE",font = ("italic",25),bg = "red",command =
cbmi)
b.place(relx = 0.4 ,rely = 0.6)
l5 = Label(window,text = "Note:Tap here to know your BMI",font =
("bolditalic",15),bg = "green")
l5.place(relx = 0.5,rely = 0.8,anchor = "center")
l6 = Label(window,text = "Your BMI:",font = ("bolditalic",25),bg = "Purple")
l6.place(relx = 0.3, rely = 0.9)
window.mainloop()
