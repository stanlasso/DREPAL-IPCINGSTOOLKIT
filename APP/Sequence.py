#####################################################################
# author : SCR 21/10/21                                             #
# ce script permet de faire de l'importation de données genomique

#####################################################################
import streamlit as st
import pandas as pd
import upload
import subprocess
import os




def sequence():
    st.text("")
    # st.markdown(
    #    """## **Bienvenu dans l'option d'importation et de téléchargement de sequence genomique.**""")
    with st.expander("GUIDE D'UTILISATION"):
        st.write("""
     aide
     """)
    type_genomique = st.radio(
        "A quelque (s) usage est (sont)  destiné (s) vos séquences ?",
        ("Séquence génomique d'hôte", 'Réference'))

    if type_genomique == "Séquence génomique d'hôte":
        st.markdown("""####  Importation locale""", unsafe_allow_html=True)
        oui = st.checkbox(
            "Avez-vous des fichiers excédant 4GB ?")
        if not(oui):
            with st.expander("importer"):
                data = st.file_uploader("charger les fichiers au format fastq*,dscr2,dsrc",
                                        type=["fastq"], accept_multiple_files=True)

                if data != []:
                    name = []
                    for uploaded_file in data:                        
                        name.append(uploaded_file.name[:-6])
                        upload.save_uploadedfile(uploaded_file)
                    st.success("Fichiers importer a succéss...")
        else:
            chemin=st.text_input("Entrer le chemin du repertoire :")
            file=chemin
            bashCmd = ["ls APP/data/Bam/Mapped/ | wc -l"]
            process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
            out, err = process.communicate()


        st.markdown("""####  Télechargement à partir d'une banque de données""")
        st.text("")
        with st.expander("Télécharger"):
            tsv = st.file_uploader("importer le fichier", type={"tsv","txt","xlsx","csv"})
            if tsv is not None:
                tsv_df = pd.read_table(tsv)
                st.markdown("""##### Telechagement en cours ...""")
                upload.save_uploadedfile(tsv)

    else:
        st.markdown("""####  Importation locale""")
        with st.expander("importer"):
            data = st.file_uploader("charger les fichiers au format fasta*",
                                    type=["fasta"], accept_multiple_files=True)

            if data != []:
                name = []
                for uploaded_file in data:
                    name.append(uploaded_file.name[:-6])
                    upload.save_uploadedfileref(uploaded_file)
                st.write('LISTE DES FICHIERS IMPORTER')
                st.write(list(set(name)))
                st.success("Référence importer ...")

def test():
    with st.expander("importer"):
                data = st.file_uploader("charger les fichiers au format fastq*,dscr2,dsrc",
                                        type=["fastq", "dsrc", "dsrc2"], accept_multiple_files=True,)    


