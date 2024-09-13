"""
Par Kraimeche Amine
"""

from scipy import constants

# Entree
feet = float(input("KA: Entrez la taille en pieds : "))
inches = float(input("KA: Entrez les pouces supplémentaires : "))

# Calculs
total_feet = feet + inches / 12
meters = total_feet * constants.foot

# Sortie
print(f"KA: {feet:.0f} pieds et {inches:.0f} pouces vaut {round(meters, 2)} m")
