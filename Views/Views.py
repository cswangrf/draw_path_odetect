from Controllers.UploadingFile import *

# show the gui to the user and get
# the link of the file
def show_gui(window):
    window.mainloop()
    # TODO: get the file link from the user
    file = r'C:\Users\RENT\Desktop\paths-project\data'
    get_file(file)
