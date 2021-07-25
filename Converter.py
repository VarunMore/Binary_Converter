from tkinter import *
from pythonds.basic.stack import Stack


root =Tk()


photo = PhotoImage(file = "src/icon.png")
root.iconphoto(False, photo)


root.title("Binary Converter")
input_data = Entry(root, width=55, borderwidth=5)
input_data.grid(row=0, column=0, columnspan=3, padx=40, pady=40)
def clear():
    input_data.delete(0, END)



def convert_binary():
    number = input_data.get()
    global decNumber 
    decNumber = int(number)
    input_data.delete(0, END)
   
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
         binString = binString + str(remstack.pop())
    input_data.insert(0, binString)
    # input_data.insert(0, bin(decNumber).replace("0b", ""))   // Using bin() Function



def convert_decimal():
    number = input_data.get()
    global binNumber
    binNumber = number
    input_data.delete(0, END)
    try:
        input_data.insert(0, int(binNumber, 2))
    except ValueError:
        input_data.insert(0, "Error :  Enter Binary Number to convert to decimal")

    

button_1 = Button(text = "Convert into Binary", padx=25, pady=25, command=lambda: convert_binary())
button_1.grid(row=1, column=0)
button_2 = Button(text = "Convert into Decimal", padx=25, pady=25, command=lambda: convert_decimal())
button_2.grid(row=1, column=1)
button_3 = Button(text = "CLear", padx=25, pady=25, command=clear)
button_3.grid(row=1, column=2)


root.mainloop()
