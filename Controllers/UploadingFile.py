from Controllers.FiltersController import *
from Views.Views import *

from tkinter import *


# Send new file to the models Receive
def build_data_base(file):
    # TODO: send file to the models to build the needed CSV OR Data Base
    # ToDO: receive data after all the changes,
    filters = build_filters_gui()


# Get the file link from the user
# Arrange unneeded data
# Send new file to the connector with the data base
def get_file(file):
    # TODO: delete all the ERROR DATA
    # TODO: delete unneeded columns
    new_file = file # get from the file a new file
    build_data_base(new_file)


# Building the first Gui
# That includes the uploading
# CSV file to the project
def building_upload_gui():
    # TODO: building GUI
    window = Tk()
    window.title("Paths Project")
    lbl = Label(window, text="Hello")
    lbl.grid(column=0, row=0)
    show_gui(window)