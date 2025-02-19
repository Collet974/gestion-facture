import streamlit as st
import pandas as pd

# === Données d'exemple ===
achats_data = {
    "Date": ["2025-01-10", "2025-01-15", "2025-01-20"],
    "Numéro de Facture": ["FA-001", "FA-002", "FA-003"],
    "Description": ["Engin de chantier A", "Pièces détachées B", "Matériaux C"],
    "Montant TTC": [18000, 600, 2400],
    "Statut": ["Payée", "En attente", "Payée"],
    "Lien PDF": [
        "https://example.com/factures/FA-001.pdf",
        "https://example.com/factures/FA-002.pdf",
        "https://example.com/factures/FA-003.pdf"
    ]
}

# Création du DataFrame
achats_df = pd.DataFrame(achats_data)

# === Titre de l'application ===
st.title("Gestion des Achats et Factures")

# === Affichage du tableau des achats ===
st.subheader("Tableau des Achats")
st.dataframe(achats_df)

# === Aperçu intégré des PDF ===
st.subheader("Aperçu des Factures PDF")
for i, row in achats_df.iterrows():
    st.markdown(f"### {row['Numéro de Facture']} - {row['Description']}")
    st.markdown(f"[Voir la facture]({row['Lien PDF']})")
