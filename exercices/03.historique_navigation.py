historique = []
pagesRetour = []


def visiter(url):
    print("Visite :", url)
    historique.append(url)
    pagesRetour.clear()


def retour():
    if historique:
        pagesRetour.append(historique.pop())
        print("Retour à :", historique[-1])
    else:
        print("Pas de page précédente.")


def avant():
    if pagesRetour:
        historique.append(pagesRetour.pop())
        print("Aller à :", historique[-1])
    else:
        print("Pas de page suivante.")


def afficher_historique():
    print("  → Historique de navigation :", historique)
    print("Pages disponibles pour un retour en avant :", pagesRetour)


visiter("page1.com")
visiter("page2.com")
visiter("page3.com")
afficher_historique()
retour()
retour()
afficher_historique()
visiter("page4.com")
afficher_historique()
