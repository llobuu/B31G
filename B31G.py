from tkinter import *
import getExcel
from functools import partial

global vendorDropDrown


root=Tk()

#Makes the window fullscreen... but no customization
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
#root.geometry("%dx%d" % (width, height))



# Create a dropdown list of vendors for formatting purposes.
options=[
    "OnStream",
    "Encompass",
    "Rosen"]
vendorSelect=StringVar(root)
vendorSelect.set(options[0])    #default vendor
vendorDropDown=OptionMenu(root, vendorSelect, *options)
vendorDropDown.grid(row=0, column=0)

# Use this to pass function through button
action_with_arg = partial(getExcel.importILIData,vendorSelect.get())

                                         

# Create a button for uploading excel data
upload=Button(root, text = "Upload File", command = action_with_arg)
upload.grid(row=1,column=1)



root.mainloop()
