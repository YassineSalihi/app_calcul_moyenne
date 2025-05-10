import tkinter as tk
from tkinter import messagebox

def Calculer():
    print("hiii")

# Creation d'une fenetre 
nom_fenetre = tk.Tk()
# titre de fenetre
nom_fenetre.title("App de calcul de moyenne : ")
# dimension de fenetre
largeur = 600
longueur = 400 
nom_fenetre.geometry(f"{largeur}x{longueur}")
# ---------- DONE ------
#####################################################
# TASK : 1 
# AJOUTER UN CADRE
nom_cadre = tk.Frame(nom_fenetre)
nom_cadre.pack(pady=5)

# AJOUTER LABEL
nom_label = tk.Label(nom_cadre, text = "Note 1 : ")
nom_label.pack(side = "left")

# AJOUTER ZONE DE TEXTE
nom_zone_texte = tk.Entry(nom_cadre) # kant nom_fenetre
nom_zone_texte.pack(side = "left") 


# TASK 2 
# AJOUTER UN CADRE
nom_cadre2 = tk.Frame(nom_fenetre)
nom_cadre2.pack(pady=5)

# AJOUTER LABEL
nom_label2 = tk.Label(nom_cadre2, text = "Note 2 : ")
nom_label2.pack(side = "left")

# AJOUTER ZONE DE TEXTE
nom_zone_texte2 = tk.Entry(nom_cadre2) # kant nom_fenetre
nom_zone_texte2.pack(side = "left") 

# TASK : 3 
# AJOUTER UN CADRE
nom_cadre3 = tk.Frame(nom_fenetre)
nom_cadre3.pack(pady=5)

# AJOUTER LABEL
nom_label3 = tk.Label(nom_cadre3, text = "Note 3 : ")
nom_label3.pack(side = "left")

# AJOUTER ZONE DE TEXTE
nom_zone_texte3 = tk.Entry(nom_cadre3) # kant nom_fenetre
nom_zone_texte3.pack(side = "left") 

# TASK : 3 
# AJOUTER UN CADRE
nom_cadre_examen = tk.Frame(nom_fenetre)
nom_cadre_examen.pack(pady=5)

# AJOUTER LABEL
nom_label_examen = tk.Label(nom_cadre_examen, text = "Examen : ")
nom_label_examen.pack(side = "left")

# AJOUTER ZONE DE TEXTE
nom_zone_texte_examen = tk.Entry(nom_cadre_examen) # kant nom_fenetre
nom_zone_texte_examen.pack(side = "left") 

#*********** FRAME FOR BOUTTON *****************
nom_cadre_boutton = tk.Frame(nom_fenetre)
nom_cadre_boutton.pack(pady=10)

# AJOUTER BOUTTON 
nom_bouton = tk.Button(nom_cadre_boutton, text = "Calculer les moyennes", command=Calculer, cursor = "heart") # TODO : FIND OPTION N#3
# FIXED
nom_bouton.pack(pady=10, side = "left") # TODO : fix me im waaay up

# start of fenetre
nom_fenetre.mainloop()



