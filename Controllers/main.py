import Views.TkView as Gui


class Controls(object):
    def onclick(self):
        pass


def main():
    print("python main function")
    gui_controls = Controls()
    gui = Gui.Userinterface(gui_controls)


if __name__ == '__main__':
    main()
