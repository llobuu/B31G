from pyexpat import features
import pandas as pd
from tkinter import filedialog as fd
newFeaturesList={}

#Need to install 'pandas', 'openpyxl'


# Allows the user to select file to open.
def importILIData():

    file = fd.askopenfilename()
    return file
    
# Reads the vendor selected in the drop down and chooses the function for analysis.
def vendorCheck(vendor,file):
    if vendor == "Test":
        Test(file)
    elif vendor == "OnStream":
        OnStream(file)
    elif vendor == "Encompass":
        Encompass(file)
    elif vendor == "Rosen":
        Rosen(file)

# Test function
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



# OnStream function
def OnStream(file):
    print('------------------------------')    
    print("OnStream Printed")
    


# Rosen function
def Rosen(file):
    print('------------------------------')
    print("Rosen Printed")



# Encompass function
def Encompass(file):
    #print('------------------------------')
    Testfile = pd.read_excel(file,sheet_name="Anomalies & Features Listing",usecols=[1,2,3,4,5,6,7,8,10,11,12,13,16,19,20,21,24],skiprows=[0,1,2,3,4,5,6]).to_dict(orient='dict')#you can use column names as well, or index location like this.
    #print(Testfile.keys())

    #variable for only the feature id's.



    originalFeature=Testfile['Feature\nID']
    originalJoint=Testfile['Joint\nID']
    originalFeatureType=Testfile['Feature\nType']
    originalGroup=Testfile['Group\nID']
    originalDistance=Testfile['Distance']
    originalUSGW=Testfile['US GW\nDistance']
    originalDSGW=Testfile['DS GW\nDistance.']
    originalJointLength=Testfile['Joint\nLength']
    originalLength=Testfile['Length']
    originalWidth=Testfile['Width']
    originalDepth=Testfile['Depth']
    originalCurrentPercent=Testfile['Current\nDepth\nPercent']
    originalOrientation=Testfile['Clock\nOrientation']
    originalIntExt=Testfile['Int/Ext']
    originalLatitude=Testfile['Latitude']
    originalLongitude=Testfile['Longitude']
    originalComments=Testfile['Comments']
    
    #Create a dict of feature id's, to later add components (like a hash)
    for i in Testfile['Feature\nID']:
 # Add the feature as level 1 dict       
        newFeaturesList[originalFeature[i]]={}
 # Add all level 2 items for disct (Joint ID, 
        newFeaturesList[originalFeature[i]]['Joint ID']=originalJoint[i]
        newFeaturesList[originalFeature[i]]['Feature Type']=originalFeatureType[i]
        newFeaturesList[originalFeature[i]]['Group ID']=originalGroup[i]
        newFeaturesList[originalFeature[i]]['Distance']=originalDistance[i]
        newFeaturesList[originalFeature[i]]['US Girth Weld']=originalUSGW[i]
        newFeaturesList[originalFeature[i]]['DS Girth Weld']=originalDSGW[i]
        newFeaturesList[originalFeature[i]]['Joint Length']=originalJointLength[i]
        newFeaturesList[originalFeature[i]]['Length']=originalLength[i]
        newFeaturesList[originalFeature[i]]['Width']=originalWidth[i]
        newFeaturesList[originalFeature[i]]['Depth']=originalDepth[i]
        newFeaturesList[originalFeature[i]]['Depth %']=originalCurrentPercent[i]
        newFeaturesList[originalFeature[i]]['Orientation']=originalOrientation[i]
        newFeaturesList[originalFeature[i]]['Internal/External']=originalIntExt[i]
        newFeaturesList[originalFeature[i]]['Latitude']=originalLatitude[i]
        newFeaturesList[originalFeature[i]]['Longitude']=originalLongitude[i]
        newFeaturesList[originalFeature[i]]['Comments']=originalComments[i]
    #print(newFeaturesList.keys())


 
    

        




