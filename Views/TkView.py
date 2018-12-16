import threading
from Views import pyQt5View
from Models.Fixer import Fixer
from tkinter import *
from tkinter import filedialog, ttk
from settings import im


def show_uploading_gui(window):
    window.mainloop()
    print(window.source_picture_file, window.source_path_file)


class Userinterface:

    def __init__(self, controller):
        self.controller = controller
        print("Userinterface")
        self.building_upload_gui()

    def choose_path(self):
        main_win.source_path_file = filedialog.askopenfilename(parent=main_win, initialdir="/",
                                                               title='Please select a CSV file',
                                                               filetypes=(
                                                               ("csv files", "*.csv"), ("all files", "*.xlsx")))

    def choose_picture(self):
        main_win.source_picture_file = filedialog.askopenfilename(parent=main_win, initialdir="/",
                                                                  title='Please select a Picture',
                                                                  filetypes=(
                                                                  ("jpeg files", "*.jpg"), ("png files", "*.png")))

    # Send new file to the models Receive
    def build_data_base_controller(self):
        # TODO: send file to the models to build the needed CSV OR Data Base
        # ToDO: receive data after all the changes,
        main_win.destroy()
        pyQt5View.start()

    def get_file_from_user(self):
        im.set_img(main_win.source_picture_file)
        progress = ttk.Progressbar(main_win, length=500)
        progress.place(x=0, y=350)
        im.set_img(main_win.source_picture_file)
        if main_win.source_path_file != "":
            n = Fixer(main_win.source_path_file)
            f = threading.Thread(target=n.fix_file)
            f.start()
            while f.is_alive():
                progress['value'] += 0.0004
                main_win.update()
            progress['value'] = 100
        self.build_data_base_controller()

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
        lbl1 = Label(main_win, text="Hello!!")
        lbl1.grid(column=0, row=0)
        MyButton1 = Button(main_win, text="Submit", width=10, command=self.get_file_from_user)
        MyButton2 = Button(main_win, text="Lastfile", width=10, command=self.build_data_base_controller)
        MyButton1.place(x=400, y=400)
        MyButton2.place(x=400, y=350)
        show_uploading_gui(main_win)
