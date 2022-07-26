import pandas as pd
from tkinter import filedialog as fd

#Need to install 'pandas', 'openpyxl'

def importILIData():
    #Allows the user to select file to open.
    file = pd.read_excel(fd.askopenfilename())
    print(file)


