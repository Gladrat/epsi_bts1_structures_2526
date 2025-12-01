def createHashmap(size=10):
    return [None] * size


def hachage_simple(key, hm):
    """Always return an index (0 : size(hm) -1)"""
    return sum(ord(k) for k in key) % len(hm)


def insert(hm, key, value):
    index = hachage_simple(key, hm)

    hm[index] = value
    return hm


def search(hm, key):
    index = hachage_simple(key, hm)

    return hm[index]


def delete(hm, key):
    index = hachage_simple(key, hm)

    hm[index] = None


hm = createHashmap()

hm = insert(hm, "AF", "Afghanistan")
hm = insert(hm, "FR", "France")

hm = insert(hm, "AF", "...")
hm = insert(hm, "GT", ":(")  # Collision

print(hm)
# print(search(hm, "FR"))
# print(search(hm, "GF"))

# AF = GT

d = {
    "AF": "Afghanistan",
    "FR": "France",
}

print(d.keys())