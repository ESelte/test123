from tkinter import *
def beregn_lån(***):
    # Tilordner lånefaktor utifra om personen er i ett forhold og bruttoinntekt
    if (int(forhold.get()) == 1):
        if (int(brutto.get()) < 300050):
            lånefaktor = 0
        else:
            if (int(brutto.get()) <= 450000):
                lånefaktor = 3.0
            else:
                if (int(brutto.get()) <= 650000):
                    lånefaktor = 4.0
                else:
                    if (int(brutto.get()) <= 900000):
                        lånefaktor = 4.5
                    else:
                        if (int(brutto.get()) <= 1000000):
                            lånefaktor = 5.0
                        else:
                            if (int(brutto.get()) <= 1200000):
                                lånefaktor = 5.25
                            else:
                                lånefaktor = 5.25
    else:
        if (int(brutto.get()) < 300000):
            lånefaktor = 0.0
        else:
            if (int(brutto.get()) <= 450000):
                lånefaktor = 0.0
            else:
                if (int(brutto.get()) <= 650000):
                    lånefaktor = 3.0
                else:
                    if (int(brutto.get()) <= 900000):
                        lånefaktor = 4.25
                    else:
                        if (int(brutto.get()) <= 1000000):
                            lånefaktor = 5.0
                        else:
                            if (int(brutto.get()) <= 1200000):
                                lånefaktor = 5.5
                            else:
                                lånefaktor = 5.75

    maks_teoretisk_kjøpesum_EK = (int(egenkapital.get())) / 0.15
    maks_teoretisk_kjøpesum_Brutto = (int(brutto.get())) * lånefaktor

    # Regner ut maks lån med hensyn til forhold og barn
    if (int(forhold.get()) == 1):
        if maks_teoretisk_kjøpesum_EK <= maks_teoretisk_kjøpesum_Brutto:
            behov = maks_teoretisk_kjøpesum_EK - (780000 * (int(barn.get()))) - int(egenkapital.get())
            makslån = behov + (int(egenkapital.get()))
        else:
            behov = maks_teoretisk_kjøpesum_Brutto - (780000 * (int(barn.get())))
            makslån = behov + int(egenkapital.get())
    else:
        if maks_teoretisk_kjøpesum_EK <= maks_teoretisk_kjøpesum_Brutto:
            behov = (maks_teoretisk_kjøpesum_EK - (365000 * (int(barn.get())))) - (int(egenkapital.get()))
            makslån = behov + (int(egenkapital.get()))
        else:
            behov = maks_teoretisk_kjøpesum_Brutto - (365000 * (int(barn.get())))
            makslån = behov + int(egenkapital.get())

    if behov <= 0:
        kjøpesum.set('Du kan desverre ikke få lån')
        lånsum.set('Du kan desverre ikke få lån')
    else:
        kjøpesum.set(round(makslån))
        lånsum.set(round(behov))


window=Tk()

# Navngir vinduet
window.title('Lånekalkulator')

# Ledetekst og inndatafelt for egenkapital
lbl_egenkapital = Label(window, text='Egenkapital:')
lbl_egenkapital.grid(row=0, column=0, padx=5, pady=5, sticky=E)

egenkapital = StringVar()
ent_egenkapital = Entry(window, width=9, textvariable=egenkapital)
ent_egenkapital.grid(row=0, column=1, padx=5, pady=5, sticky=W)

# Ledetekst og inndatafelt for bruttoinntekt
lbl_bruttoinntekt = Label(window, text='Bruttoinntekt:')
lbl_bruttoinntekt.grid(row=1, column=0, padx=5, pady=5, sticky=E)

brutto = StringVar()
ent_brutto = Entry(window, width=9, textvariable=brutto)
ent_brutto.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# Ledetekst og inndatafelt for forhold
lbl_forhold = Label(window, text="Forhold (1 for singel, 2 for par):")
lbl_forhold.grid(row=2, column=0, padx=5, pady=5, sticky=E)

forhold = StringVar()
ent_forhold = Entry(window, width=9, textvariable=forhold)
ent_forhold.grid(row=2, column=1, padx=5, pady=5, sticky=W)

# Ledetekst og inndatafelt for barn
lbl_barn = Label(window, text='Barn:')
lbl_barn.grid(row=3, column=0, padx=5, pady=5, sticky=E)

barn = StringVar()
ent_barn = Entry(window, width=9, textvariable=barn)
ent_barn.grid(row=3, column=1, padx=5, pady=5, sticky=W)

# Ledetekst og utdatafelt for maksimal lånesum
lbl_lån = Label(window, text='Maks lånesum:')
lbl_lån.grid(row=5, column=0, padx=5, pady=5, sticky=E)

lånsum = StringVar()
ent_lån = Entry(window, width=35, state='readonly', textvariable=lånsum)
ent_lån.grid(row=5, column=2, padx=5, pady=5)

# Ledetekst og utdatafelt for maksimal kjøpesum
lbl_kjøpesum = Label(window, text='Maks kjøpesum:')
lbl_kjøpesum.grid(row=6, column=0, padx=5, pady=5, sticky=E)

kjøpesum = StringVar()
ent_kjøp = Entry(window, width=35, state='readonly', textvariable=kjøpesum)
ent_kjøp.grid(row=6, column=2, padx=5, pady=5)

# Knapp for å beregne lånet
btn_beregn_lån = Button(window, text='Beregn lån', command=beregn_lån)
btn_beregn_lån.grid(row=4, column=2, padx=5, pady=5, sticky=W)

# Knapp for å avslutte programmet
btn_avslutt = Button(window, text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=7, column=1, padx=5, pady=25, sticky=E)

window.mainloop()
