import tkinter as tk
  
frame = tk.Tk()
frame.title("chat")
  
def printInput():
    inp = textBox.get(1.0, "end-1c")
    label.config(text = inp)

label = tk.Label(frame, text = "",height = 25,width = 50,anchor='nw')
label.pack()
textBox = tk.Text(frame,height = 1,width = 50)
textBox.configure(background='light grey')
textBox.pack()
Button = tk.Button(frame,text = "Print", command = printInput)
Button.pack()

frame.mainloop()
