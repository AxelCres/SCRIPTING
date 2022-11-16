import tkinter as tk
from tkinter import ttk, messagebox


class FenetrePrincipale(tk.Tk):



    def __init__(self):

        super().__init__()

        self.fInformation= tk.Frame()
        self.fValidation= tk.Frame()
        self.test = True
        




        self.label = ttk.Label(self.fInformation, text='Calcul de places',width=20)
        self.lEleves = ttk.Label(self.fInformation, text="Eleves",width=20)
        self.eEleves = ttk.Entry(self.fInformation)
        self.lAdultes= ttk.Label(self.fInformation, text="Adultes",width=20)
        self.eAdultes = ttk.Entry(self.fInformation)
        self.lBus= ttk.Label(self.fInformation, text="Bus",width=20)
        self.eBus = ttk.Entry(self.fInformation)

        self.bValider = ttk.Button(self.fValidation, text='Valider', command=self.__Validation)
        self.lResultat = ttk.Label(self.fInformation, text='', width=20)


        self.__place()

        self.__bind()



    def __place(self):
        

        self.label.pack()
        
        self.fInformation.pack(fill=tk.X)
        self.fValidation.pack(fill=tk.X)

        self.lEleves.pack()
        self.eEleves.pack()
        self.lAdultes.pack()
        self.eAdultes.pack()
        self.lBus.pack()
        self.eBus.pack()
        self.bValider.pack()
        self.lResultat.pack()


    def __bind(self):
        self.bValider.bind("<Button-1>", self.__Validation)




    def __Validation(self, event=None):
        try:
            eleve=self.eEleves.get()
            adultes=self.eAdultes.get()
            bus=self.eBus.get()
            self.lResultat.config(text=str(OUI(int(bus),int(adultes),int(eleve))))
        except:
            self.lResultat.configure(text="BRUUUUAAAAH")

if __name__ == "__main__":
    from problemes import OUI
    FenetrePrincipale.mainloop()
#app=FenetrePrincipale()
#app.mainloop()