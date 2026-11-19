#On définit le taux TVA 0.20 en France 
taux_tva = 0.20

#On définit la variable prix et on pose la question à l'utilisateur
prix =float(input("Quel est le prix de votre article ? "))

#On définit la variable quantite et on pose la question à l'utilisateur
quantite =int(input("Quelle quantite avez vous pris ? "))

#On définit la variable prix HT
prix_ht = prix * quantite

#On définit la variable prix TTC
prix_ttc = prix_ht * (1 + taux_tva)

#Enfin on affiche le coût total
print(f"Le prix HT est de : {prix_ht:.2f} euros")
print(f"Le prix TTC est de : {prix_ttc:.2f} euros")