# Importing the necessary libraries and modules
from PIL import Image
import os
from tkinter import filedialog, Tk, Button, Label, Frame

def get_directory_path():
    directorypath = filedialog.askdirectory()

    return directorypath

def compress_image():
    # getting the directory path
    path = get_directory_path()

    # getting the files list
    filenames = os.listdir(path)

    for filename in filenames:
        name, extension = os.path.splitext(path + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(path + "/" + filename)
            picture.save(path + "compressed_" + filename,
                         optimize = True,
                         quality = 60)
            
    print("Done, compressed images")

def script_gui():

    # setting the GUI main window
    window = Tk()
    window.geometry("400x100")
    window.title("Compress Image")

    # GUI widgets
    frame = Frame(window)
    frame.pack(expand = True, fill = "both", padx = 10, pady = 10)
    
    label1 = Label(frame, text = "Select a directory")
    label1.pack(side = "left", expand = True, fill = "both")

    run = Button(frame, text = "Run", command = compress_image)
    run.pack(side = "left", expand = True, fill = "both")
    
    # run the GUI
    window.mainloop()

if __name__ == "__main__":
    script_gui()