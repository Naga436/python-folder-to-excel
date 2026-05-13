import os
import pandas as pd

def formate_size(size):
    if size < 1024:
        return f"{size} B"
    elif size < 1024 * 1024:
        return f"{round(size / 1024, 2)} KB"
    else:
        return f"{round(size / 1024 * 1024)} KB"

base_folder = "data"
rows = []

for folder_name in os.listdir(base_folder):
    folder_path = os.path.join(base_folder, folder_name)

    if os.path.isdir(folder_path):
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            file_name, extension = os.path.splitext(file)
            file_size = os.path.getsize(file_path)
            formatted_size = formate_size(file_size)

            if extension.lower() in [".jpg", ".txt"]:

                rows.append({
                    "Category": folder_name,
                    "File": file_name,
                    "Extension": extension,
                    "File Size": formatted_size
                    })
total_files = len(rows)

df = pd.DataFrame(rows)

df.to_excel("output/output.xlsx", index = False)

print("Excel File Created successfully!")
print(f"Total files processed: {total_files}")
