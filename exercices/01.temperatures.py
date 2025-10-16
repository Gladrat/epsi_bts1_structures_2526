temperatures = [
    [15, 14, 14, 13, 13, 14, 15, 16, 18, 20, 22, 23, 23, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14],
    [14, 13, 13, 12, 12, 13, 14, 16, 18, 21, 23, 24, 25, 25, 24, 23, 22, 21, 19, 18, 17, 15, 14, 13],
    [13, 12, 12, 11, 11, 12, 13, 15, 17, 20, 22, 23, 23, 24, 23, 22, 21, 20, 18, 17, 16, 14, 13, 12],
    [14, 13, 13, 12, 12, 14, 15, 17, 19, 22, 24, 25, 26, 26, 25, 24, 23, 22, 20, 19, 18, 16, 15, 14],
    [15, 14, 14, 13, 13, 15, 16, 18, 20, 23, 25, 26, 27, 27, 26, 25, 24, 23, 21, 20, 19, 17, 16, 15],
    [16, 15, 15, 14, 14, 16, 17, 19, 21, 24, 26, 27, 28, 28, 27, 26, 25, 24, 22, 21, 20, 18, 17, 16],
    [15, 14, 14, 13, 12, 14, 15, 17, 19, 22, 24, 25, 26, 26, 25, 24, 23, 22, 21, 20, 19, 17, 16, 15]
]

# Afficher PROPREMENT :
    # Vérifier qu'il y a bien 24 températures pour chaque jour
    # Quelle température à midi le mercredi ?
    # Afficher la moyenne des températures sur un jour (idéalement dans une fonction)
    # Afficher toutes les températures

j = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

for i, jour in enumerate(temperatures, 0):
    print(f"Le {j[i]}, il y a {len(jour)} températures.")

i = j.index("Mercredi")
h = 12
print(f"Le {j[2]} à midi, il fait: {temperatures[i][h + 1]}°")

