import threading

import cv2


from Views.Views import *
from tkinter import *
from Models.Filters import Filter
from PIL import ImageTk,Image
class Filters:
    # TODO: build class that get the filters data from the user
    # TODO: and send them back to UploadingFileController
    pass



# add paths to the gui, show them in table or in the picture
def add_paths_to_gui(needed_paths):
    # TODO: add paths to the gui
    # add them to the window
    # TODO: send new window to the view
    new_filters = "fsdfsdfdsfs"
    # ned to think how to get and send te same gui this is not working right
    show_filters_gui(my_window, new_filters)


# building gui that present the filters options to the user
# and build filter class that includes all of
# the filters and send them back to the data
def build_filters_gui():
    # TODO: build GUI interface get the filters from user,
    # TODO: send him back to the models to process them

    # f = threading.Thread(target=Filter)
    # f.start()
    # mg = f.join()
    # f.locate_time("11:00:00", "11:03:00")
    mg = Filter()
    window = Tk()
    window.title("Welcome to LikeGeeks app")
    window.geometry('1000x700')
    img = cv2.imread('../paths0.png')
    b, g, r = cv2.split(img)
    img = cv2.merge((r, g, b))
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)
    imAg = Label(window, image=imgtk)
    imAg.place(x=250,y=0)
    lbl = Label(window, text="Hello")
    lbl.grid(column=0, row=0)



    btn1 = Button(window, text="Click Me")
    btn2 = Button(window, text="Click Me")
    btn3 = Button(window, text="Click Me")
    btn4 = Button(window, text="Click Me")
    btn1.place(x=250, y=300)
    btn2.place(x=250, y=350)
    btn3.place(x=250, y=400)
    btn4.place(x=250, y=450)
    window.mainloop()
    filters = show_filters_gui(window)
    global my_window
    my_window = window
    return filters


# send filters to the models,
def process_filters_controller(needed_file):
    # TODO: send filters to the models,
    # TODO: get the requested paths
    # TODO: and send them to the GUI builder
    # GO TO MODELS TO PROCESS THE Filter
    needed_paths = needed_file
    add_paths_to_gui(needed_paths)