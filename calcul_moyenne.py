import tkinter as tk

# Creation d'une fenetre 
#nom_fenetre = tk.Tk()
nom_fenetre = tk.Tk()
# titre de fenetre
nom_fenetre.title("App de calcul de moyenne : ")
# dimension de fenetre
largeur = 600
longueur = 400 
nom_fenetre.geometry(f"{largeur}x{longueur}")

#####################################################

# AJOUTER UN CADRE
nom_cadre = tk.Frame(nom_fenetre)
nom_cadre.pack()

# AJOUTER LABEL
nom_label = tk.Label(nom_fenetre, text = "Note 1 : ")
nom_label.pack()

# AJOUTER ZONE DE TEXTE
nom_zone_texte = tk.Entry(nom_fenetre)
nom_zone_texte.pack()

# start of fenetre
nom_fenetre.mainloop()






