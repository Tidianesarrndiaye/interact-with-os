import re
# Chaîne de log utilisée pour tester l'extraction d'un identifiant numérique.
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# Expression régulière pour capturer le nombre entre crochets.
regex = r"\[(\d+)\]"
# Recherche de l'identifiant dans le log puis affichage du groupe capturé.
result = re.search(regex, log)
print(result[1])


# Recherche de la séquence "aza" dans différents textes.
result = re.search(r"aza", "plaza")
print(result)

# Aucun résultat ici, donc la recherche renvoie None.
result = re.search(r"aza", "bazaar")
print(result)

# Aucun résultat ici également.
result = re.search(r"aza", "maze")
print(result)

# Vérifie si une chaîne commence par "x".
print(re.search(r"^x", "xenon"))

# Le point "." remplace un caractère quelconque dans le motif.
print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))

# Recherche insensible à la casse.
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))

# Même recherche, répétée pour illustrer le comportement.
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))


# Motif pour détecter une terminaison en "way".
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
# Motif pour capturer "cloud" suivi d'un caractère alphanumérique.
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

# Premier caractère non alphabétique.
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
# Premier caractère non alphabétique et non espace.
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

# Correspondance entre "cat" et "dog".
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

# Même exemple répété.
print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
# Liste toutes les occurrences trouvées.
print(re.findall(r"cat|dog", "I like both dogs and cats."))

#Repeated examples of searching for patterns with wildcards and character classes.
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))
# le caratere plus "+" indique que le caractère précédent doit apparaître une ou plusieurs fois.
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

# Le point d'interrogation "?" indique que le caractère précédent est optionnel.
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))

# Le motif "\w*" correspond à zéro ou plusieurs caractères alphanumériques.
# Le motif "\w" correspond à un caractère alphanumérique.
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

#le motif "$" indique la fin de la chaîne.
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))
# verifie si une chaîne est un nom de variable valide en Python.
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))

# la methode groups() retourne un tuple contenant tous les groupes capturés par l'expression régulière.
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
print("{} {}".format(result[2], result[1]))


def rearrange_name(name):
    """
    Cette fonction prend un nom sous la forme "Nom, Prénom" et le réarrange en "Prénom Nom".
    Si le nom n'est pas dans le format attendu, il est retourné tel quel.
    """
        
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


rearrange_name("Lovelace, Ada")

def rearrange_name(name):
    """
    version améliorée de la fonction rearrange_name qui prend en compte les noms avec des caractères spéciaux et des espaces.
    Cette fonction prend un nom sous la forme "Nom, Prénom" et le réarrange en "Prénom Nom". 
    Si le nom n'est pas dans le format attendu, il est retourné tel quel.
    """
    
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])


rearrange_name("Hopper, Grace M.")


# la repetition d'un motif est indiquée par des accolades "{}". Le motif "\b" correspond à une frontière de mot.
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))
print(re.findall(r"\w{5,10}", "I really like strawberries"))
print(re.findall(r"\w{5,}", "I really like strawberries"))
print(re.search(r"s\w{,20}", "I really like strawberries"))


# escapement des caractères spéciaux dans les expressions régulières.
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
result = re.search(regex, "A completely different string that also has numbers [34567]")
result = re.search(regex, "99 elephants in a [cage]")
def extract_pid(log_line):
    """
    Cette fonction prend une ligne de log en entrée et retourne l'identifiant numérique trouvé entre crochets.
    Si aucun identifiant n'est trouvé, elle retourne une chaîne vide.
    """
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))
print(extract_pid("99 elephants in a [cage]"))


# la fonction re.split() divise une chaîne en utilisant un motif d'expression régulière comme séparateur.
print(re.split(r"the|a", "One sentence. Another one? And the last one!"))
print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
#si on veut conserver les séparateurs dans le résultat, on peut utiliser des parenthèses pour capturer le motif.
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))
#-- la fonction re.sub() remplace les occurrences d'un motif par une chaîne spécifiée.
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))
#-- la fonction re.sub() peut également utiliser des groupes capturés pour réorganiser les parties d'une chaîne.
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))