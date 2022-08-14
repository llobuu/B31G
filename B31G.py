from tkinter import *
from tkinter import ttk
import getExcel



class MainWindow:
    def __init__(self, master):     #you can use something other than 'master' if you'd like.
        self.main_frame=Frame(master)
        self.main_frame.grid(row=0,column=0)
        #self.some_kind_of_controlled=0
        self.upload_Screen()
# Screen #1
    def upload_Screen(self):   
        root.title("Vendor Data Screen")


        #self.frame1=Frame(bg='white')
        #self.frame1.grid(column=0,row=0,columnspan=2,rowspan=3)

        # DropDown list for ComboBox
        self.vendorDropDown=ttk.Combobox(value=["Test","Onstream","Encompass","Rosen"])
        self.vendorDropDown.current(0)
        self.vendorDropDown.bind("<<ComboboxSelected>>")
        self.vendorDropDown.grid(row=0, column=0)

        # File Path Button
        self.upload=Button(text = "Upload File", command = self.pullfile)
        self.upload.grid(row=1,column=1)
        
        # Submit Button
        self.review=Button(text="Submit", command=self.callbackFunc)
        self.review.grid(row=2,column=2)

        self.gui_elements=[self.vendorDropDown,
                           self.upload,
                           self.review]
# Screen #2
    def pipeline_Detail_Screen(self,event):
        self.gui_elements_remove(self.gui_elements)

        root.title("Pipeline Specific Data")



        # Column 1 Pipeline Static Design Details (Labels)
        self.detail_label_1=ttk.Label(self.main_frame,text="Pipeline Identification",background="white", font="10")
        self.detail_label_1.grid(column=0,row=0,columnspan=2)
        self.detail_label_2=ttk.Label(self.main_frame,text="Client: ")
        self.detail_label_2.grid(column=0,row=1,sticky='e')
        self.detail_label_3=ttk.Label(self.main_frame,text="Pipeline License Number: ")
        self.detail_label_3.grid(column=0,row=2,sticky='e')
        self.detail_label_4=ttk.Label(self.main_frame,text="Inspection Date: ")
        self.detail_label_4.grid(column=0,row=3,sticky='e')
        self.detail_label_5=ttk.Label(self.main_frame,text="Pipeline Static Design Details",background="white", font="10")
        self.detail_label_5.grid(column=0,row=4,sticky='e',columnspan=2)
        self.detail_label_6=ttk.Label(self.main_frame,text="Nominal OD: ")
        self.detail_label_6.grid(column=0,row=5,sticky='e')
        self.detail_label_7=ttk.Label(self.main_frame,text="Nominal Wall Thickness (WT): ")
        self.detail_label_7.grid(column=0,row=6,sticky='e')
        self.detail_label_8=ttk.Label(self.main_frame,text="Corrosion/Inspection Allowance: ")
        self.detail_label_8.grid(column=0,row=7,sticky='e')
        self.detail_label_9=ttk.Label(self.main_frame,text="SMYS: ")
        self.detail_label_9.grid(column=0,row=8,sticky='e')
        self.detail_label_10=ttk.Label(self.main_frame,text="Code Design Factor, F: ")
        self.detail_label_10.grid(column=0,row=9,sticky='e')
        self.detail_label_11=ttk.Label(self.main_frame,text="Location Factor, L: ")
        self.detail_label_11.grid(column=0,row=10,sticky='e')
        self.detail_label_12=ttk.Label(self.main_frame,text="Joint Factor, L: ")
        self.detail_label_12.grid(column=0,row=11,sticky='e')
        self.detail_label_13=ttk.Label(self.main_frame,text="Temperature Factor, T: ")
        self.detail_label_13.grid(column=0,row=12,sticky='e')
        self.detail_label_14=ttk.Label(self.main_frame,text="License Pressure (kPa): ")
        self.detail_label_14.grid(column=0,row=13,sticky='e')
        self.detail_label_15=ttk.Label(self.main_frame,text="Normal Operating Pressure (kPa): ")
        self.detail_label_15.grid(column=0,row=14,sticky='e')
        self.detail_label_16=ttk.Label(self.main_frame,text="Maximum Possible Pressure (kPa): ")
        self.detail_label_16.grid(column=0,row=15,sticky='e')
        
        # Column 2 User Input for Pipeline Static Design Details
        self.detail_label_2_input=ttk.Entry(self.main_frame)
        self.detail_label_2_input.grid(column=1,row=1)
        self.detail_label_3_input=ttk.Entry(self.main_frame)
        self.detail_label_3_input.grid(column=1,row=2)
        self.detail_label_4_input=ttk.Entry(self.main_frame)
        self.detail_label_4_input.grid(column=1,row=3)
        self.detail_label_5_input=ttk.Entry(self.main_frame)
        self.detail_label_5_input.grid(column=1,row=4)
        self.detail_label_6_input=ttk.Entry(self.main_frame)
        self.detail_label_6_input.grid(column=1,row=5)
        self.detail_label_7_input=ttk.Entry(self.main_frame)
        self.detail_label_7_input.grid(column=1,row=6)
        self.detail_label_8_input=ttk.Entry(self.main_frame)
        self.detail_label_8_input.grid(column=1,row=7)
        self.detail_label_9_input=ttk.Entry(self.main_frame)
        self.detail_label_9_input.grid(column=1,row=8)
        self.detail_label_10_input=ttk.Entry(self.main_frame)
        self.detail_label_10_input.grid(column=1,row=9)
        self.detail_label_11_input=ttk.Entry(self.main_frame)
        self.detail_label_11_input.grid(column=1,row=10)
        self.detail_label_12_input=ttk.Entry(self.main_frame)
        self.detail_label_12_input.grid(column=1,row=11)
        self.detail_label_13_input=ttk.Entry(self.main_frame)
        self.detail_label_13_input.grid(column=1,row=12)
        self.detail_label_14_input=ttk.Entry(self.main_frame)
        self.detail_label_14_input.grid(column=1,row=13)
        self.detail_label_15_input=ttk.Entry(self.main_frame)
        self.detail_label_15_input.grid(column=1,row=14)
        self.detail_label_16_input=ttk.Entry(self.main_frame)
        self.detail_label_16_input.grid(column=1,row=15)




        # Column 3 PL 100 Data (Labels)
        self.detail_label_17=ttk.Label(self.main_frame,text="PL 100 Data",background="white", font="10")
        self.detail_label_17.grid(column=3,row=4,columnspan=2)
        self.detail_label_18=ttk.Label(self.main_frame,text="Substance: ")
        self.detail_label_18.grid(column=3,row=5,sticky='e')
        self.detail_label_19=ttk.Label(self.main_frame,text="To: ")
        self.detail_label_19.grid(column=3,row=6,sticky='e')
        self.detail_label_20=ttk.Label(self.main_frame,text="From: ")
        self.detail_label_20.grid(column=3,row=7,sticky='e')
        self.detail_label_21=ttk.Label(self.main_frame,text="Length (km): ")
        self.detail_label_21.grid(column=3,row=8,sticky='e')
        self.detail_label_22=ttk.Label(self.main_frame,text="Material: ")
        self.detail_label_22.grid(column=3,row=9,sticky='e')
        self.detail_label_23=ttk.Label(self.main_frame,text="Material Type: ")
        self.detail_label_23.grid(column=3,row=10,sticky='e')
        self.detail_label_24=ttk.Label(self.main_frame,text="Grade: ")
        self.detail_label_24.grid(column=3,row=11,sticky='e')
        self.detail_label_25=ttk.Label(self.main_frame,text="Stress: ")
        self.detail_label_25.grid(column=3,row=12,sticky='e')
        self.detail_label_26=ttk.Label(self.main_frame,text="MOP: ")
        self.detail_label_26.grid(column=3,row=13,sticky='e')
        self.detail_label_27=ttk.Label(self.main_frame,text="H2S: ")
        self.detail_label_27.grid(column=3,row=14,sticky='e')
        self.detail_label_28=ttk.Label(self.main_frame,text="Age: ")
        self.detail_label_28.grid(column=3,row=15,sticky='e')

        # Column 4 User Input for PL 100 Data 
        self.detail_label_18_input=ttk.Entry(self.main_frame)
        self.detail_label_18_input.grid(column=4,row=5)
        self.detail_label_19_input=ttk.Entry(self.main_frame)
        self.detail_label_19_input.grid(column=4,row=6)
        self.detail_label_20_input=ttk.Entry(self.main_frame)
        self.detail_label_20_input.grid(column=4,row=7)
        self.detail_label_21_input=ttk.Entry(self.main_frame)
        self.detail_label_21_input.grid(column=4,row=8)
        self.detail_label_22_input=ttk.Entry(self.main_frame)
        self.detail_label_22_input.grid(column=4,row=9)
        self.detail_label_23_input=ttk.Entry(self.main_frame)
        self.detail_label_23_input.grid(column=4,row=10)
        self.detail_label_24_input=ttk.Entry(self.main_frame)
        self.detail_label_24_input.grid(column=4,row=11)
        self.detail_label_25_input=ttk.Entry(self.main_frame)
        self.detail_label_25_input.grid(column=4,row=12)
        self.detail_label_26_input=ttk.Entry(self.main_frame)
        self.detail_label_26_input.grid(column=4,row=13)
        self.detail_label_27_input=ttk.Entry(self.main_frame)
        self.detail_label_27_input.grid(column=4,row=14)
        self.detail_label_28_input=ttk.Entry(self.main_frame)
        self.detail_label_28_input.grid(column=4,row=15)

        #Column 5 Env Factors (Labels)
        self.detail_label_29=ttk.Label(self.main_frame,text="Env Factors")
        self.detail_label_29.grid(column=5,row=4,sticky='e',columnspan=2)
        self.detail_label_30=ttk.Label(self.main_frame,text="Cased Crossings: ")
        self.detail_label_30.grid(column=5,row=5,sticky='e')
        self.detail_label_31=ttk.Label(self.main_frame,text="Road Crossings: ")
        self.detail_label_31.grid(column=5,row=6,sticky='e')
        self.detail_label_32=ttk.Label(self.main_frame,text="Railway Crossings: ")
        self.detail_label_32.grid(column=5,row=7,sticky='e')
        self.detail_label_33=ttk.Label(self.main_frame,text="Station Crossings: ")
        self.detail_label_33.grid(column=5,row=8,sticky='e')
        self.detail_label_34=ttk.Label(self.main_frame,text="Other Crossings: ")
        self.detail_label_34.grid(column=5,row=9,sticky='e')
        self.detail_label_35=ttk.Label(self.main_frame,text="Substance Class: ")
        self.detail_label_35.grid(column=5,row=10,sticky='e')
        self.detail_label_36=ttk.Label(self.main_frame,text="Pipeline Class: ")
        self.detail_label_36.grid(column=5,row=11,sticky='e')
        self.detail_label_37=ttk.Label(self.main_frame,text="Seam Type: ")
        self.detail_label_37.grid(column=5,row=12,sticky='e')
        
        #Column 6 User Input for Env Factors
        self.detail_label_29_input=ttk.Combobox(value=["Yes","No"])
        self.detail_label_29_input.grid(column=6,row=5)
        self.detail_label_30_input=ttk.Combobox(value=["Yes","No"])
        self.detail_label_30_input.grid(column=6,row=6)
        self.detail_label_31_input=ttk.Combobox(value=["Yes","No"])
        self.detail_label_31_input.grid(column=6,row=7)
        self.detail_label_32_input=ttk.Combobox(value=["Yes","No"])
        self.detail_label_32_input.grid(column=6,row=8)
        self.detail_label_33_input=ttk.Combobox(value=["Yes","No"])
        self.detail_label_33_input.grid(column=6,row=9)
        self.detail_label_34_input=ttk.Combobox(value=["Gas","Multiphase"])
        self.detail_label_34_input.grid(column=6,row=10)
        self.detail_label_35_input=ttk.Combobox(value=["None","10 or fewer dwelling units","11 to 46 dwellings","46 or more dwelling units","prevelance of buildings intended for oiccupancy with 4 or more stories"])
        self.detail_label_35_input.grid(column=6,row=11)
        self.detail_label_36_input=ttk.Combobox(value=["Seamless","Electric Welder","Submerged Arc Welded","Continuous Weld"])
        self.detail_label_36_input.grid(column=6,row=12)


    
    # Pull ComboBox selection and send to excel sorting. Chance window for display.
    def callbackFunc(self):
        self.vendor=self.vendorDropDown.get()
        getExcel.vendorCheck(self.vendor, self.file)
        self.pipeline_Detail_Screen(self)


    # Get File Path From User
    def pullfile(self):
        self.file=getExcel.importILIData()


    def gui_elements_remove(self,elements):
        for element in elements:
            element.destroy()



def main():
    global root

    root=Tk()
    root.geometry("1200x800")
    window=MainWindow(root)
    
    root.mainloop()


if __name__ == '__main__':
    main()
 

