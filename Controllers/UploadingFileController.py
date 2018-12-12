from Models.Fixer import Fixer
from Controllers.FiltersController import *
from Views.Views import *
from tkinter import *
from tkinter import filedialog

class UpdateData:

    def __init__(self):
        print("Start UpdateData")

    def choose_path(self):
        # TODO: check if the file is CSV
        main_win.source_path_file = filedialog.askopenfilename(parent=main_win, initialdir="/",
                                                         title='Please select a CSV file')


    def choose_picture(self):
        # TODO: check if the file is picture
        main_win.source_picture_file = filedialog.askopenfilename(parent=main_win, initialdir="/",
                                                             title='Please select a Picture')

    # Send new file to the models Receive
    def build_data_base_controller(self):
        # TODO: send file to the models to build the needed CSV OR Data Base
        # ToDO: receive data after all the changes,
        # GO TO MODELS TO PROCESS THE FILE
        filters = build_filters_gui()
        process_filters_controller(filters)


    # Get the file link from the user
    # Arrange unneeded data
    # Send new file to the connector with the data base
    def get_file_from_user(self):
        # TODO: delete all the ERROR DATA
        # TODO: delete unneeded columns
        f = Fixer()
        new_file = f.fix_file(main_win.source_path_file) # get from the file a new file
        self.build_data_base_controller()


    # Building the first Gui
    # That includes the uploading
    # CSV file to the project
    def building_upload_gui(self):
        global main_win
        main_win = Tk()
        main_win.geometry("500x500")
        main_win.source_path_file = ''
        main_win.source_picture_file = ''
        b_choose_path = Button(main_win, text="Chose Path File", width=20, height=3, command=self.choose_path)
        b_choose_path.place(x=100, y=50)
        b_choose_path.width = 100
        b_choose_picture = Button(main_win, text="Chose Picture", width=20, height=3, command=self.choose_picture)
        b_choose_picture.place(x=100, y=150)
        b_choose_picture.width = 100
        lbl1= Label(main_win, text="Hello!!")
        lbl1.grid(column=0, row=0)
        MyButton1 = Button(main_win, text="Submit", width=10, command=self.get_file_from_user)
        MyButton1.place(x=400, y=400)
        show_uploading_gui(main_win)


