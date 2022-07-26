from tkinter import *
import getExcel



root=Tk()
#Makes the window fullscreen... but no customization
root.attributes("-fullscreen", True)


upload=Button(root, text = "Upload File", command = getExcel.importILIData)
upload.grid(row=1,column=1)

root.mainloop()
