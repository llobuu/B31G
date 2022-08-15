from textwrap import fill
from tkinter import *
from tkinter import ttk
import getExcel




class MainWindow:
    def __init__(self, master):     #you can use something other than 'master' if you'd like.
        self.main_frame=Frame(master)
        self.main_frame.grid(row=0,column=0,sticky=(N,E,S,W))
        self.upload_Screen()
# Screen #1 - Upload Screen
    def upload_Screen(self):   
        root.title("Vendor Data Screen")


        self.frame1=Frame(self.main_frame,borderwidth=1,relief="solid",padx=2,pady=2,bg="red")
        self.frame1.grid(column=0,row=0,columnspan=4,rowspan=4)

        # DropDown list for ComboBox
        self.vendorDropDown=ttk.Combobox(self.frame1,value=["Test","Onstream","Encompass","Rosen"])
        #self.vendorDropDown.current(0)
        #self.vendorDropDown.bind("<<ComboboxSelected>>")
        self.vendorDropDown.grid(row=0, column=0)

        # File Path Button
        self.upload=Button(self.frame1,text = "Upload File", command = self.pullfile)
        self.upload.grid(row=1,column=1)
        
        # Submit Button
        self.review=Button(self.frame1,text="Submit", command=self.submit_ILI4Review)
        self.review.grid(row=4,column=4)
        self.gui_elements=[self.vendorDropDown,
                           self.upload,
                           self.review,
                           self.frame1]

# Screen #2 - Pipeline Detail Screen
    def pipeline_Detail_Screen(self,event):
        # Clean up Screen 1
        self.gui_elements_remove(self.gui_elements)
        root.title("Pipeline Specific Data")

        # Set up Frames for Screen 2
        self.frame_left_upper=Frame(self.main_frame,borderwidth=1,relief="solid",padx=1,pady=1,background="white")
        self.frame_left_upper.grid(column=0,row=0,sticky="e,w")
        self.frame_left_lower=Frame(self.main_frame,borderwidth=1,relief="solid",padx=1,pady=1,background="white")
        self.frame_left_lower.grid(column=0,row=1)
        self.frame_middle=Frame(self.main_frame,borderwidth=1,relief="solid",padx=1,pady=1,background="white")
        self.frame_middle.grid(column=2,row=1)
        self.frame_right=Frame(self.main_frame,borderwidth=1,relief="solid",padx=1,pady=1,background="white")
        self.frame_right.grid(column=3,row=1,sticky="n")

        # Column 1 Pipeline Static Design Details (Labels)
        self.detail_label_1=ttk.Label(self.frame_left_upper,text="Pipeline Identification",background="white", font="Arial 14 bold",anchor="n",justify='center')
        self.detail_label_1.grid(column=0,row=0,columnspan=2)
        self.client_label=ttk.Label(self.frame_left_upper,text="Client: ",background="white")
        self.client_label.grid(column=0,row=1,sticky='e')
        self.license_label=ttk.Label(self.frame_left_upper,text="Pipeline License Number: ",background="white")
        self.license_label.grid(column=0,row=2,sticky='e')
        self.inspectiondate_label=ttk.Label(self.frame_left_upper,text="Inspection Date: ",background="white")
        self.inspectiondate_label.grid(column=0,row=3,sticky='e')
        self.detail_label_2=ttk.Label( self.frame_left_lower,text="Pipeline Static Design Details",background="white", font="Arial 14 bold",width=30,anchor="n",justify='center')
        self.detail_label_2.grid(column=0,row=4,columnspan=2)
        self.nominalOD_label=ttk.Label( self.frame_left_lower,text="Nominal OD: ",background="white")
        self.nominalOD_label.grid(column=0,row=5,sticky='e')
        self.nominalWT_label=ttk.Label( self.frame_left_lower,text="Nominal Wall Thickness (WT): ",background="white")
        self.nominalWT_label.grid(column=0,row=6,sticky='e')
        self.corrosionAllowance_label=ttk.Label( self.frame_left_lower,text="Corrosion/Inspection Allowance: ",background="white")
        self.corrosionAllowance_label.grid(column=0,row=7,sticky='e')
        self.SMYS_label=ttk.Label( self.frame_left_lower,text="SMYS: ",background="white")
        self.SMYS_label.grid(column=0,row=8,sticky='e')
        self.designFactor_label=ttk.Label( self.frame_left_lower,text="Code Design Factor, F: ",background="white")
        self.designFactor_label.grid(column=0,row=9,sticky='e')
        self.locationFactor_label=ttk.Label( self.frame_left_lower,text="Location Factor, L: ",background="white")
        self.locationFactor_label.grid(column=0,row=10,sticky='e')
        self.jointFactor_label=ttk.Label( self.frame_left_lower,text="Joint Factor, L: ",background="white")
        self.jointFactor_label.grid(column=0,row=11,sticky='e')
        self.temperatureFactor_label=ttk.Label( self.frame_left_lower,text="Temperature Factor, T: ",background="white")
        self.temperatureFactor_label.grid(column=0,row=12,sticky='e')
        self.licensePressure_label=ttk.Label( self.frame_left_lower,text="License Pressure (kPa): ",background="white")
        self.licensePressure_label.grid(column=0,row=13,sticky='e')
        self.operatingPressure_label=ttk.Label( self.frame_left_lower,text="Normal Operating Pressure (kPa): ",background="white")
        self.operatingPressure_label.grid(column=0,row=14,sticky='e')
        self.maximumPressure_label=ttk.Label( self.frame_left_lower,text="Maximum Possible Pressure (kPa): ",background="white")
        self.maximumPressure_label.grid(column=0,row=15,sticky='e')
        
        # Column 2 User Input for Pipeline Static Design Details
        self.client_label_input=StringVar()
        self.client_label_input=ttk.Entry(self.frame_left_upper,textvariable=self.client_label_input)
        self.client_label_input.grid(column=1,row=1)

        self.license_label_input=StringVar()
        self.license_label_input=ttk.Entry(self.frame_left_upper,textvariable=self.client_label_input)
        self.license_label_input.grid(column=1,row=2)


        self.inspectiondate_label_input=ttk.Entry(self.frame_left_upper)
        self.inspectiondate_label_input.grid(column=1,row=3)

        self.nominalOD_label_input=ttk.Entry( self.frame_left_lower)
        self.nominalOD_label_input.grid(column=1,row=5)

        self.nominalWT_label_input=ttk.Entry( self.frame_left_lower)
        self.nominalWT_label_input.grid(column=1,row=6)

        self.corrosionAllowance_label_input=ttk.Entry( self.frame_left_lower)
        self.corrosionAllowance_label_input.grid(column=1,row=7)

        self.SMYS_label_input=ttk.Entry( self.frame_left_lower)
        self.SMYS_label_input.grid(column=1,row=8)

        self.designFactor_label_input=ttk.Entry( self.frame_left_lower)
        self.designFactor_label_input.grid(column=1,row=9)

        self.locationFactor_label_input=ttk.Entry( self.frame_left_lower)
        self.locationFactor_label_input.grid(column=1,row=10)

        self.jointFactor_label_input=ttk.Entry( self.frame_left_lower)
        self.jointFactor_label_input.grid(column=1,row=11)

        self.temperatureFactor_label_input=ttk.Entry( self.frame_left_lower)
        self.temperatureFactor_label_input.grid(column=1,row=12)

        self.licensePressure_label_input=ttk.Entry( self.frame_left_lower)
        self.licensePressure_label_input.grid(column=1,row=13)

        self.operatingPressure_label_input=ttk.Entry( self.frame_left_lower)
        self.operatingPressure_label_input.grid(column=1,row=14)

        self.maximumPressure_label_input=ttk.Entry( self.frame_left_lower)
        self.maximumPressure_label_input.grid(column=1,row=15)
          
        # Column 3 PL 100 Data (Labels)
        self.detail_label_3=ttk.Label(self.frame_middle,text="PL 100 Data",background="white", font="Arial 14 bold",width=20,anchor="n",justify='center')
        self.detail_label_3.grid(column=3,row=4,columnspan=2)
        self.substance_label=ttk.Label(self.frame_middle,text="Substance: ",background="white")
        self.substance_label.grid(column=3,row=5,sticky='e')
        self.to_Label=ttk.Label(self.frame_middle,text="To: ",background="white")
        self.to_Label.grid(column=3,row=6,sticky='e')
        self.from_label=ttk.Label(self.frame_middle,text="From: ",background="white")
        self.from_label.grid(column=3,row=7,sticky='e')
        self.length_label=ttk.Label(self.frame_middle,text="Length (km): ",background="white")
        self.length_label.grid(column=3,row=8,sticky='e')
        self.material_label=ttk.Label(self.frame_middle,text="Material: ",background="white")
        self.material_label.grid(column=3,row=9,sticky='e')
        self.materialType_label=ttk.Label(self.frame_middle,text="Material Type: ",background="white")
        self.materialType_label.grid(column=3,row=10,sticky='e')
        self.grade_label=ttk.Label(self.frame_middle,text="Grade: ",background="white")
        self.grade_label.grid(column=3,row=11,sticky='e')
        self.stress_label=ttk.Label(self.frame_middle,text="Stress: ",background="white")
        self.stress_label.grid(column=3,row=12,sticky='e')
        self.MOP_label=ttk.Label(self.frame_middle,text="MOP: ",background="white")
        self.MOP_label.grid(column=3,row=13,sticky='e')
        self.h2s_label=ttk.Label(self.frame_middle,text="H2S: ",background="white")
        self.h2s_label.grid(column=3,row=14,sticky='e')
        self.age_label=ttk.Label(self.frame_middle,text="Age: ",background="white")
        self.age_label.grid(column=3,row=15,sticky='e')

        # Column 4 User Input for PL 100 Data 
        self.substance_label_input=ttk.Entry(self.frame_middle)
        self.substance_label_input.grid(column=4,row=5)
        self.to_label_input=ttk.Entry(self.frame_middle)
        self.to_label_input.grid(column=4,row=6)
        self.from_label_input=ttk.Entry(self.frame_middle)
        self.from_label_input.grid(column=4,row=7)
        self.length_label_input=ttk.Entry(self.frame_middle)
        self.length_label_input.grid(column=4,row=8)
        self.material_label_input=ttk.Entry(self.frame_middle)
        self.material_label_input.grid(column=4,row=9)
        self.materialType_label_input=ttk.Entry(self.frame_middle)
        self.materialType_label_input.grid(column=4,row=10)
        self.grade_label_input=ttk.Entry(self.frame_middle)
        self.grade_label_input.grid(column=4,row=11)
        self.stress_label_input=ttk.Entry(self.frame_middle)
        self.stress_label_input.grid(column=4,row=12)
        self.MOP_label_input=ttk.Entry(self.frame_middle)
        self.MOP_label_input.grid(column=4,row=13)
        self.h2s_label_input=ttk.Entry(self.frame_middle)
        self.h2s_label_input.grid(column=4,row=14)
        self.age_label_input=ttk.Entry(self.frame_middle)
        self.age_label_input.grid(column=4,row=15)
          
        # Column 5 Env Factors (Labels)
        self.detail_label_4=ttk.Label(self.frame_right,text="Env Factors",background="white", font="Arial 14 bold",anchor="n",justify='center')
        self.detail_label_4.grid(column=5,row=4,columnspan=2)
        self.casedCrossing_label=ttk.Label(self.frame_right,text="Cased Crossings: ",background="white")
        self.casedCrossing_label.grid(column=5,row=5,sticky='e')
        self.roadCrossing_label=ttk.Label(self.frame_right,text="Road Crossings: ",background="white")
        self.roadCrossing_label.grid(column=5,row=6,sticky='e')
        self.railwayCrossing_label=ttk.Label(self.frame_right,text="Railway Crossings: ",background="white")
        self.railwayCrossing_label.grid(column=5,row=7,sticky='e')
        self.stationCrossing_label=ttk.Label(self.frame_right,text="Station Crossings: ",background="white")
        self.stationCrossing_label.grid(column=5,row=8,sticky='e')
        self.otherCrossing_label=ttk.Label(self.frame_right,text="Other Crossings: ",background="white")
        self.otherCrossing_label.grid(column=5,row=9,sticky='e')
        self.substanceClass_label=ttk.Label(self.frame_right,text="Substance Class: ",background="white")
        self.substanceClass_label.grid(column=5,row=10,sticky='e')
        self.pipelineClass_label=ttk.Label(self.frame_right,text="Pipeline Class: ",background="white")
        self.pipelineClass_label.grid(column=5,row=11,sticky='e')
        self.seamType_label=ttk.Label(self.frame_right,text="Seam Type: ",background="white")
        self.seamType_label.grid(column=5,row=12,sticky='e')
        
        # Column 6 User Input for Env Factors
        self.casedCrossing_label_input=ttk.Combobox(self.frame_right,value=["Yes","No"],background="white")
        self.casedCrossing_label_input.grid(column=6,row=5)
        self.roadCrossing_label_input=ttk.Combobox(self.frame_right,value=["Yes","No"],background="white")
        self.roadCrossing_label_input.grid(column=6,row=6)
        self.railwayCrossing_label_input=ttk.Combobox(self.frame_right,value=["Yes","No"],background="white")
        self.railwayCrossing_label_input.grid(column=6,row=7)
        self.stationCrossing_label_input=ttk.Combobox(self.frame_right,value=["Yes","No"],background="white")
        self.stationCrossing_label_input.grid(column=6,row=8)
        self.otherCrossing_label_input=ttk.Combobox(self.frame_right,value=["Yes","No"],background="white")
        self.otherCrossing_label_input.grid(column=6,row=9)
        self.substanceClass_label_input=ttk.Combobox(self.frame_right,value=["Gas","Multiphase"],background="white")
        self.substanceClass_label_input.grid(column=6,row=10)
        self.pipelineClass_label_input=ttk.Combobox(self.frame_right,background="white",value=["None","10 or fewer dwelling units","11 to 46 dwellings","46 or more dwelling units","prevelance of buildings intended for oiccupancy with 4 or more stories"])
        self.pipelineClass_label_input.grid(column=6,row=11)
        self.seamType_label_input=ttk.Combobox(self.frame_right,background="white",value=["Seamless","Electric Welder","Submerged Arc Welded","Continuous Weld"])
        self.seamType_label_input.grid(column=6,row=12)
      
        # Submit Button at the bottom
        self.submit_button=ttk.Button(text="Submit",command=self.submit_pipelineDetail)
        self.submit_button.grid(column=7,row=13)

# Screen #3 - ILI Data Display
    #def iliData_Display()

    # (Screen #1) pullfile() - Get File Path From User
    def pullfile(self):
        self.file=getExcel.importILIData()

    # (Screen #1) submit_ILI4Review - Pull ComboBox selection and send to excel sorting. Chance window for display.
    def submit_ILI4Review(self):
        self.vendor=self.vendorDropDown.get()
        getExcel.vendorCheck(self.vendor, self.file)
        self.pipeline_Detail_Screen(self)
      
    # (Screen #2) submit_pipelineDetail - Send ILI data to...
    def submit_pipelineDetail(self):
        global pipelineDetails
        pipelineDetails={}
        pipelineDetails["Client"]= self.client_label_input.get()
        pipelineDetails["License Number"]= self.license_label_input
        pipelineDetails["Inspection Date"]= self.inspectiondate_label_input
        pipelineDetails["Nominal OD"]= self.nominalOD_label_input
        pipelineDetails["Nominal Wall Thickness"]= self.nominalWT_label_input
        pipelineDetails["Corrosion Allowance"]= self.corrosionAllowance_label_input
        pipelineDetails["SMYS"]= self.SMYS_label_input
        pipelineDetails["Code Design Factor"]= self.designFactor_label_input
        pipelineDetails["Location Factor"]= self.locationFactor_label_input
        pipelineDetails["Joint Factor"]= self.jointFactor_label_input
        pipelineDetails["Temperature Factor"]= self.temperatureFactor_label_input
        pipelineDetails["License Pressure"]= self.licensePressure_label_input
        pipelineDetails["Normal Operating Pressure"]= self.operatingPressure_label_input
        pipelineDetails["Max Operating Pressure"]= self.maximumPressure_label_input
        pipelineDetails["Substance"]= self.substance_label_input
        pipelineDetails["To"]= self.to_label_input
        pipelineDetails["From"]= self.from_label_input
        pipelineDetails["Length"]= self.length_label_input
        pipelineDetails["Material"]= self.material_label_input
        pipelineDetails["Material Type"]= self.materialType_label_input
        pipelineDetails["Grade"]= self.grade_label_input
        pipelineDetails["Stress"]= self.stress_label_input
        pipelineDetails["MOP"]= self.MOP_label_input
        pipelineDetails["H2S"]= self.h2s_label_input
        pipelineDetails["Age"]= self.age_label_input
        pipelineDetails["Cased Crossing"]= self.casedCrossing_label_input
        pipelineDetails["Road Crossing"]= self.roadCrossing_label_input
        pipelineDetails["Railway Crossing"]= self.railwayCrossing_label_input
        pipelineDetails["Stations Crossing"]= self.stationCrossing_label_input
        pipelineDetails["Other Crossings"]= self.otherCrossing_label_input
        pipelineDetails["Substance Class"]= self.substanceClass_label_input
        pipelineDetails["Pipeline Class"]= self.pipelineClass_label_input
        pipelineDetails["Seam Type"]= self.seamType_label_input
#----Why doesn't this work? Check formatting input.        
        print(pipelineDetails["Client"])

    # gui_elements_remove - Delete current screen widgets
    def gui_elements_remove(self,elements):
        for element in elements:
            element.destroy()
     
def main():
    global root

    root=Tk()
    root.geometry("1000x1000")
    #root.resizable(width=FALSE,height=FALSE)
    window=MainWindow(root)
    
    root.mainloop()

if __name__ == '__main__':
    main()
 

