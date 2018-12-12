from Controllers.FiltersController import *
from Views.Views import *
from tkinter import *

# Send new file to the models Receive
def build_data_base_controller(file):
    # TODO: send file to the models to build the needed CSV OR Data Base
    # ToDO: receive data after all the changes,
    # GO TO MODELS TO PROCESS THE FILE
    needed_file = file
    filters = build_filters_gui()
    process_filters_controller(needed_file, filters)


# Get the file link from the user
# Arrange unneeded data
# Send new file to the connector with the data base
def get_file_from_user(file):
    # TODO: delete all the ERROR DATA
    # TODO: delete unneeded columns
    new_file = file # get from the file a new file
    print("kk")
    build_data_base_controller(new_file)


# Building the first Gui
# That includes the uploading
# CSV file to the project
def building_upload_gui():
    # TODO: building GUI
    window = Tk()
    window.title("Paths Project")
    lbl = Label(window, text="Hello")
    lbl.grid(column=0, row=0)
    file = show_uploading_gui(window)
    get_file_from_user(file)

