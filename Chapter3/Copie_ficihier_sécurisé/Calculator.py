
from tkinter import Tk,TRUE,FALSE,Entry,RIGHT,Button,Frame,StringVar

root = Tk()
root.title("CALCULATRICE SCIENTIFIQUE")
root.geometry("380x550") # Taille ajustée pour tout voir
root.resizable(width=FALSE, height=FALSE)
root.config(bg="#090711")

# VARIABLES 
etext = StringVar()

# FONCTIONS 

def operation(valeur):
    """Ajoute le chiffre ou l'opérateur à l'écran"""
    actuel = etext.get()
    # Si l'écran affiche "0" ou "Erreur", on remplace par la nouvelle valeur
    if actuel == "0" or actuel == "Erreur":
        etext.set(valeur)
    else:
        etext.set(actuel + str(valeur))

def calculer():
    """Calcule le résultat de l'expression à l'écran"""
    try:
        expression = etext.get()
        # Python ne comprend pas "x" pour multiplier, il veut "*". On remplace donc :
        expression = expression.replace("x", "*")
        
        # eval() calcule le résultat mathématique de la chaîne de caractères
        resultat = eval(expression) 
        etext.set(str(resultat))
        
    except ZeroDivisionError:
        etext.set("Erreur")
    except SyntaxError:
        etext.set("Erreur")
    except Exception as e:
        etext.set(f"Erreur:{e}")

def clear():
    """Efface tout l'écran"""
    etext.set("0")

def supprimer():
    """Efface le dernier caractère"""
    actuel = etext.get()
    if len(actuel) > 1:
        etext.set(actuel[:-1]) # Garde tout sauf le dernier caractère
    else:
        etext.set("0") # S'il ne reste qu'un chiffre, on remet à 0

# --- INTERFACE GRAPHIQUE ---

frame = Frame(root, bg="#090711")
frame.pack(expand=TRUE, fill="both")

# Ecran
ecran = Entry(frame, textvariable=etext, font=("Arial", 30), bg="#090711", fg="white", bd=0, justify=RIGHT)
ecran.grid(row=0, column=0, columnspan=5, pady=20, padx=10, sticky="nsew")
etext.set("0")

# Boutons Chiffres (1-9)
chiffre = 1
for i in range(1, 4):
    for j in range(3):
        bt = Button(frame, text=str(chiffre), font=("Arial", 20), bg="#3C4349", 
                    fg="#D19629", command=lambda x=chiffre: operation(x))
        bt.grid(row=i, column=j, padx=3, pady=3, sticky="nsew")
        chiffre += 1

# Opérateurs (+, -, x, /)
operateurs = ["+", "-", "x", "/"]
for k, op in enumerate(operateurs):
    bt = Button(frame, text=op, font=("Arial", 20), bg="#D19629", 
                fg="black", command=lambda x=op: operation(x))
    bt.grid(row=k+1, column=3, padx=3, pady=3, sticky="nsew")

# Ligne du bas (0, ., +/-)
btn_0 = Button(frame, text="0", font=("Arial", 20), bg="#3C4349", fg="#D19629", 
               command=lambda: operation(0))
btn_0.grid(row=4, column=1, padx=3, pady=3, sticky="nsew")

btn_point = Button(frame, text=".", font=("Arial", 20), bg="#D19629", fg="black", 
                   command=lambda: operation("."))
btn_point.grid(row=4, column=2, padx=3, pady=3, sticky="nsew")

# Boutons d'action (AC, =, Sup)
btn_clear = Button(frame, text="AC", font=("Arial", 20), bg="#D19629", fg="black", 
                   command=clear)
btn_clear.grid(row=1, column=4, rowspan=2, padx=3, pady=3, sticky="nsew")

btn_egal = Button(frame, text="=", font=("Arial", 20), bg="#D19629", fg="black", 
                  command=calculer) # Appel de la fonction calculer
btn_egal.grid(row=3, column=4, rowspan=2, padx=3, pady=3, sticky="nsew") # J'ai agrandi le bouton =

btn_sup = Button(frame, text="←", font=("Arial", 20), bg="#D19629", fg="black", 
                 command=supprimer)
btn_sup.grid(row=4, column=0, padx=3, pady=3, sticky="nsew") # J'ai remplacé +/- par retour arrière pour l'instant

# Configuration de la grille pour que les boutons s'adaptent
for i in range(5):
    frame.grid_columnconfigure(i, weight=1)
for i in range(5):
    frame.grid_rowconfigure(i, weight=1)

root.mainloop()