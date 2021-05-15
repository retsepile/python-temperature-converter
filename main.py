# importing the tkinter module

import tkinter

root = tkinter.Tk()   # creating a window
root.title("Temperature Converter")   # naming the recently created window
root.geometry("620x500")   #  setting the size of the window
root.config(bg="#dad1d3")   # setting the background color for the window

l1 = tkinter.LabelFrame(root, text="Celsius to Farenheit", padx=20, pady=20)
l1.grid(row=2, column=0)

e1 = tkinter.Entry(l1, state="disable")
e1. grid(row=4, column=0)

# setting the state for Celsius
def cel_active():
    e2.configure(state='disable')
    e1.configure(state="normal")


btn_active = tkinter.Button(root, text="Active -Celsius to Fahrenheit", command=cel_active)
btn_active.grid(row=6, column=0)

l2 = tkinter.LabelFrame(root, text="Fahrenheit to Celsius", padx=20, pady=20)
l2.grid(row=2, column=5)

e2 = tkinter.Entry(l2, state="disable")
e2.grid(row=4, column=5)


# setting the state for Fahrenheit
def far_active():
    e1.configure(state="disable")
    e2.configure(state="normal")


btn_active1 =tkinter.Button(root, text="Active -Fahrenheit to Celsius", command=far_active)
btn_active1.grid(row=6, column=5)


# defining function that will exit/ close the window/ program
def close():
    root.destroy()


exit_btn = tkinter.Button(text="Exit Program", command=close)
exit_btn.grid(row=9, column=6)


# defining function for converting celsius to fahrenheit
def convert_C():
    if e1["state"] == "normal" and e1.get() != "":
        celsius = float(e1.get())
        fahrenheit = (celsius*9/5)+32
        result_entry.insert(0, str(fahrenheit))


# defining function for converting fahrenheit to celsius
def convert_f():
    if e2["state"] == "normal" and e2.get() != "":
        fahrenheit = float(e2.get())
        celsius = (fahrenheit-32)*5/9
        result_entry.insert(0, celsius)


result_btn = tkinter.Button(root, text="Convert C-F", command=convert_C)
result_btn.grid(row=7, column=2)


# creating the action button for converting Fahrenheit to Celsius and calling the convert_f()
result_btn2 = tkinter.Button(root, text="Convert F-C", command=convert_f)
result_btn2.grid(row=7, column=4)


# creating the result_entry or output entry
result_entry = tkinter.Entry(root, bg="#f37683")
result_entry.grid(row=8, column=2)

# defining function that will delete the figure in the Entry box/ input box
def clear():
    e1.delete(0)
    e2.delete(0)
    result_entry.delete(0)


# creating the Clear button and calling the clear()
clear_btn = tkinter.Button(root, text="Clear", command=clear)
clear_btn.grid(row=8, column=6)

# starting the app
root.mainloop()