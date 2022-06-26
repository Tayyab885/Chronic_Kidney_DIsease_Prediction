
# Importing the necessary Liberaries
import numpy as np
import pandas as pd


class DataCleaning:
    def __init__(self,data):
        self.data = data

    def columns_rename(self):
        self.data.drop('id',axis=1,inplace=True)
        columns_names=['Age (years)','Blood Pressure (mm/Hg)','Specific Gravity','Albumin','Sugar','Red Blood Cells',
                    'Pus Cells','Pus Cell Clumps','Bacteria','Blood Glucose Random (mgs/dL)','Blood Urea (mgs/dL)',
                    'Serum Creatinine (mgs/dL)','Sodium (mEq/L)','Potassium (mEq/L)','Hemoglobin (gms)','Packed Cell Volume',
                    'White Blood Cells (cells/cmm)','Red Blood Cells (millions/cmm)','Hypertension','Diabetes Mellitus',
                    'Coronary Artery Disease','Appetite','Pedal Edema','Anemia','Chronic Kidney Disease']
        self.data.columns=columns_names

    def wrong_datatypes(self):
        mis_dtyped=['Packed Cell Volume','White Blood Cells (cells/cmm)','Red Blood Cells (millions/cmm)']
        numeric=[]
        for i in self.data.columns:
            if self.data[i].dtype=='float64':
                numeric.append(i)
        numeric=numeric+mis_dtyped
        for col in mis_dtyped:
                self.data[col]=self.data[col].astype('float')

    def replace_values(self):
        self.data['Diabetes Mellitus'] = self.data['Diabetes Mellitus'].replace(to_replace= {
                '\tno': 'no', '\tyes': 'yes', ' yes': 'yes'})

        self.data["White Blood Cells (cells/cmm)"] = self.data["White Blood Cells (cells/cmm)"].replace(to_replace= {
                '\t?': np.nan, '\t8400': '8400' })

        self.data["Red Blood Cells (millions/cmm)"]   = self.data["Red Blood Cells (millions/cmm)"].replace(to_replace= {
                '\t?': np.nan})

        self.data['Coronary Artery Disease'] = self.data['Coronary Artery Disease'].replace(to_replace= {
                '\tno': 'no'})

        self.data["Packed Cell Volume"] = self.data["Packed Cell Volume"].replace(to_replace= {
                '\t?': np.nan})

    def categorcal_numerical(self):
        self.data['Red Blood Cells'] = self.data['Red Blood Cells'].replace(to_replace={"normal":0,"abnormal":1})
        self.data['Pus Cells'] = self.data['Pus Cells'].replace(to_replace={"normal":0 , "abnormal":1})
        self.data['Pus Cell Clumps'] = self.data['Pus Cell Clumps'].replace(to_replace = {'notpresent':0,'present':1})
        self.data["Bacteria"]= self.data["Bacteria"].replace(to_replace = {'notpresent':0,'present':1})
        self.data["Hypertension"] = self.data["Hypertension"].replace(to_replace = {'yes' : 1, 'no' : 0})
        self.data["Diabetes Mellitus"] = self.data["Diabetes Mellitus"].replace(to_replace={'yes' : 1, 'no' : 0})
        self.data["Coronary Artery Disease"] = self.data["Coronary Artery Disease"].replace(to_replace = {'yes' : 1, 'no' : 0})
        self.data["Appetite"] = self.data["Appetite"].replace(to_replace={'good':1,'poor':0})
        self.data["Pedal Edema"] = self.data["Pedal Edema"].replace(to_replace = {'yes' : 1, 'no' : 0})
        self.data["Anemia"] = self.data["Anemia"].replace(to_replace = {'yes' : 1, 'no' : 0})
        self.data["Chronic Kidney Disease"] = [1 if i == "ckd" else 0 for i in self.data["Chronic Kidney Disease"]]
    

    def nan_values(self):
        # Cheaking Missing (NaN) Values
        features = ['Age (years)','Blood Pressure (mm/Hg)','Specific Gravity','Albumin','Sugar','Red Blood Cells',
                    'Pus Cells','Pus Cell Clumps','Bacteria','Blood Glucose Random (mgs/dL)','Blood Urea (mgs/dL)',
                    'Serum Creatinine (mgs/dL)','Sodium (mEq/L)','Potassium (mEq/L)','Hemoglobin (gms)','Packed Cell Volume',
                    'White Blood Cells (cells/cmm)','Red Blood Cells (millions/cmm)','Hypertension','Diabetes Mellitus',
                    'Coronary Artery Disease','Appetite','Pedal Edema','Anemia']
        for feature in features:
            self.data[feature] = self.data[feature].fillna(self.data[feature].median())
    
    def save_cleaned_data(self):
        new_file_name = input("Enter the file name You want to Saved with: ")
        self.data.to_csv(f"CleanedData/{new_file_name}.csv")
        print("Your File has been Cleaned and saved in CleanedData folder.")


if __name__ == '__main__':
    df = pd.read_csv("Dataset/kidney_disease_train.csv")
    data_cleaning = DataCleaning(df)
    data_cleaning.columns_rename()
    data_cleaning.replace_values()
    data_cleaning.categorcal_numerical()
    data_cleaning.wrong_datatypes()
    data_cleaning.nan_values()
    data_cleaning.save_cleaned_data()

