import os

from FileArrangement import FA
from FileArrangement.FA import file_automation


def main():
    folder_path=input("Please enter the folder path: ")
    if not os.path.isabs(folder_path):
        current_directory=os.getcwd()
        folder_path=os.path.join(current_directory,folder_path)


    file_automation(folder_path)

if __name__ == "__main__":
    main()