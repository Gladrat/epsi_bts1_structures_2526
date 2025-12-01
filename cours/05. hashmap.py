import hashlib
# dictionnaires / hashmap / tableaux associatifs
# Les clefs doivent être uniques !

d = {
    "DE": "Allemagne",
}

# Table de hachage
    # réduction
    # perte de matière (données)
    # opération irreversible

    # objectif : créer une signature (unique)


def hachage_simple(value: str) -> int:
    return sum(ord(v) for v in value)


r = hachage_simple("Maëlys")
print(r)


# Créer une fonction de hachage avancée

def hachage_avance(nom: str, prenom: str, ddn: str) -> int:
    s = hachage_simple(nom)
    s += hachage_simple(prenom)
    s += hachage_simple(ddn.replace("/", ""))
    return  s


r = hachage_avance("Leon", "Duval", "12/06/1998")
print(r)

r = hachage_avance("Noel", "Valud", "19/08/1962")
print(r)

r = hachage_avance("Amy", "Doning", "29/12/1997")
print(r)

import hashlib

texte = """a"""

hash_object = hashlib.md5(texte.encode())
hex_digest = hash_object.hexdigest()
print(hex_digest)