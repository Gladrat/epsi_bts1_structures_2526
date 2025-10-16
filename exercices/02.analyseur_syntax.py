# Vous devez construire un analyseur syntaxique
    # () : True
    # ()() : True
    # (()) : True
    # (() : False
    # )( : False

def analyseur_syntaxique(x):
    print(x)

analyseur_syntaxique("()")
analyseur_syntaxique("()()")
analyseur_syntaxique("(())")
analyseur_syntaxique("(()")
analyseur_syntaxique(")(")