from tkinter import *
import getExcel
from tkinter import ttk

root=Tk()
root.title("Test1")
root.geometry("400x400")

class Window:
    def __init__(self, master):     #you can use something other than 'master' if you'd like.
        #self.master
        
        #Frame
        myframe=Frame(master)
        myframe.grid(column=500,row=500)
  

     
        #Makes the window fullscreen... but no customization
        #width=root.winfo_screenwidth()
        #height=root.winfo_screenheight()
        #root.geometry("%dx%d" % (width, height))
        
        # DropDown list for ComboBox
        self.options=[
            "Test",
            "OnStream",
            "Encompass",
            "Rosen"]
        self.vendorDropDown=ttk.Combobox(master, value=self.options)
        self.vendorDropDown.current(0)
        self.vendorDropDown.bind("<<ComboboxSelected>>")
        self.vendorDropDown.grid(row=0, column=0)

        # Upload Button
        self.upload=Button(master, text = "Upload File", command = self.pullfile)
        self.upload.grid(row=1,column=1)
        
        # Review Button
        self.review=Button(master,text="Submit", command=self.callbackFunc)
        self.review.grid(row=2,column=2)
    
    #Pull ComboBox selection and send to excel sorting.
    def callbackFunc(self):
        self.vendor=self.vendorDropDown.get()
        print(self.vendor)
        print(self.file)
        getExcel.vendorCheck(self.vendor, self.file)

    def pullfile(self):
        self.file=getExcel.importILIData()


 
e=Window(root)
root.mainloop()
