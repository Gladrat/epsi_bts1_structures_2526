from rich.pretty import pprint


def createHashmap(size=10):
    return [[] for _ in range(10)]


def hachage_simple(key, hm):
    """Always return an index (0 : size(hm) -1)"""
    return sum(ord(k) for k in key) % len(hm)


def insert(hm, key, value):
    index = hachage_simple(key, hm)

    for k, v in hm[index]:
        if k == key:
            hm[index] = value
            return hm

    hm[index].append([key, value])
    return hm


def search(hm, key):
    index = hachage_simple(key, hm)

    for k, v in hm[index]:
        if k == key:
            return v

    return None


def delete(hm, key):
    # Récupérer l'index du bucket
    index = hachage_simple(key, hm)
    bucket = hm[index]

    # Récupérer l'indice de l'emplacement de la clef dans le bucket
    # del bucket[i]

    return hm


hm = createHashmap()
print(hm)

hm = insert(hm, "AF", "Afghanistan")
hm = insert(hm, "AZ", "Afrique du Sud")
hm = insert(hm, "GT", ":(")  # Collision
hm = insert(hm, "FR", "France")
hm = insert(hm, "BE", "Belgique")
hm = insert(hm, "EE", "Estonie")
pprint(hm)

print(search(hm, "GT"))
pprint(hm)

hm = delete(hm, "GT")
hm = delete(hm, "FR")
pprint(hm)
