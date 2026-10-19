import os
import pandas as pd

FICHIER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "donnees.xlsx")

COLS_ETUDIANT = ["Numéro", "Nom", "Prénom", "Classe"]
COLS_NOTE = ["Numéro", "Nom et Prénom", "Math", "PC", "Malagasy"]


def charger():
    if os.path.exists(FICHIER):
        etudiants = pd.read_excel(FICHIER, sheet_name="Etudiant")
        notes = pd.read_excel(FICHIER, sheet_name="Note")
    else:
        etudiants = pd.DataFrame(columns=COLS_ETUDIANT)
        notes = pd.DataFrame(columns=COLS_NOTE)
    return etudiants, notes


def sauvegarder(etudiants, notes):
    with pd.ExcelWriter(FICHIER, engine="openpyxl") as writer:
        etudiants.to_excel(writer, sheet_name="Etudiant", index=False)
        notes.to_excel(writer, sheet_name="Note", index=False)
    print(f"Données enregistrées dans : {FICHIER}")


def afficher(etudiants, notes):
    print("\n--- ETUDIANTS ---")
    print(etudiants.to_string(index=False) if not etudiants.empty else "Aucun étudiant.")
    print("\n--- NOTES ---")
    print(notes.to_string(index=False) if not notes.empty else "Aucune note.")


def ajouter_etudiant(etudiants):
    numero = input("Numéro : ").strip()
    if not numero:
        print("Numéro obligatoire.")
        return etudiants
    if not etudiants.empty and etudiants["Numéro"].astype(str).str.strip().eq(numero).any():
        print("Ce numéro existe déjà.")
        return etudiants
    nom = input("Nom : ").strip()
    prenom = input("Prénom : ").strip()
    classe = input("Classe : ").strip()
    nouveau = pd.DataFrame([[numero, nom, prenom, classe]], columns=COLS_ETUDIANT)
    etudiants = pd.concat([etudiants, nouveau], ignore_index=True)
    print("Étudiant ajouté.")
    return etudiants


def ajouter_note(etudiants, notes):
    numero = input("Numéro de l'étudiant : ").strip()
    if etudiants.empty or not etudiants["Numéro"].astype(str).str.strip().eq(numero).any():
        print("Aucun étudiant avec ce numéro.")
        return notes
    etud = etudiants[etudiants["Numéro"].astype(str).str.strip() == numero].iloc[0]
    nom_prenom = f"{etud['Nom']} {etud['Prénom']}"
    try:
        math = float(input("Note Math : ").strip())
        pc = float(input("Note PC : ").strip())
        malagasy = float(input("Note Malagasy : ").strip())
    except ValueError:
        print("Note invalide.")
        return notes
    nouvelle = pd.DataFrame([[numero, nom_prenom, math, pc, malagasy]], columns=COLS_NOTE)
    notes = pd.concat([notes, nouvelle], ignore_index=True)
    print("Note ajoutée.")
    return notes


def main():
    etudiants, notes = charger()
    menu = """
===== MENU =====
1. Afficher les étudiants et les notes
2. Ajouter un étudiant
3. Ajouter une note
4. Quitter
"""
    while True:
        print(menu)
        choix = input("Choix : ").strip()
        if choix == "1":
            afficher(etudiants, notes)
        elif choix == "2":
            etudiants = ajouter_etudiant(etudiants)
            sauvegarder(etudiants, notes)
        elif choix == "3":
            notes = ajouter_note(etudiants, notes)
            sauvegarder(etudiants, notes)
        elif choix == "4":
            sauvegarder(etudiants, notes)
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
