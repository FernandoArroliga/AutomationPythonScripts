"""

This python script allow you to move several files from folder one to another
folder

Author: @FernandoArroliga
Creation Date: 17/07/2023
"""

# Importing the modules and libraries
import os

# Defining the directories
source_directory = "C:/Users/PC 01/Desktop/Python_practica/Automatization/Image_compressor/files"
destination_directory = "C:/Users/PC 01/Pictures"

def file_mover(source, destiny):

    # getting the file names
    file_names = os.listdir(source)
    for file_name in file_names:
        name, extension = os.path.splitext(file_name)

        if extension in [".jpg", ".jpeg", ".png"]:
            path_source = os.path.join(source, file_name)
            path_destiny = os.path.join(destiny, file_name)

            # moving and replacing the files
            os.replace(path_source, path_destiny)
    return None

# Runing the main file        
if __name__ == "__main__":
    file_mover(source_directory, destination_directory)
    print("Done!\nFiles moved successfully")


