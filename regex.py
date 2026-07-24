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


print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))

print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))


print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Lovelace, Ada")

def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])
rearrange_name("Hopper, Grace M.")