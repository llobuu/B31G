from tkinter import * #This imports all 'objects' and 'methods' from the file as if they were in this file... generally bad practice.   It DOES NOT import all modules...
from tkinter import ttk
import getExcel #Import File #2
import numpy as np



class MainWindow:
    def __init__(self, master):     #you can use something other than 'master' if you'd like.
        self.screenChoice=0
        self.main_upperFrame=Frame(master,borderwidth=1,background="#82C836",width=2200,height=1300)
        self.main_upperFrame.grid(column=0,row=0,sticky=(E,W))
        self.main_upperFrame.grid_columnconfigure(0,pad=520)
        self.main_upperFrame.grid_columnconfigure(1,pad=520)# First number is the column - will imact both sides; second number is the spacing.
       # self.main_upperFrame.propagate(False)

        self.main_frame=Frame(master,height=700)
        self.main_frame.grid(row=1,column=0,sticky=(N,E,S,W))
        self.main_frame.propagate(False)

        self.uploadScreen=Button(self.main_upperFrame,text="Upload File",command=self.upload_Screen,width=40,height=4)
        self.uploadScreen.grid(column=0,row=0)  

        self.pipelineDetail_Screen=Button(self.main_upperFrame,text="Pipeline Details",command=self.pipeline_Detail_Screen,width=40,height=4)
        self.pipelineDetail_Screen.grid(column=1,row=0)

        self.iliDisplay_Screen=Button(self.main_upperFrame,text="Data",command=self.iliData_Display,width=40,height=4)
        self.iliDisplay_Screen.grid(column=2,row=0)
        self.pipelineDetails={}



# Screen #1 - Upload Screen
    def upload_Screen(self):
        # Clean up Screen
        if self.screenChoice == 2:
            print("----------",self.screen_Elements(2),"----------")
            self.gui_elements_remove(self.screen_Elements(2))
        elif self.screenChoice ==3:
            print("----------",self.screen_Elements(3),"----------")
            self.gui_elements_remove(self.screen_Elements(3))

        self.screenChoice = 1

        self.frame1=Frame(self.main_frame,borderwidth=1,relief="solid",padx=2,pady=2)
        self.frame1.place(relheight=1,relwidth=1)


        # DropDown list for ComboBox
        self.vendorDropDown=ttk.Combobox(self.frame1,value=["Test","Onstream","Encompass","Rosen"],state="readonly")
        self.vendorDropDown.grid(row=0, column=0)

        # File Path Button
        self.upload=Button(self.frame1,text = "Upload File", command = self.pullfile)
        self.upload.grid(row=1,column=1)
        self.uploadLabel=Label(self.frame1,text="choose file")
        self.uploadLabel.grid(row=2,column=0)
        
        # Submit Button
        self.review=Button(self.frame1,text="Submit", command=self.submit_ILI4Review)
        self.review.grid(row=3,column=3)

# Screen #2 - Pipeline Detail Screen
    def pipeline_Detail_Screen(self):
        # Clean up Screen
        if self.screenChoice == 1:
            self.gui_elements_remove(self.screen_Elements(1))

        elif self.screenChoice ==3:
            self.gui_elements_remove(self.screen_Elements(3))

        self.screenChoice = 2
        self.screen2_Setup()
                         

# Screen #3 - ILI Data Display
    def iliData_Display(self):
        if self.screenChoice == 1:
            self.gui_elements_remove(self.screen_Elements(1))
        elif self.screenChoice ==2:
            self.gui_elements_remove(self.screen_Elements(2))

        self.screenChoice = 3

        self.w3_Lower=Frame(self.main_frame,borderwidth=1,relief="solid",padx=1,pady=1,background="white")
        self.w3_Lower.place(relheight=1,relwidth=1)

        self.tv1=ttk.Treeview(self.w3_Lower,columns=('feature','jointID','featureType','groupID','distance','girthUS','girthDS','jointLength','length','width','depth','depthPercent','orientation','intExt','latitude','longitude','comment'),show='headings')
        self.tv1.place(relheight=1,relwidth=1,)
        self.tv1.column("#1",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#2",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#3",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#4",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#5",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#6",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#7",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#8",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#9",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#10",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#11",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#12",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#13",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#14",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#15",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#16",anchor=CENTER,width=70,stretch=False)
        self.tv1.column("#17",anchor=CENTER,width=70,stretch=False)


        self.treescrollY=Scrollbar(self.w3_Lower,orient='vertical',command=self.tv1.yview)
        self.treescrollX=Scrollbar(self.w3_Lower,orient='horizontal',command=self.tv1.xview)
        self.tv1.configure(xscrollcommand=self.treescrollX.set,yscrollcommand=self.treescrollY.set)
        self.treescrollX.pack(side="bottom",fill="x")
        self.treescrollY.pack(side="right",fill="y")

        self.display_Dictionary()
 
# (Screen #1 Button) pullfile() - Get File Path From User
    def pullfile(self):
        self.file=getExcel.importILIData()
        self.uploadLabel["text"]=self.file
        self.submit_ILI4Review

# (Screen #1 Button) Submit_ILI4Review - Pull ComboBox selection and send to excel sorting. Chance window for display.
    def submit_ILI4Review(self):
        self.vendor=self.vendorDropDown.get()
        getExcel.vendorCheck(self.vendor, self.file)
      
# (Screen #2 Button) save_pipelineDetail - Send ILI data to screen 3
    def save_pipelineDetail(self):
        
        self.pipelineDetails["Client"]= self.client_label_input.get()
        self.pipelineDetails["License Number"]= self.license_label_input.get()
        self.pipelineDetails["Inspection Date"]= self.inspectiondate_label_input.get()
        self.pipelineDetails["Nominal OD"]= self.nominalOD_label_input.get()
        self.pipelineDetails["Nominal Wall Thickness"]= self.nominalWT_label_input.get()
        self.pipelineDetails["Corrosion Allowance"]= self.corrosionAllowance_label_input.get()
        self.pipelineDetails["SMYS"]= self.SMYS_label_input.get()
        self.pipelineDetails["Code Design Factor"]= self.designFactor_label_input.get()
        self.pipelineDetails["Location Factor"]= self.locationFactor_label_input.get()
        self.pipelineDetails["Joint Factor"]= self.jointFactor_label_input.get()
        self.pipelineDetails["Temperature Factor"]= self.temperatureFactor_label_input.get()
        self.pipelineDetails["License Pressure"]= self.licensePressure_label_input.get()
        self.pipelineDetails["Normal Operating Pressure"]= self.operatingPressure_label_input.get()
        self.pipelineDetails["Max Operating Pressure"]= self.maximumPressure_label_input.get()
        self.pipelineDetails["Substance"]= self.substance_label_input.get()
        self.pipelineDetails["To"]= self.to_label_input.get()
        self.pipelineDetails["From"]= self.from_label_input.get()
        self.pipelineDetails["Length"]= self.length_label_input.get()
        self.pipelineDetails["Material"]= self.material_label_input.get()
        self.pipelineDetails["Material Type"]= self.materialType_label_input.get()
        self.pipelineDetails["Grade"]= self.grade_label_input.get()
        self.pipelineDetails["Stress"]= self.stress_label_input.get()
        self.pipelineDetails["MOP"]= self.MOP_label_input.get()
        self.pipelineDetails["H2S"]= self.h2s_label_input.get()
        self.pipelineDetails["Age"]= self.age_label_input.get()
        self.pipelineDetails["Cased Crossing"]= self.casedCrossing_label_input.get()
        self.pipelineDetails["Road Crossing"]= self.roadCrossing_label_input.get()
        self.pipelineDetails["Railway Crossing"]= self.railwayCrossing_label_input.get()
        self.pipelineDetails["Stations Crossing"]= self.stationCrossing_label_input.get()
        self.pipelineDetails["Other Crossings"]= self.otherCrossing_label_input.get()
        self.pipelineDetails["Substance Class"]= self.substanceClass_label_input.get()
        self.pipelineDetails["Pipeline Class"]= self.pipelineClass_label_input.get()
        self.pipelineDetails["Seam Type"]= self.seamType_label_input.get()
# (Screen 2) - screen2_Setup (load widgets for screen 2) 
    def screen2_Setup(self):
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
        self.inspectiondate_label_input=StringVar()
        self.inspectiondate_label_input=ttk.Entry(self.frame_left_upper,textvariable=self.inspectiondate_label_input)
        self.inspectiondate_label_input.grid(column=1,row=3)
        self.nominalOD_label_input=StringVar()
        self.nominalOD_label_input=ttk.Entry( self.frame_left_lower,textvariable=self.nominalOD_label_input)
        self.nominalOD_label_input.grid(column=1,row=5)
        self.nominalWT_label_input=StringVar()
        self.nominalWT_label_input=ttk.Entry( self.frame_left_lower,textvariable=self.nominalWT_label_input)
        self.nominalWT_label_input.grid(column=1,row=6)
        self.corrosionAllowance_label_input=StringVar()
        self.corrosionAllowance_label_input=ttk.Entry( self.frame_left_lower,textvariable=self.corrosionAllowance_label_input)
        self.corrosionAllowance_label_input.grid(column=1,row=7)
        self.SMYS_label_input=StringVar()
        self.SMYS_label_input=ttk.Entry( self.frame_left_lower,textvariable=self.SMYS_label_input)
        self.SMYS_label_input.grid(column=1,row=8)
        self.designFactor_label_input=StringVar()
        self.designFactor_label_input=ttk.Entry( self.frame_left_lower,textvariable=self.designFactor_label_input)
        self.designFactor_label_input.grid(column=1,row=9)
        self.locationFactor_label_input=StringVar()
        self.locationFactor_label_input=ttk.Entry( self.frame_left_lower,textvariable=self.locationFactor_label_input)
        self.locationFactor_label_input.grid(column=1,row=10)
        self.jointFactor_label_input=StringVar()
        self.jointFactor_label_input=ttk.Entry( self.frame_left_lower,textvariable=self.jointFactor_label_input)
        self.jointFactor_label_input.grid(column=1,row=11)
        self.temperatureFactor_label_input=StringVar()
        self.temperatureFactor_label_input=ttk.Entry( self.frame_left_lower,textvariable=self.temperatureFactor_label_input)
        self.temperatureFactor_label_input.grid(column=1,row=12)
        self.licensePressure_label_input=StringVar()
        self.licensePressure_label_input=ttk.Entry( self.frame_left_lower,textvariable=self.licensePressure_label_input)
        self.licensePressure_label_input.grid(column=1,row=13)
        self.operatingPressure_label_input=StringVar()
        self.operatingPressure_label_input=ttk.Entry( self.frame_left_lower,textvariable=self.operatingPressure_label_input)
        self.operatingPressure_label_input.grid(column=1,row=14)
        self.maximumPressure_label_input=StringVar()
        self.maximumPressure_label_input=ttk.Entry( self.frame_left_lower,textvariable=self.maximumPressure_label_input)
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
        self.substance_label_input=StringVar()
        self.substance_label_input=ttk.Entry(self.frame_middle,textvariable=self.substance_label_input)
        self.substance_label_input.grid(column=4,row=5)
        self.to_label_input=StringVar()
        self.to_label_input=ttk.Entry(self.frame_middle,textvariable=self.to_label_input)
        self.to_label_input.grid(column=4,row=6)
        self.from_label_input=StringVar()
        self.from_label_input=ttk.Entry(self.frame_middle,textvariable=self.from_label_input)
        self.from_label_input.grid(column=4,row=7)
        self.length_label_input=StringVar()
        self.length_label_input=ttk.Entry(self.frame_middle,textvariable=self.length_label_input)
        self.length_label_input.grid(column=4,row=8)
        self.material_label_input=StringVar()
        self.material_label_input=ttk.Entry(self.frame_middle,textvariable=self.material_label_input)
        self.material_label_input.grid(column=4,row=9)
        self.materialType_label_input=StringVar()
        self.materialType_label_input=ttk.Entry(self.frame_middle,textvariable=self.materialType_label_input)
        self.materialType_label_input.grid(column=4,row=10)
        self.grade_label_input=StringVar()
        self.grade_label_input=ttk.Entry(self.frame_middle,textvariable=self.grade_label_input)
        self.grade_label_input.grid(column=4,row=11)
        self.stress_label_input=StringVar()
        self.stress_label_input=ttk.Entry(self.frame_middle,textvariable=self.stress_label_input)
        self.stress_label_input.grid(column=4,row=12)
        self.MOP_label_input=StringVar()
        self.MOP_label_input=ttk.Entry(self.frame_middle,textvariable=self.MOP_label_input)
        self.MOP_label_input.grid(column=4,row=13)
        self.h2s_label_input=StringVar()
        self.h2s_label_input=ttk.Entry(self.frame_middle,textvariable=self.h2s_label_input)
        self.h2s_label_input.grid(column=4,row=14)
        self.age_label_input=StringVar()
        self.age_label_input=ttk.Entry(self.frame_middle,textvariable=self.age_label_input)
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
        self.casedCrossing_label_input=ttk.Combobox(self.frame_right,value=["Yes","No"],background="white",state="readonly")
        self.casedCrossing_label_input.grid(column=6,row=5)
        self.roadCrossing_label_input=ttk.Combobox(self.frame_right,value=["Yes","No"],background="white",state="readonly")
        self.roadCrossing_label_input.grid(column=6,row=6)
        self.railwayCrossing_label_input=ttk.Combobox(self.frame_right,value=["Yes","No"],background="white",state="readonly")
        self.railwayCrossing_label_input.grid(column=6,row=7)
        self.stationCrossing_label_input=ttk.Combobox(self.frame_right,value=["Yes","No"],background="white",state="readonly")
        self.stationCrossing_label_input.grid(column=6,row=8)
        self.otherCrossing_label_input=ttk.Combobox(self.frame_right,value=["Yes","No"],background="white",state="readonly")
        self.otherCrossing_label_input.grid(column=6,row=9)
        self.substanceClass_label_input=ttk.Combobox(self.frame_right,value=["Gas","Multiphase"],background="white",state="readonly")
        self.substanceClass_label_input.grid(column=6,row=10)
        self.pipelineClass_label_input=ttk.Combobox(self.frame_right,state="readonly",background="white",value=["None","10 or fewer dwelling units","11 to 46 dwellings","46 or more dwelling units","prevelance of buildings intended for oiccupancy with 4 or more stories"])
        self.pipelineClass_label_input.grid(column=6,row=11)
        self.seamType_label_input=ttk.Combobox(self.frame_right,state="readonly",background="white",value=["Seamless","Electric Welder","Submerged Arc Welded","Continuous Weld"])
        self.seamType_label_input.grid(column=6,row=12)
      
        # Submit Button at the bottom
        self.save_button=ttk.Button(self.frame_right,text="Save Data",command=self.save_pipelineDetail)
        self.save_button.grid(column=4,row=13)

# gui_elements_remove - Delete widgets from screen (generic) 
    def gui_elements_remove(self,elements):
        for element in elements:
            element.destroy()
       
# display_Dictionary - Display ILI data and results to user (generic)
    def display_Dictionary(self):
        rowNumber=1
        
        self.tv1.heading('feature',text='Feature',anchor='n')
        self.tv1.heading('jointID',text='Joint ID',anchor='n')
        self.tv1.heading('featureType',text='Feature\nType',anchor='n')
        self.tv1.heading('groupID',text='Group ID',anchor='n')
        self.tv1.heading('distance',text='Distance',anchor='n')
        self.tv1.heading('girthUS',text='US\nGirth Weld',anchor='n')
        self.tv1.heading('girthDS',text='DS\nGirth Weld',anchor='n')
        self.tv1.heading('jointLength',text='Joint\nLength',anchor='n')
        self.tv1.heading('length',text='Length',anchor='n')
        self.tv1.heading('width',text='Width',anchor='n')
        self.tv1.heading('depth',text='Depth',anchor='n')
        self.tv1.heading('depthPercent',text='Depth %',anchor='n')
        self.tv1.heading('orientation',text='Orientation',anchor='n')
        self.tv1.heading('intExt',text='Int/Ext',anchor='n')
        self.tv1.heading('latitude',text='Latitude',anchor='n')
        self.tv1.heading('longitude',text='Longitude',anchor='n')
        self.tv1.heading('comment',text='Comments',anchor='n')


        for i in getExcel.newFeaturesList: # Sort through Features (i = feature ID)
            list=[]
            for j in getExcel.newFeaturesList[i]: # Sort through feature specifics (J = specific information in row)
                if getExcel.newFeaturesList[i][j] != getExcel.newFeaturesList[i][j]:
                    #print("NaN") #Test case
                    list.append("")
                else:
                    #print("good")    # Test case
                    list.append(getExcel.newFeaturesList[i][j])
            self.tv1.insert("","end",values=list)





# screen_Elements - frames to delete when switching tabs (semi-generic)    
    def screen_Elements(self,number):
        if number == 1:
            return [self.frame1
                   ]
        elif number == 2:
           return [self.frame_left_upper,
                   self.frame_left_lower,
                   self.frame_middle,                             
                   self.frame_right,
                   self.save_button
                   ]
        elif number == 3:
            return [self.w3_Lower
                   ]            


def main():
    global root

    root=Tk()
    root.geometry("2200x1300")
    #root.resizable(width=FALSE,height=FALSE)
    window=MainWindow(root)
    
    root.mainloop()

if __name__ == '__main__':
    main()
 

