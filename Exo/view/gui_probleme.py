from tkinter import *

class Gui_probleme:
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.button = Button(self.frame, text="QUIT", fg="red", command=self.frame.quit)
        self.button.pack(side=LEFT)
        self.slogan = Button(self.frame, text="Hello", command=self.write_slogan)
        self.slogan.pack(side=LEFT)

    def write_slogan(self):
        print("Tkinter is easy to use!")

# fen = Tk()
# fen.geometry("200x200")
# fen.title("Nombre de cars et de places vides")

# def calcul():
#     try:
#         nb_eleve = int(enNbEleves.get())
#         nb_adulte = int(enNbAdultes.get())
#         nb_place = int(enNbPlacesCars.get())
#         labNbCars.config(text="test", fg="green")
#     except:
#         labNbCars.config(text="Erreur de saisie", fg="red")

# labNbEleves = Label(fen, text="Nombre d'élèves")
# enNbEleves = Entry(fen)
# labNbAdultes = Label(fen, text="Nombre d'adultes")
# enNbAdultes = Entry(fen)
# labNbPlacesCars = Label(fen, text="Nombre de places par cars")
# enNbPlacesCars = Entry(fen)
# retourBtn = Button(fen, text="Calcul", command=calcul)
# labNbCars = Label(fen, text="Nombre de cars")

# labNbEleves.pack()
# enNbEleves.pack()
# labNbAdultes.pack()
# enNbAdultes.pack()
# labNbPlacesCars.pack()
# enNbPlacesCars.pack()
# retourBtn.pack()
# labNbCars.pack()

# fen.mainloop()