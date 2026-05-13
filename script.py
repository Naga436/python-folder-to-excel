import os
import pandas as pd

base_folder = "data"
rows = []

for folder_name in os.listdir(base_folder):
    folder_path = os.path.join(base_folder, folder_name)

    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            file_name, extension = os.path.splitext(file)

            if extension.lower() in [".jpg", ".txt"]:

                rows.append({
                    "Category": folder_name,
                    "File": file_name,
                    "Extension": extension
                    })

df = pd.DataFrame(rows)

df.to_excel("output/output.xlsx", index = False)

print("Excel File Created successfully!")
