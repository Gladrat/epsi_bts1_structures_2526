# Exercice : Gestion d'une File d'Attente de Support Client

**Objectif :** Écrire un programme en Python qui simule la gestion d'une file d'attente de support client à l'aide d'une queue (FIFO - First In, First Out). Les clients envoient des demandes de support qui sont traitées dans l'ordre où elles sont reçues. L'exercice mettra en pratique la manipulation d'une queue pour ajouter, retirer et afficher les demandes de support.

**Contexte :** Dans un système de support client, il est crucial de gérer les demandes des clients de manière équitable et ordonnée. Une file d'attente permet de s'assurer que les premières demandes reçues sont les premières traitées, suivant le principe FIFO.

## Instructions

1. **Initialiser la Queue :**

- Déclarez une liste vide, `file_attente`, pour représenter la queue des demandes de support.

1. **Ajouter une Demande de Support (`ajouter_demande`) :**
   
- Créez une fonction `ajouter_demande(client, demande)` qui prend le nom du client et le détail de sa demande en paramètres, et les ajoute à la fin de la file d'attente.

2. **Traiter une Demande de Support (`traiter_demande`) :**
   
- Implémentez une fonction `traiter_demande()` qui retire et retourne la première demande de la file d'attente, simulant ainsi le traitement d'une demande de support. Affichez le nom du client et le détail de la demande traitée.

3. **Afficher la File d'Attente (`afficher_file_attente`) :**
   
- Écrivez une fonction `afficher_file_attente()` qui affiche toutes les demandes actuellement dans la file d'attente, en indiquant l'ordre dans lequel elles seront traitées.

## Exemple de Scénario

- Trois clients envoient des demandes de support dans l'ordre suivant : Alice, Bob, et Charlie.
- Traitez une demande, ce qui devrait retirer la demande d'Alice de la file d'attente.
- Alice envoie une nouvelle demande de support.
- Affichez la file d'attente de support pour voir l'ordre des demandes restantes.

## Attentes

```py
file_attente = []
file_attente = ajouter_demande(file_attente, "Alice", "Problème de connexion")
file_attente = ajouter_demande(file_attente, "Bob", "Mot de passe oublié")
file_attente = ajouter_demande(file_attente, "Charlie", "Problème de facturation")

file_attente = traiter_demande(file_attente)
file_attente = ajouter_demande(file_attente, "Alice", "Question sur un produit")

afficher_file_attente(file_attente)
```

Résultat :

```
Traitement de la demande de Alice : Problème de connexion
File d'attente de support :
1. Bob : Mot de passe oublié
2. Charlie : Problème de facturation
3. Alice : Question sur un produit
```