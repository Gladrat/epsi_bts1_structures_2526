from rich.pretty import pprint


def creer_noeud(valeur, suivant=None):
    return {"valeur": valeur, "suivant": suivant}


def inserer_debut(tete, valeur):
    nouveau = creer_noeud(valeur, tete)
    return nouveau


def inserer_fin(tete, valeur):
    if tete is None:
        return creer_noeud(valeur)

    courant = tete
    while courant["suivant"] is not None:
        courant = courant["suivant"]

    courant["suivant"] = creer_noeud(valeur)
    return tete


def afficher(tete):
    courant = tete
    elements = []

    while courant is not None:
        elements.append(str(courant["valeur"]))
        courant = courant["suivant"]

    print(" -> ".join(elements))


# Suppression
# Insertion


tete = None
tete = inserer_fin(tete, "Antoine")
tete = inserer_fin(tete, "Pierre")
tete = inserer_fin(tete, "Nathan")
tete = inserer_fin(tete, "Lisa")
tete = inserer_fin(tete, "Lola")

tete = inserer_debut(tete, "Yann")

pprint(tete, expand_all=True)
afficher(tete)
