from view.gui_probleme import Gui_probleme

class App:
    def __init__(self,master):
        self.master = master
        self.probleme = Gui_probleme(self.master)

if __name__ == "__main__":
    from tkinter import Tk
    root = Tk()
    App(root)
    root.mainloop()
