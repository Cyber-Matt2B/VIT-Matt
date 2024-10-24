"""def CalculerSurfaceRectangle(Longueur:int,largeur:int): # Calcule la surface d'un rectangle
      Somme=Longueur*largeur
      print (Somme)
CalculerSurfaceRectangle(5,3)

def Factorielle(n): # Fait la factorielle de n'importe quel nombre   
    resultat = 1       
    for i in range(1, n + 1):
        resultat *= i # Multiplication assignment 
    return resultat
resultat = Factorielle(5)
print(resultat)

def ConvertirEnFahrenheit(celsius): # Converti le Farhenheit en Celsius
    fahrenheit = celsius * 9 / 5 + 32 
    return fahrenheit
resultat = ConvertirEnFahrenheit(0)
print(resultat)  # Et maintenant tout ceci fonctionne convenablement ! 

def Fonction(): # Donne la valeur absolue d'un entier
    nombre = int(input("Entrez un nombre entier : "))
    valeur_absolue = abs(nombre) # abs pour la valeur absolue
    print("La valeur absolue de", nombre, "est", valeur_absolue)
Fonction()

def Fonction(): # Le script calcule la longueur de la phrase et la mets en majuscule
    phrase = input("Entrez une phrase : ")
    phrase_majuscule = phrase.upper() # Ici en majuscule
    longueur_phrase = len(phrase) # Ici compte le nombre de charactère 
    print("Phrase en majuscules :", phrase_majuscule)
    print("Longueur de la phrase :", longueur_phrase)
Fonction() 

def Fonction(): # Saisir 2 nombres et trouver le nombre le plus grand puis l'afficher
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    plus_grand = max(nombre1, nombre2) # Trouve le nombre le plus grand 
    print("Le plus grand des deux nombres est :", plus_grand) # Affiche le plus grand
Fonction()

def Fonction():
    nombre = float(input("Entrez un nombre à virgule flottante : ")) # Demande à l'utilisateur de saisir un nombre à virgule flottante
    nombre_arrondi = round(nombre) # Arrondi le nombre entier le plus proche
    print("Le nombre arrondi à l'entier le plus proche est :", nombre_arrondi) #Affiche le nombre arrondi
Fonction()
# Création de tableaux
def Fonction(): # Créer un tableau avec 3 charactères
    color:str[3]
    color=["red","blue","green"]
    print (color[0]) # Affiche le 1er charactère du tableau
    print (color[2]) # Affiche le 3ème charactère du tableau
Fonction()

def Fonction(): # Créer un tableau avec 3 charactères
    fruit:str[3]
    fruit=["pomme","banane","cerise"]
    print (fruit[0]) # Affiche le 1er charactère du tableau
    print (fruit[2]) # Affiche le 3ème charactère du tableau
Fonction()

def Fonction(): # Créer un tableau avec 3 charactères
    nombre:str[5]
    nombre=["10","20","30","40","50"]
    nombre[1]=25  # Remplace le 20 par 25
    print (nombre) # Affiche le tableau
Fonction()

def Fonction(): # 1ère version
    animaux = [] # Créer un tableau vide
    animaux.append("chien") # Ajoute le mot chien
    animaux.append("chat") # Ajoute le mot chat
    animaux.append("oiseau") # Ajoute le mot oiseau
    # animaux.append("requin") test
    # animaux.remove("chien") test
    animaux.remove("chat") # Retire le mot chat
    print(animaux) 
Fonction()

def Fonction(): # 2ème version
    animaux = [] # Tableau vide
    animaux = ["chien","chat","oiseau"] # Voilà le tableau
    animal=animaux.pop(1) # Retire le mot chat "2ème mot"
    print(animaux) # Affiche le tableau sans le chat
Fonction()

def Fonction(): # 1ère version
    notes = []
    notes = [12,15,14,10,20]
    somme=notes[0]+notes[1]+notes[2]+notes[3]+notes[4]
    print(somme)
Fonction()

def Fonction(): # 2ème version
    notes = []
    notes = [12,15,14,10,20]
    total_notes = sum(notes)
    print (total_notes)
Fonction()

def Fonction(): # 1ère version
    valeurs = [5,3,8,2,7,1,10] # Création du tableau
    max_valeur = max(valeurs) # Trouver la valeur maximale et minimale avec les fonctions intégrées
    min_valeur = min(valeurs)
    print(f"Le max est : {max_valeur}")
    print(f"Le mini est : {min_valeur}")
Fonction()"""

def Fonction(): # 2ème version
    valeurs = [5, 3, 8, 2, 7, 1, 10] # Création du tableau
    max_valeur = valeurs[0] # Initialisation des variables pour le maximum et le minimum
    min_valeur = valeurs[1]
    for valeur in valeurs: # Parcourir les éléments pour trouver le max et le min
     if valeur > max_valeur:
        max_valeur = valeur
        if valeur < min_valeur:
            min_valeur = valeur
    print(f"Le max est : {max_valeur}")
    print(f"Le mini est : {min_valeur}")
Fonction()





