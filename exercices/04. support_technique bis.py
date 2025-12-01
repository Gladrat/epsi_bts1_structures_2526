from collections import deque

file: dict = {
    1: deque(),
    2: deque(),
    3: deque()
}


# def ajouter_demande(file_attente: deque[tuple[str, str]], client: str, demande: str) -> deque[tuple[str, str]]:
#     file_attente.append((client, demande))

#     return file_attente


# def traiter_demande(file_attente: deque[tuple[str, str]]) -> deque[tuple[str, str]]:
#     if file_attente:
#         demande_traitee: tuple[str, str] = file_attente.popleft()
#         print("Traitement de la demande :", demande_traitee)
#     else:
#         print("La file d'attente est vide.")

#     return file_attente


# def afficher_file_attente(file_attente: deque[tuple[str, str]]) -> None:
#     if file_attente:
#         print("File d'attente du support:")
#         for i, (client, demande) in enumerate(file_attente, 1):
#             print(f"Demande n°{i}: {client} -> {demande}")
#     else:
#         print("La file d'attente est vide.")


# file: deque[tuple[str, str]] = deque([])

# file = ajouter_demande(file, "Client 1", "Mon clavier ne fonctionne plus.")
# file = ajouter_demande(file, "CLIENT 2", "Mon écran affiche des lignes vertes")
# file = traiter_demande(file)
# file = ajouter_demande(file, "Client 3", "Licence office désactivée")
# file = ajouter_demande(file, "Client 1", "Ma souris a disparue")
# file = ajouter_demande(file, 12, "Hello ?")
# afficher_file_attente(file)
