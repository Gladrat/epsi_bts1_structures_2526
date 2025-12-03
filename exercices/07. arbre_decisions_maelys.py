from rich.pretty import pprint


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


def parcours_ordre(racine):
    if racine is None:
        return

    parcours_ordre(racine["g"])
    print(f"{str(racine["val"][0])}: {str(racine["val"][1])} ")
    parcours_ordre(racine["d"])


def rechercher(racine, val):
    if racine is None:
        return False
    
    if racine["val"] == val:
        return True
    
    if val < racine["val"]:
        return rechercher(racine["g"], val)
    else:
        return rechercher(racine["d"], val)


decisions = [
    (50, "Faire ses devoirs"),
    (30, "Regarder une série"),
    (20, "Manger"),
    (40, "Dormir"),
    (70, "Coder un projet perso"),
    (60, "Lire un livre"),
    (80, "Commander un café"),
]

racine = None
for d in decisions:
    racine = inserer(d, racine)

pprint(racine)
parcours_ordre(racine)

print(rechercher(racine, (40, "Jouer à la GameBoy")))