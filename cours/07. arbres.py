from rich.pretty import pprint

#       A
#     / | \
#    B  C  D
#      / \
#     E   F


#       A
#     / |
#    B  C
#      / \
#     E   F


# 30, 50, 10, 20, 60

#       30
#     / |
#    50  10
#      / \
#     20   60

# Arbres : Racine / Noeuds
# Arbres binaires : Racine / Noeuds (2 max)
# Binary Search Tree (BST) : Racine / Noeuds (2 max) / sous-arbre de gauche < racine & sous-arbre de droite > racine

# creer_noeud
# inserer

def creer_noeud(val):
    return {"val": val, "g": None, "d": None}


def inserer(val, racine=None):
    if racine is None:
        return creer_noeud(val)
    
    if val < racine["val"]:
        racine["g"] = inserer(val, racine["g"])
    else:
        racine["d"] = inserer(val, racine["d"])

    return racine


# 50, 30, 70, 20, 40, 60, 80

racine = inserer(30)


pprint(racine)