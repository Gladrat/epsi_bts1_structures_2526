# Exercice : Simuler la Navigation Web avec des Stacks

**Objectif :** Écrire un programme en Python qui simule la gestion de l'historique de navigation d'un navigateur web. L'utilisateur doit pouvoir visiter des pages web, revenir à la page précédente, aller à la page suivante (si un retour a été effectué précédemment), et afficher l'historique de navigation.

**Contexte :** Dans un navigateur web, l'historique de navigation est une fonctionnalité essentielle qui permet aux utilisateurs de naviguer facilement entre les pages visitées. Pour cet exercice, vous allez simuler cette fonctionnalité en utilisant des structures de données de type stack pour l'historique des pages visitées (`historique`) et pour les pages vers lesquelles un utilisateur peut revenir après avoir fait un retour (`pagesRetour`).

## Instructions

1. **Initialiser les Stacks :**

- Déclarez deux listes vides, `historique` et `pagesRetour`, pour représenter les stacks d'historique de navigation et de pages de retour.

2. **Visiter une Page (`visiter`) :**

- Créez une fonction `visiter(url)` qui prend une URL en paramètre, l'ajoute à l'historique de navigation et efface toutes les URLs dans les pages de retour, simulant ainsi la visite d'une nouvelle page.

3. **Retourner à la Page Précédente (`retour`) :**

- Implémentez une fonction `retour()` qui permet à l'utilisateur de revenir à la page précédente. Cette action déplace l'URL actuelle de l'historique vers les pages de retour, simulant un retour en arrière dans la navigation.

4. **Avancer à la Page Suivante (`avant`) :**

- Concevez une fonction `avant()` qui permet à l'utilisateur d'avancer à la page suivante si un retour a été effectué auparavant. Cette action déplace l'URL de la stack des pages de retour vers l'historique de navigation.

5. **Afficher l'Historique de Navigation (`afficher_historique`) :**

- Écrivez une fonction `afficher_historique()` qui affiche l'historique de navigation et les pages disponibles pour un retour en avant.

## Exemple de Scénario

- L'utilisateur visite `page1.com`, puis `page2.com`, et enfin `page3.com`.
- L'utilisateur effectue un retour, revenant ainsi à `page2.com`, puis un autre retour à `page1.com`.
- Ensuite, l'utilisateur visite `page4.com`.
- À la fin, affichez l'historique de navigation et les pages disponibles pour un retour en avant.

## Attentes

```python
visiter("page1.com")
visiter("page2.com")
visiter("page3.com")
afficher_historique()
retour()
retour()
afficher_historique()
visiter("page4.com")
afficher_historique()
```

```
Visite : page1.com
Visite : page2.com
Visite : page3.com
  → Historique de navigation : ['page1.com', 'page2.com', 'page3.com']
  → Pages disponibles pour un retour en avant : []
Retour à : page2.com
Retour à : page1.com
  → Historique de navigation : ['page1.com']
  → Pages disponibles pour un retour en avant : ['page3.com', 'page2.com']
Visite : page4.com
  → Historique de navigation : ['page1.com', 'page4.com']
  → Pages disponibles pour un retour en avant : []
```