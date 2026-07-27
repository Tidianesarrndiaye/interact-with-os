#Attentin n'executer pas ce code, il est dangereux et peut endommager votre système.
# c'est un exemple pour montrer comment ajouter un chemin à la variable d'environnement PATH pour exécuter une commande qui se trouve dans ce chemin.


import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["~/projets/interact-with-os/myapp", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)
print(result)