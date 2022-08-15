from tkinter import *
from tkinter import ttk
import getExcel



class MainWindow:
    def __init__(self, master):     #you can use something other than 'master' if you'd like.
        self.main_frame=Frame(master)
        self.main_frame.grid(row=0,column=0,sticky=(N,E,S,W))
        self.upload_Screen()
# Screen #1
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
        self.review=Button(self.frame1,text="Submit", command=self.callbackFunc)
        self.review.grid(row=4,column=4)
        self.gui_elements=[self.vendorDropDown,
                           self.upload,
                           self.review,
                           self.frame1]
# Screen #2
    def pipeline_Detail_Screen(self,event):
        # Clean up Screen 1
        self.gui_elements_remove(self.gui_elements)
        root.title("Pipeline Specific Data")

        # Set up Frames for Screen 2
        self.frame_left_upper=Frame(self.main_frame,borderwidth=1,relief="solid",padx=2,pady=2)
        self.frame_left_upper.grid(column=0,row=0)
        self.frame_left_lower=Frame(self.main_frame,borderwidth=1,relief="solid",padx=2,pady=2)
        self.frame_left_lower.grid(column=0,row=4)
        self.frame_middle=Frame(self.main_frame,borderwidth=1,relief="solid",padx=2,pady=2)
        self.frame_middle.grid(column=2,row=0,rowspan=2)
        self.frame_right=Frame(self.main_frame,borderwidth=1,relief="solid",padx=2,pady=2)
        self.frame_right.grid(column=4,row=0,rowspan=2)

        # Column 1 Pipeline Static Design Details (Labels)
        self.detail_label_1=ttk.Label(self.frame_left_upper,text="Pipeline Identification",background="white", font="10")
        self.detail_label_1.grid(column=0,row=0,columnspan=2)
        self.detail_label_2=ttk.Label(self.frame_left_upper,text="Client: ")
        self.detail_label_2.grid(column=0,row=1,sticky='e')
        self.detail_label_3=ttk.Label(self.frame_left_upper,text="Pipeline License Number: ")
        self.detail_label_3.grid(column=0,row=2,sticky='e')
        self.detail_label_4=ttk.Label(self.frame_left_upper,text="Inspection Date: ")
        self.detail_label_4.grid(column=0,row=3,sticky='e')
        self.detail_label_5=ttk.Label( self.frame_left_lower,text="Pipeline Static Design Details",background="white", font="10")
        self.detail_label_5.grid(column=0,row=4,sticky='e',columnspan=2)
        self.detail_label_6=ttk.Label( self.frame_left_lower,text="Nominal OD: ")
        self.detail_label_6.grid(column=0,row=5,sticky='e')
        self.detail_label_7=ttk.Label( self.frame_left_lower,text="Nominal Wall Thickness (WT): ")
        self.detail_label_7.grid(column=0,row=6,sticky='e')
        self.detail_label_8=ttk.Label( self.frame_left_lower,text="Corrosion/Inspection Allowance: ")
        self.detail_label_8.grid(column=0,row=7,sticky='e')
        self.detail_label_9=ttk.Label( self.frame_left_lower,text="SMYS: ")
        self.detail_label_9.grid(column=0,row=8,sticky='e')
        self.detail_label_10=ttk.Label( self.frame_left_lower,text="Code Design Factor, F: ")
        self.detail_label_10.grid(column=0,row=9,sticky='e')
        self.detail_label_11=ttk.Label( self.frame_left_lower,text="Location Factor, L: ")
        self.detail_label_11.grid(column=0,row=10,sticky='e')
        self.detail_label_12=ttk.Label( self.frame_left_lower,text="Joint Factor, L: ")
        self.detail_label_12.grid(column=0,row=11,sticky='e')
        self.detail_label_13=ttk.Label( self.frame_left_lower,text="Temperature Factor, T: ")
        self.detail_label_13.grid(column=0,row=12,sticky='e')
        self.detail_label_14=ttk.Label( self.frame_left_lower,text="License Pressure (kPa): ")
        self.detail_label_14.grid(column=0,row=13,sticky='e')
        self.detail_label_15=ttk.Label( self.frame_left_lower,text="Normal Operating Pressure (kPa): ")
        self.detail_label_15.grid(column=0,row=14,sticky='e')
        self.detail_label_16=ttk.Label( self.frame_left_lower,text="Maximum Possible Pressure (kPa): ")
        self.detail_label_16.grid(column=0,row=15,sticky='e')
        
        # Column 2 User Input for Pipeline Static Design Details
        self.detail_label_2_input=ttk.Entry(self.frame_left_upper)
        self.detail_label_2_input.grid(column=1,row=1)
        self.detail_label_3_input=ttk.Entry(self.frame_left_upper)
        self.detail_label_3_input.grid(column=1,row=2)
        self.detail_label_4_input=ttk.Entry(self.frame_left_upper)
        self.detail_label_4_input.grid(column=1,row=3)
        self.detail_label_5_input=ttk.Entry( self.frame_left_lower)
        self.detail_label_5_input.grid(column=1,row=4)
        self.detail_label_6_input=ttk.Entry( self.frame_left_lower)
        self.detail_label_6_input.grid(column=1,row=5)
        self.detail_label_7_input=ttk.Entry( self.frame_left_lower)
        self.detail_label_7_input.grid(column=1,row=6)
        self.detail_label_8_input=ttk.Entry( self.frame_left_lower)
        self.detail_label_8_input.grid(column=1,row=7)
        self.detail_label_9_input=ttk.Entry( self.frame_left_lower)
        self.detail_label_9_input.grid(column=1,row=8)
        self.detail_label_10_input=ttk.Entry( self.frame_left_lower)
        self.detail_label_10_input.grid(column=1,row=9)
        self.detail_label_11_input=ttk.Entry( self.frame_left_lower)
        self.detail_label_11_input.grid(column=1,row=10)
        self.detail_label_12_input=ttk.Entry( self.frame_left_lower)
        self.detail_label_12_input.grid(column=1,row=11)
        self.detail_label_13_input=ttk.Entry( self.frame_left_lower)
        self.detail_label_13_input.grid(column=1,row=12)
        self.detail_label_14_input=ttk.Entry( self.frame_left_lower)
        self.detail_label_14_input.grid(column=1,row=13)
        self.detail_label_15_input=ttk.Entry( self.frame_left_lower)
        self.detail_label_15_input.grid(column=1,row=14)
        self.detail_label_16_input=ttk.Entry( self.frame_left_lower)
        self.detail_label_16_input.grid(column=1,row=15)




        # Column 3 PL 100 Data (Labels)
        self.detail_label_17=ttk.Label(self.frame_middle,text="PL 100 Data",background="white", font="10")
        self.detail_label_17.grid(column=3,row=4,columnspan=2)
        self.detail_label_18=ttk.Label(self.frame_middle,text="Substance: ")
        self.detail_label_18.grid(column=3,row=5,sticky='e')
        self.detail_label_19=ttk.Label(self.frame_middle,text="To: ")
        self.detail_label_19.grid(column=3,row=6,sticky='e')
        self.detail_label_20=ttk.Label(self.frame_middle,text="From: ")
        self.detail_label_20.grid(column=3,row=7,sticky='e')
        self.detail_label_21=ttk.Label(self.frame_middle,text="Length (km): ")
        self.detail_label_21.grid(column=3,row=8,sticky='e')
        self.detail_label_22=ttk.Label(self.frame_middle,text="Material: ")
        self.detail_label_22.grid(column=3,row=9,sticky='e')
        self.detail_label_23=ttk.Label(self.frame_middle,text="Material Type: ")
        self.detail_label_23.grid(column=3,row=10,sticky='e')
        self.detail_label_24=ttk.Label(self.frame_middle,text="Grade: ")
        self.detail_label_24.grid(column=3,row=11,sticky='e')
        self.detail_label_25=ttk.Label(self.frame_middle,text="Stress: ")
        self.detail_label_25.grid(column=3,row=12,sticky='e')
        self.detail_label_26=ttk.Label(self.frame_middle,text="MOP: ")
        self.detail_label_26.grid(column=3,row=13,sticky='e')
        self.detail_label_27=ttk.Label(self.frame_middle,text="H2S: ")
        self.detail_label_27.grid(column=3,row=14,sticky='e')
        self.detail_label_28=ttk.Label(self.frame_middle,text="Age: ")
        self.detail_label_28.grid(column=3,row=15,sticky='e')

        # Column 4 User Input for PL 100 Data 
        self.detail_label_18_input=ttk.Entry(self.frame_middle)
        self.detail_label_18_input.grid(column=4,row=5)
        self.detail_label_19_input=ttk.Entry(self.frame_middle)
        self.detail_label_19_input.grid(column=4,row=6)
        self.detail_label_20_input=ttk.Entry(self.frame_middle)
        self.detail_label_20_input.grid(column=4,row=7)
        self.detail_label_21_input=ttk.Entry(self.frame_middle)
        self.detail_label_21_input.grid(column=4,row=8)
        self.detail_label_22_input=ttk.Entry(self.frame_middle)
        self.detail_label_22_input.grid(column=4,row=9)
        self.detail_label_23_input=ttk.Entry(self.frame_middle)
        self.detail_label_23_input.grid(column=4,row=10)
        self.detail_label_24_input=ttk.Entry(self.frame_middle)
        self.detail_label_24_input.grid(column=4,row=11)
        self.detail_label_25_input=ttk.Entry(self.frame_middle)
        self.detail_label_25_input.grid(column=4,row=12)
        self.detail_label_26_input=ttk.Entry(self.frame_middle)
        self.detail_label_26_input.grid(column=4,row=13)
        self.detail_label_27_input=ttk.Entry(self.frame_middle)
        self.detail_label_27_input.grid(column=4,row=14)
        self.detail_label_28_input=ttk.Entry(self.frame_middle)
        self.detail_label_28_input.grid(column=4,row=15)

        #Column 5 Env Factors (Labels)
        self.detail_label_29=ttk.Label(self.frame_right,text="Env Factors")
        self.detail_label_29.grid(column=5,row=4,sticky='e',columnspan=2)
        self.detail_label_30=ttk.Label(self.frame_right,text="Cased Crossings: ")
        self.detail_label_30.grid(column=5,row=5,sticky='e')
        self.detail_label_31=ttk.Label(self.frame_right,text="Road Crossings: ")
        self.detail_label_31.grid(column=5,row=6,sticky='e')
        self.detail_label_32=ttk.Label(self.frame_right,text="Railway Crossings: ")
        self.detail_label_32.grid(column=5,row=7,sticky='e')
        self.detail_label_33=ttk.Label(self.frame_right,text="Station Crossings: ")
        self.detail_label_33.grid(column=5,row=8,sticky='e')
        self.detail_label_34=ttk.Label(self.frame_right,text="Other Crossings: ")
        self.detail_label_34.grid(column=5,row=9,sticky='e')
        self.detail_label_35=ttk.Label(self.frame_right,text="Substance Class: ")
        self.detail_label_35.grid(column=5,row=10,sticky='e')
        self.detail_label_36=ttk.Label(self.frame_right,text="Pipeline Class: ")
        self.detail_label_36.grid(column=5,row=11,sticky='e')
        self.detail_label_37=ttk.Label(self.frame_right,text="Seam Type: ")
        self.detail_label_37.grid(column=5,row=12,sticky='e')
        
        #Column 6 User Input for Env Factors
        self.detail_label_29_input=ttk.Combobox(self.frame_right,value=["Yes","No"])
        self.detail_label_29_input.current(0)
        self.detail_label_29_input.bind("<<ComboboxSelected>>")
        self.detail_label_29_input.grid(column=6,row=5)
        self.detail_label_30_input=ttk.Combobox(self.frame_right,value=["Yes","No"])
        self.detail_label_30_input.grid(column=6,row=6)
        self.detail_label_31_input=ttk.Combobox(self.frame_right,value=["Yes","No"])
        self.detail_label_31_input.grid(column=6,row=7)
        self.detail_label_32_input=ttk.Combobox(self.frame_right,value=["Yes","No"])
        self.detail_label_32_input.grid(column=6,row=8)
        self.detail_label_33_input=ttk.Combobox(self.frame_right,value=["Yes","No"])
        self.detail_label_33_input.grid(column=6,row=9)
        self.detail_label_34_input=ttk.Combobox(self.frame_right,value=["Gas","Multiphase"])
        self.detail_label_34_input.grid(column=6,row=10)
        self.detail_label_35_input=ttk.Combobox(self.frame_right,value=["None","10 or fewer dwelling units","11 to 46 dwellings","46 or more dwelling units","prevelance of buildings intended for oiccupancy with 4 or more stories"])
        self.detail_label_35_input.grid(column=6,row=11)
        self.detail_label_36_input=ttk.Combobox(self.frame_right,value=["Seamless","Electric Welder","Submerged Arc Welded","Continuous Weld"])
        self.detail_label_36_input.grid(column=6,row=12)


    
    # Pull ComboBox selection and send to excel sorting. Chance window for display.
    def callbackFunc(self):
        self.vendor=self.vendorDropDown.get()
        getExcel.vendorCheck(self.vendor, self.file)
        self.pipeline_Detail_Screen(self)


    # Get File Path From User
    def pullfile(self):
        self.file=getExcel.importILIData()

    # Delete current screen widgets
    def gui_elements_remove(self,elements):
        for element in elements:
            element.destroy()



def main():
    global root

    root=Tk()
    root.geometry("1000x1000")
    window=MainWindow(root)
    
    root.mainloop()


if __name__ == '__main__':
    main()
 

