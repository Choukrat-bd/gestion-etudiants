# Gestion des étudiants avec pandas

Petite application en ligne de commande pour gérer des étudiants et leurs notes,
avec stockage dans un fichier Excel.

## Contenu

- `gestion_etudiants.py` — programme Python (pandas)
- `donnees.xlsx` — fichier Excel avec deux feuilles :

| Feuille `Etudiant` | Feuille `Note` |
|---|---|
| Numéro, Nom, Prénom, Classe | Numéro, Nom et Prénom, Math, PC, Malagasy |

## Prérequis

- Python 3.10 ou plus récent
- Bibliothèques :

```
pip install pandas openpyxl
```

## Lancement

```
python gestion_etudiants.py
```

## Menu

```
1. Afficher les étudiants et les notes
2. Ajouter un étudiant
3. Ajouter une note
4. Quitter
```

Les données sont sauvegardées automatiquement dans `donnees.xlsx` après chaque
ajout et à la sortie du programme.

## Fonctionnalités

- Ajout d'un étudiant avec vérification des doublons (numéro unique)
- Ajout de notes (Math, PC, Malagasy) liées à un étudiant existant
- Affichage des tableaux sans index technique
- Sauvegarde persistante dans le fichier Excel
