#On définit la variable prix et on pose la question à l'utilisateur
prix =float(input("Quel est le prix de votre article ? "))

#On définit la variable quantite et on pose la question à l'utilisateur
quantite =int(input("Quelle quantite avez vous pris ? "))

#On définit la variable prix total
prix_total = prix * quantite

#Enfin on affiche le coût total
print(f"Cela fera un total de {prix_total:.2f} euros")