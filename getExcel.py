import pandas as pd
from tkinter import filedialog as fd


#Need to install 'pandas', 'openpyxl'


def importILIData(vendor):
    #Allows the user to select file to open.
    file = pd.read_excel(fd.askopenfilename())
    if vendor == "OnStream":
        OnStream(file)
    elif vendor == "Encompass":
        Encompass(file)
    elif vendor == "Rosen":
        Rosen(file)


def OnStream(file):
    #print("OnStream Printed")
    
def Rosen(file):
    #print("Rosen Printed")

def Encompass(file):
    #print("Encompass Printed")



  
    #sortFile(file)





