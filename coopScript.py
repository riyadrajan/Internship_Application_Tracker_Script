import os
import pandas as pd

base_path = "OneDrive/Concordia/Co-Op"
entries = []

#getting data from the base path (company names, then application ID)

for company in os.listdir(base_path):
    #path for each company
    company_path = os.path.join(base_path, company)
    if os.path.isdir(company_path):
        for app in os.listdir(company_path):
            #create path for each application
            app_path = os.path.join(company_path, app)
            if os.path.isdir(app_path):
                #dictionary cast as set to remove duplicates
                entries.append({
                    "Company Name": company,
                    "Application": app,
                    "Status": None
                })

    

        
#use pandas to create the dataframe
df = pd.DataFrame(entries)

#now export to excel
output_path = "/Users/riyadrajan/Desktop/coopTracker.xlsx"
# if os.path.isdir(output_path):
df.to_excel(output_path, index=False)

print(f"Tracker saved to: {output_path}")



