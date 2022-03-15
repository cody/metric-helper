#metric helper app

#import the GUI framwork
from dataclasses import field
import tkinter as tk
from tkinter import ttk, END
from tkinter import font


#define root window
root = tk.Tk()
root.title("Metric Helper")
root.iconbitmap("/Users/cody/Documents/guis/metric-helper/ruler-16.gif")
root.resizable(0,0)

#define fonts and colors
fieldfont = ("Cambria", 10)
bgcolor = "#c75c5c"
buttoncolor = "#f5cf87"
root.config(bg=bgcolor)


#define functions
def convert():
    '''convert from metric prefix to another'''
    metricvalues = {
        "femto":10**-15,
        "pico":10**-12,
        "nano":10**-9,
        "micro":10**-6,
        "milli":10**-3,
        "centi":10**-2,
        "deci":10**-1,
        "base value":10**0,
        "deca":10**1,
        "hecto":10**2,
        "kilo":10**3,
        "mega":10**6,
        "giga":10**9,
        "tera":10**12,
        "peta":10**15
    }

    #clear the output field
    outputfield.delete(0, END)



    #get all user info
    startvalue = float(inputfield.get())
    startprefix = inputcombobox.get()
    endprefix = outputcombobox.get()

    #convert to the base unit first
    basevalue = startvalue*metricvalues[startprefix]
    #convert to new metric value
    endvalue = basevalue/metricvalues[endprefix]

    #update output field with answer
    outputfield.insert(0, str(endvalue))


#define the GUI layout
#create input and output entry fields
inputfield = tk.Entry(root, width=20, font=fieldfont, borderwidth=3)
outputfield = tk.Entry(root, width=20, font=fieldfont, borderwidth=3)
equallabel = tk.Label(root, text="=", font=fieldfont, bg=bgcolor)

inputfield.grid(row=0, column=0, padx=10, pady=10)
equallabel.grid(row=0, column=1, padx=10, pady=10)
outputfield.grid(row=0, column=2, padx=10, pady=10)

inputfield.insert(0, "Enter your quantity")

#create combobox for metric values
metriclist = ["femto", "pico", "nano", "micro", "milli", "centi", "deci","base value", "deca", "hecto", "kilo", "mega", "giga", "tera", "peta"]
inputcombobox = ttk.Combobox(root, value=metriclist, font=fieldfont, justify="center")
outputcombobox = ttk.Combobox(root, value=metriclist, font=fieldfont, justify="center")
inputcombobox.grid(row=4)
tolabel = tk.Label(root, text="to", font=fieldfont, bg=bgcolor)
inputcombobox.grid(row=1, column=0, padx=10, pady=10)
tolabel.grid(row=1, column=1, padx=10, pady=10)
outputcombobox.grid(row=1, column=2, padx=10, pady=10)

inputcombobox.set("base value")
outputcombobox.set("base value")

#create a conversion button
convertbutton = tk.Button(root, text="Convert", bg=buttoncolor, command=convert)
convertbutton.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)


#run main loop
root.mainloop()