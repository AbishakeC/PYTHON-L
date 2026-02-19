import os
import shutil

# For the folder name and seperation process
File_Types = {
    "Images":[".jpg",".jpeg",".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}


def file_automation(folder_path):
    # verifying whether the path exist or not
    if not os.path.exists(folder_path):
        print("\nEnter the correct path detail....")
        return

# To display the list of file name with Extension
    print("file inside the folder.")
    print("--------------------------")
    files = [f for f in os.listdir(folder_path)]
    print(files)

    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isdir(file_path):
            continue

        file_name,extention = os.path.splitext(file)
        print("-------------------------")
        print("FileName:",file_name)
        print("extention:",extention)

        for Folder_Name,extentions in File_Types.items():
            if extention.lower() in extentions:

                new_Folder_process= os.path.join(folder_path,Folder_Name)

                if not os.path.exists(new_Folder_process):
                    os.makedirs(new_Folder_process)

                shutil.move(file_path,os.path.join(new_Folder_process,file))

                print(f"moved:{file} to {Folder_Name}")
                break

