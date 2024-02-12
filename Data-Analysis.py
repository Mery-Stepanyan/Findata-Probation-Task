import csv
import pandas as pd
import re

 
def read_csv_(filename):
    data = {}
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if not row[1].startswith("$"): 
                continue
            else: data[row[0]]=float(re.sub(r'[$,]', '',row[1]) )
    return data

def diff_quarter1_quarter2(data1, data2):
    
    result = {}
    for row1, row2 in zip(data1, data2):
        result[row1]= "${:,.1f}".format(data2[row2]-data1[row2])
    return result

def result_data_to_csv(result_data):
    fieldnames = result_data.keys()
    csv_filename = "output.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(result_data)
    result=pd.read_csv("output.csv")
    print(result)
    
comp_name=input("Please enter the company name (CompanyA or CompanyB) " )
if comp_name=="CompanyA":
  
    with open('CompanyA_Quarter1.txt') as quarter_1,open ('CompanyA_Quarter2.txt') as quarter_2:
        with open('CompanyA_Quarter1.csv', 'w', newline='') as quarter1_csv, open ('CompanyA_Quarter2.csv', 'w', newline='') as quarter2_csv:
            csv_writer_q1 = csv.writer(quarter1_csv)
            csv_writer_q2 = csv.writer(quarter2_csv)
            for line_q1 in quarter_1:
                fields_q1 = line_q1.strip().split()  
                csv_writer_q1.writerow(fields_q1)
                
            for line_q2 in quarter_2:
                fields_q2 = line_q2.strip().split()  
                csv_writer_q2.writerow(fields_q2)   

    df_q1 = pd.read_csv('CompanyA_Quarter1.csv')
    df_q2 = pd.read_csv('CompanyA_Quarter2.csv')
    print("Company A Quarter 1:"); print(df_q1) 
    print("-----------------------------------")
    print("Company A Quarter 2:"); print(df_q2) 
    print("-------------------------------------------")
    data1=read_csv_('CompanyA_Quarter1.csv'); data2=read_csv_('CompanyA_Quarter2.csv')
   
    result_data = diff_quarter1_quarter2(data1, data2)
    
    print("Difference between Quarter 2 and Quarter 1") 
    print("-------------------------------------------")
    result_data_to_csv(result_data)

elif comp_name=="CompanyB":
  
    with open('CompanyB_Quarter1.txt') as quarter_1,open ('CompanyB_Quarter2.txt') as quarter_2:
        with open('CompanyB_Quarter1.csv', 'w', newline='') as quarter1_csv, open ('CompanyB_Quarter2.csv', 'w', newline='') as quarter2_csv:
            csv_writer_q1 = csv.writer(quarter1_csv)
            csv_writer_q2 = csv.writer(quarter2_csv)
            for line_q1 in quarter_1:
                fields_q1 = line_q1.strip().split()  
                csv_writer_q1.writerow(fields_q1)
                
            for line_q2 in quarter_2:
                fields_q2 = line_q2.strip().split()  
                csv_writer_q2.writerow(fields_q2)    
    df_q1 = pd.read_csv('CompanyB_Quarter1.csv')
    df_q2 = pd.read_csv('CompanyB_Quarter2.csv')
    print("Company B Quarter 1:"); print(df_q1) 
    print("-----------------------------------")
    print("Company B Quarter 2:"); print(df_q2) 
    print("-------------------------------------------")
    
    data1=read_csv_('CompanyB_Quarter1.csv'); data2=read_csv_('CompanyB_Quarter2.csv')
    result_data = diff_quarter1_quarter2(data1, data2)
    print("Difference between Quarter 2 and Quarter 1") 
    print("-------------------------------------------")
    result_data_to_csv(result_data) 

    
else :
    print("Incorrect name!!!")









