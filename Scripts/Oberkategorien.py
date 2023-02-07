#%%
import pandas as pd
import os

# create an empty list (for all Kategorien and their Oberkategorie)
all_categories = {"topcategory": [], "category":[]}


#%%
# Path to the folder containing all the files
directory = '/Users/liane/Documents/GitHub/La_Bonne_Fortune/Data/Oberkategorien'

# Get all the file names from the directory
files = os.listdir(directory)

for file in files:
    #open file
    data = pd.read_excel(directory + "/" + file)

    #append all categories
    for category in data.Kategorie.unique().tolist():
        all_categories['topcategory'].append(file.strip(".xlsx"))
        all_categories['category'].append(category)

#%%
all_categories_df = pd.DataFrame(all_categories)
# %%

#save categories and topcategories
all_categories_df.to_csv("/Users/liane/Documents/GitHub/La_Bonne_Fortune/Data/Oberkategorien.csv",index=False)

