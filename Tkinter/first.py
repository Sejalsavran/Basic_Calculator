import tkinter as tk
#Creating root(window)
root=tk.Tk()
root.geometry("800x500")
#root name
root.title("My first GUI")

#creating lablein existinf root with providing text and font
label=tk.Label(root,text="Hello world!",fon=("Arial",18))
#to get label into root
label.pack(padx=20,pady=20)



#creating a textbox into root
textbox=tk.Text(root,height="3",font=("Arial",16))
textbox.pack()


#creating a entry box
entrybox=tk.Entry(root)
entrybox.pack(padx=0)

#creating buttons in button frame
buttonframe=tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

btn1=tk.Button(buttonframe,text="1",font=("Arial",18))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)

btn2=tk.Button(buttonframe,text="2",font=("Arial",18))
btn2.grid(row=0,column=1,sticky=tk.W+tk.E)

btn3=tk.Button(buttonframe,text="3",font=("Arial",18))
btn3.grid(row=0,column=2,sticky=tk.W+tk.E)

btn4=tk.Button(buttonframe,text="4",font=("Arial",18))
btn4.grid(row=1,column=0,sticky=tk.W+tk.E)

btn5=tk.Button(buttonframe,text="5",font=("Arial",18))
btn5.grid(row=1,column=1,sticky=tk.W+tk.E)

btn6=tk.Button(buttonframe,text="6",font=("Arial",18))
btn6.grid(row=1,column=2,sticky=tk.W+tk.E)

buttonframe.pack(fill="x")

##using place function
anotherbutton=tk.Button(root,text="TEST")
anotherbutton.place(x=200,y=200,height=100,width=100)

root.mainloop()
