import pandas as pd
from tkinter import filedialog as fd


#Need to install 'pandas', 'openpyxl'


def importILIData():
    #Allows the user to select file to open.
    file = fd.askopenfilename()
    return file
    

def vendorCheck(vendor,file):
    if vendor == "Test":
        Test(file)
    elif vendor == "OnStream":
        OnStream(file)
    elif vendor == "Encompass":
        Encompass(file)
    elif vendor == "Rosen":
        Rosen(file)


def Test(file):
    print(pd.read_excel(file))
    print('------------------------------')
    Testfile = pd.read_excel(file,usecols=[0,1,2,3]).to_dict(orient='dict') #you can use column names as well, or index location like this.
    print(Testfile.keys())
    print('------------------------------')
    print(Testfile.values())
    print('------------------------------')
    column1=Testfile['Unnamed: 0']
    print(column1[0])



def OnStream(file):
    print('------------------------------')    
    print("OnStream Printed")
    
def Rosen(file):
    print('------------------------------')
    print("Rosen Printed")

def Encompass(file):
    print('------------------------------')
    print("Encompass Printed")
    Testfile = pd.read_excel(file,sheet_name="Anomalies & Features Listing",usecols=[1,2,3,4,5,6,7,8,10,11,12,13,16,19,20,21,24]).to_dict(orient='dict') #you can use column names as well, or index location like this.
    #print(Testfile.keys())
