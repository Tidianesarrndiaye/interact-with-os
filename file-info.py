from datetime import datetime
from pathlib import Path
import os

def main():
    print("La taille du fichier health_check est de : ", os.path.getsize("health_check.py"), "octets")

    print("Le fichier health_check a été modifié pour la dernière fois le : ", datetime.fromtimestamp(os.path.getmtime("health_check.py")))

    remove_dir("sample-data/remove_dir_sandbox")

def remove_dir(dir_path):
    target = Path(dir_path)

    if not target.exists():
        print(f"Le répertoire {dir_path} n'existe pas.")
        return

    if target.is_symlink():
        print(f"Le chemin {dir_path} est un lien symbolique et ne sera pas supprimé.")
        return

    if not target.is_dir():
        print(f"Le chemin {dir_path} n'est pas un répertoire.")
        return

    for child in target.iterdir():
        if child.is_symlink() or child.is_file():
            child.unlink()
        elif child.is_dir():
            remove_dir(child)

    target.rmdir()
    print(f"Le répertoire {dir_path} a été supprimé.")


if __name__ == "__main__":
    main()

