# interact-with-os
Durant mon cours de IT Automation, j'apprends à travers ce cours comment interagir avec le OS

## Pré-requis
- Python 3
- `pip`

## Créer un environnement virtuel

Créer puis activer l'environnement virtuel local. `python3` sert à garantir l'interpréteur système pour créer le venv, puis `python` pointe vers l'interpréteur du venv une fois activé :

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Mettre à jour `pip` puis installer les dépendances du projet :

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Lancer le projet

Exécuter le script de health check après activation du venv :

```bash
python health_check.py
```

## Tests

Lancer la suite de tests :

Installer les dépendances puis lancer les tests :

```bash
pytest
```
