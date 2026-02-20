import os
import pandas as pd
from qr_generator import qr_generator

def generate_from_csv(csv_file):
    df=pd.read_csv(csv_file)
    #for making new Directories
    os.makedirs("output",exist_ok=True)
    #for Validating
    if 'name' not in df.columns or 'data' not in df.columns:
        print("the CSV file must be Contain the name and data column....")
        return
    for _,row in df.iterrows():
        file_name=f"output/{row['name']}.png"
        qr_generator(row['data'],file_name)

    print("All the QR are Generated......")

if __name__=="__main__":
    csv_file=input("enter the csv file name:")
    generate_from_csv(csv_file)