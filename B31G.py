from tkinter import *
import getExcel
from functools import partial
from tkinter import ttk

global vendorSelect2



root=Tk()

#Makes the window fullscreen... but no customization
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
#root.geometry("%dx%d" % (width, height))

#callback for vendor
def callbackFunc(event):
    vendorDropDown=event.get()
    print(vendorDropDown)

# Create a dropdown list of vendors for formatting purposes.
options=[
    "Test",
    "OnStream",
    "Encompass",
    "Rosen"]

#
vendorDropDown=ttk.Combobox(root, value=options)
vendorDropDown.current(0)
vendorDropDown.bind("<<ComboboxSelected>>", command=callbackFunc)
vendorDropDown.grid(row=0, column=0)

# Use this to pass function through button
action_with_arg = partial(getExcel.vendorCheck,vendorDropDown.get())
                                             
# Create a button for uploading excel data
upload=Button(root, text = "Upload File", command = action_with_arg)
upload.grid(row=1,column=1)

#
review=Button(root,text="Submit", command=action_with_arg)
review.grid(row=2,column=2)




root.mainloop()
