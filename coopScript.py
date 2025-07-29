import os
import pandas as pd

base_path = "OneDrive/Concordia/Co-Op"
entries = [] 

df_existing = pd.read_excel("/Users/riyadrajan/Desktop/coopTracker.xlsx")


#getting data from the base path (company names, then application ID)

'''
implement search algorithm and append function since the data will be sorted in excel after
avoid looping through the entire df
unique identifier needed is the application ID
'''

existing_keys = set(zip(df_existing["Company Name"], df_existing["Application"]))

for company in os.listdir(base_path):
    #create path for each company
    company_path = os.path.join(base_path, company)
    if os.path.isdir(company_path):
        for app in os.listdir(company_path):
            #create path for each application
            app_path = os.path.join(company_path, app)
            if os.path.isdir(app_path):
                key = (company, app)
                if key not in existing_keys:
                    #list of dictionaries
                    entries.append({
                        "Company Name": company,
                        "Application": app,
                        "Status": "inactive"
                    })

    

        
#use pandas to create the dataframe of entries to add
df_new = pd.DataFrame(entries)

#add new df to old df
df_combined = pd.concat([df_existing, df_new], ignore_index=True)


#now export to excel
output_path = "/Users/riyadrajan/Desktop/coopTrackerCopy.xlsx"
# if os.path.isdir(output_path):
df_combined.to_excel(output_path, index=False)

print(f"Tracker saved to: {output_path}")



