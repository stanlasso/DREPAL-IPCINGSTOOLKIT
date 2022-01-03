import streamlit as st
import subprocess
import os
import pandas as pd
import plotly.graph_objects as go



def filterring():
    user = str(os.getcwd())
    st.write("")
    st.markdown(""" 
            <h5><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="26" height="26" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M3 17v2h6v-2H3M3 5v2h10V5H3m10 16v-2h8v-2h-8v-2h-2v6h2M7 9v2H3v2h4v2h2V9H7m14 4v-2H11v2h10m-6-4h2V7h4V5h-4V3h-2v6z" fill="currentColor"/></svg>&nbsp;Paramètre Du Filtrage</h4>
            """
            ,unsafe_allow_html=True)
    st.write()
    optionstype=["snps","indels","other"]
    type = st.radio("Coché le types d'alternatif",options=optionstype)
    st.text("")
    with st.container():
        colq,colp=st.columns(2)
        with  colq:
            qualite=st.number_input("Entrer la qualité",step=1)
        with colp:    
            profondeur=st.number_input("Entrer la profondeur",step=1)
    zonechoix=st.checkbox("Voulez vous effectué un filtre dans une zone particulière")
    zone="abscence"
    zonech=1
    program1="bcftools"
    program2="bgzip"
    process1=subprocess.run(['which', program1], capture_output=True, text=True)
    process2=subprocess.run(['which', program2], capture_output=True, text=True)
    file = user+"/APP/data/variants.bcftools"
    if os.path.exists(r'{}'.format(file)) == True:
        bashCmd = ["ls "+user+"/APP/data/variants.bcftools/*_normalized.vcf | wc -l"]
        process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
        out, err = process.communicate()
        st.markdown("""<p><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M5.25 3A3.25 3.25 0 0 0 2 6.25v6.007a5.477 5.477 0 0 1 2.5-1.166V8.75A3.25 3.25 0 0 1 7.75 5.5H19v-.25A2.25 2.25 0 0 0 16.75 3H5.25zm14.5 17.5h-7.775l-1.55-1.55A5.5 5.5 0 0 0 5.5 11V8.75A2.25 2.25 0 0 1 7.75 6.5h12A2.25 2.25 0 0 1 22 8.75v9.5a2.25 2.25 0 0 1-2.25 2.25zm-11.643-.332a4.5 4.5 0 1 1 1.06-1.06l2.613 2.612a.75.75 0 1 1-1.06 1.06l-2.613-2.612zM2.5 16.5a3 3 0 1 0 6 0a3 3 0 0 0-6 0z" fill="currentColor"/></g></svg>&nbsp;Nombre De Fichiers vcf : <strong>{}</strong></p>""".format(str(int(out))),unsafe_allow_html=True)
        if err==None:
            if process1.returncode == 0 and process2.returncode == 0:
                if zonechoix==True:
                    zonech=0
                    st.write("Veuillez entrer la zone :[CHROM:DE POSITION-A POSITION  !!(ex : Pf3D7_01_v3:1409-10000 )]")
                    zone=st.text_input("Zone")
                if qualite!="" and profondeur!="" or zone!="":
                    file = user+"/APP/data/variants.bcftools/Filterring"
                    if os.path.exists(r'{}'.format(file)) == True and int(out)!=0:
                        if st.button("Demarrer"):
                            bashCmdex = ["bash  APP/bashScripts/filterring.sh {} {} {} {} {} {}".format(str("APP/data/variants.bcftools/*_normalized.vcf"),str(type),str(qualite),str(profondeur),str(zonech),str(zone))]
                            processex= subprocess.Popen(bashCmdex, stdout=subprocess.PIPE, text=True, shell=True)
                            outex, errex = processex.communicate()
                            if errex==None:
                                st.success("EFFECTUER AVEC SUCCES")
        st.info("Telecharger vos fichiers filtrer")
        bashCmdcheck=["ls "+user+"/APP/data/variants.bcftools/Filterring/*.vcf | wc -l"]
        processcheck = process = subprocess.Popen(bashCmdcheck, stdout=subprocess.PIPE, text=True, shell=True)
        out, err = processcheck.communicate()
        st.markdown("""<p><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M5.25 3A3.25 3.25 0 0 0 2 6.25v6.007a5.477 5.477 0 0 1 2.5-1.166V8.75A3.25 3.25 0 0 1 7.75 5.5H19v-.25A2.25 2.25 0 0 0 16.75 3H5.25zm14.5 17.5h-7.775l-1.55-1.55A5.5 5.5 0 0 0 5.5 11V8.75A2.25 2.25 0 0 1 7.75 6.5h12A2.25 2.25 0 0 1 22 8.75v9.5a2.25 2.25 0 0 1-2.25 2.25zm-11.643-.332a4.5 4.5 0 1 1 1.06-1.06l2.613 2.612a.75.75 0 1 1-1.06 1.06l-2.613-2.612zM2.5 16.5a3 3 0 1 0 6 0a3 3 0 0 0-6 0z" fill="currentColor"/></g></svg>&nbsp;Nombre De Fichiers&nbsp; <i style="color:rgb(244 40 38);font-weight:900">vcf* fitrés </i> : <strong>{}</strong></p>""".format(str(int(out))),unsafe_allow_html=True)
        filenames = os.listdir(file)
        vcf = ["Fichier vcf filtrés"]
        for element in filenames:
            if ".sh" not in str(element) and ".tsv" not in str(element) and ".txt" not in str(element) and "MATRICE" not in str(element):
                vcf.append(element)
        with st.container():
            colselect,colbtn=st.columns([2,1])
            with  colselect:
                option = st.selectbox('Télecharger',sorted(list(set(vcf))))
            with colbtn:
                if option!="Fichier vcf filtrés":
                    with open(os.path.join("APP/data/variants.bcftools/Filterring/",option), "rb") as file:
                        st.download_button(
                               label="Telecharger le fichier",
                               data=file,
                               file_name="{}".format(option),
                               mime="file/vcf")