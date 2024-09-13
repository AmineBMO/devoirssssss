"""
Par Kraimeche Amine
"""

from scipy import constants

# Constantes
CONVERSION_PIEDS_CARRES_METRES_CARRES = constants.foot ** 2
TEMPS_PAR_METRE_CARRE_SECONDES = 5
COUVERTURE_PAR_SAC_METRES_CARRES = 100
COUT_PAR_SAC = 12.50
TAUX_TAXE = 0.14975

# Entree
longueur_pieds = float(input("KA: Entrez la longueur du terrain en pieds : "))
largeur_pieds = float(input("KA: Entrez la largeur du terrain en pieds : "))

# Calculs
surface_pieds_carres = longueur_pieds * largeur_pieds
surface_metres_carres = surface_pieds_carres * CONVERSION_PIEDS_CARRES_METRES_CARRES

temps_secondes = surface_metres_carres * TEMPS_PAR_METRE_CARRE_SECONDES
temps_minutes = temps_secondes / 60

nombre_sacs = (surface_metres_carres + COUVERTURE_PAR_SAC_METRES_CARRES - 1) // COUVERTURE_PAR_SAC_METRES_CARRES

cout_total_avant_taxe = nombre_sacs * COUT_PAR_SAC
cout_total_apres_taxe = cout_total_avant_taxe * (1 + TAUX_TAXE)

# Sortie
print(f"KA: {'Surface du terrain :':<35} {surface_pieds_carres:>10.1f} pieds carrés")
print(f"KA: {'Surface (m²) :':<34} {surface_metres_carres:>10.1f} m²")
print(f"KA: {'Temps pour tondre le gazon :':<33} {temps_minutes:>10.1f} minutes")
print(f"KA: {'Nombre de sacs d\'engrais nécessaires :':<29} {round(nombre_sacs):>2} sacs")
print(f"KA: {'Coût total des sacs d\'engrais :':<25} {cout_total_apres_taxe:>13.2f}$")
