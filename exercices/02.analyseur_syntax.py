# Vous devez construire un analyseur syntaxique
    # () : True
    # ()() : True
    # (()) : True
    # (() : False
    # )( : False

def analyseur_syntaxique(chaine):
    stack = []
    print(f"Analyse de: {chaine}")
    for car in chaine:
        if car == "(":
            stack.append(car)
        elif car == ")":
            if not stack:
                print(False)
                return
            stack.pop()
    print(len(stack) == 0)

analyseur_syntaxique("()")
analyseur_syntaxique("()()")
analyseur_syntaxique("(())")
analyseur_syntaxique("(()")
analyseur_syntaxique(")(")
analyseur_syntaxique("(()))")