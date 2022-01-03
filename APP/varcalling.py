#####################################################################
# author : SCR 21/10/21                                             
# ce script permet de faire du variant calling
# sequence...
#####################################################################

import streamlit as st
import subprocess
import os
import pandas as pd
import plotly.graph_objects as go
import math



def varcalling():
    user = str(os.getcwd())
    st.text("")
    with st.expander("GUIDE D'UTILISATION"):
        st.write("""
     aide
     """)
    st.markdown("""
    <h3><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="32" height="32" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path d="M19 20H4a2 2 0 0 1-2-2V6c0-1.11.89-2 2-2h6l2 2h7a2 2 0 0 1 2 2H4v10l2.14-8h17.07l-2.28 8.5c-.23.87-1.01 1.5-1.93 1.5z" fill="currentColor"/></svg>&nbsp; Choisir La  Référence <strong style="color:crimson;">[ Pathogène ]</strong> </h3>
     """, unsafe_allow_html=True)
    st.text("")
    # liste de programe réquis
    program ="picard"
    program2 = "samtools"
    program3="bcftools"
    process=subprocess.run(['which', program], capture_output=True, text=True)
    process2=subprocess.run(['which', program2], capture_output=True, text=True)
    process3 = subprocess.run(['which', program3], capture_output=True, text=True)
    file = user+"/APP/data/Bam/Mapped"
    if os.path.exists(r'{}'.format(file)) == True:
       bashCmd = ["ls APP/data/Bam/Mapped/*.bam | wc -l"]
       process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
       out, err = process.communicate()
       st.markdown("""<p><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M5.25 3A3.25 3.25 0 0 0 2 6.25v6.007a5.477 5.477 0 0 1 2.5-1.166V8.75A3.25 3.25 0 0 1 7.75 5.5H19v-.25A2.25 2.25 0 0 0 16.75 3H5.25zm14.5 17.5h-7.775l-1.55-1.55A5.5 5.5 0 0 0 5.5 11V8.75A2.25 2.25 0 0 1 7.75 6.5h12A2.25 2.25 0 0 1 22 8.75v9.5a2.25 2.25 0 0 1-2.25 2.25zm-11.643-.332a4.5 4.5 0 1 1 1.06-1.06l2.613 2.612a.75.75 0 1 1-1.06 1.06l-2.613-2.612zM2.5 16.5a3 3 0 1 0 6 0a3 3 0 0 0-6 0z" fill="currentColor"/></g></svg>&nbsp;Nombre De Fichiers Mapped : <strong>{}</strong></p>""".format(str(int(math.sqrt(int(out))))),unsafe_allow_html=True)
       if err==None:
           if process.returncode == 0 and process2.returncode == 0 and process3.returncode == 0:
                file = user+"/APP/data/Reference"
                if os.path.exists(r'{}'.format(file)) == True:
                    bashCmd1 = ["ls APP/data/Reference/*.pac | wc -l"]
                    process1 = subprocess.Popen(bashCmd1, stdout=subprocess.PIPE, text=True, shell=True)
                    out, err = process1.communicate()
                    if err == None:
                        if int(out) != 0:
                            filenames = os.listdir(file)
                            Refereces = []
                            for element in filenames:
                                if ".bwt" not in str(element) and ".pac" not in str(element) and ".ann" not in str(element) and ".sa" not in str(element) and ".amb" not in str(element):
                                    Refereces.append(element)
                                index=[]
                                for name in Refereces:
                                    if str(name)+".bwt" in str(filenames) and str(name)+".pac" in str(filenames) and str(name)+".ann" in str(filenames) and str(name)+".sa" in str(filenames) and str(name)+".amb"  in str(filenames):
                                        index.append(name)
                                
                        with st.container():
                            col1,col2= st.columns([3,1])
                            with col1:
                                optionref = st.selectbox('Liste De Reference',list(set(index)))
                            with col2:
                                Activer=st.button("Demarer")
                        st.write("")
                        filefastq =user+"/APP/data/Bam/Mapped"
                        bashCmd = ["ls APP/data/Bam/Mapped/ | wc -l"]
                        process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
                        out, err = process.communicate()
                        if os.path.exists(r'{}'.format(filefastq)) == True and str(out) != "0":
                            if Activer:
                                filevcf=user+"/APP/data/variants.bcftools"
                                if os.path.exists(r'{}'.format(filevcf)) == True:
                                    optionref="APP/data/Reference/"+str(optionref)
                                    bashCmd1 = ["bash  APP/bashScripts/varcalling.sh {}  {}".format("APP/data/Bam/Mapped/*.bam",str(optionref))]
                                    process3 = subprocess.Popen(bashCmd1, stdout=subprocess.PIPE, text=True,shell=True)
                                    out, err = process3.communicate()
                                    if err == None:
                                        with st.container():
                                            st.write(str(out))
                                            st.success('Effectuer Avec Succès')
                
    filevcf=user+"/APP/data/variants.bcftools"
    if os.path.exists(r'{}'.format(filevcf)) == True:
        st.info("Telecharger vos fichiers vcf [genotypes* , variants*, normalized*]")
        bashCmdcheck=["ls "+user+"/APP/data/variants.bcftools/*.vcf | wc -l"]
        processcheck = process = subprocess.Popen(bashCmdcheck, stdout=subprocess.PIPE, text=True, shell=True)
        out, err = processcheck.communicate()
        st.markdown("""<p><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M5.25 3A3.25 3.25 0 0 0 2 6.25v6.007a5.477 5.477 0 0 1 2.5-1.166V8.75A3.25 3.25 0 0 1 7.75 5.5H19v-.25A2.25 2.25 0 0 0 16.75 3H5.25zm14.5 17.5h-7.775l-1.55-1.55A5.5 5.5 0 0 0 5.5 11V8.75A2.25 2.25 0 0 1 7.75 6.5h12A2.25 2.25 0 0 1 22 8.75v9.5a2.25 2.25 0 0 1-2.25 2.25zm-11.643-.332a4.5 4.5 0 1 1 1.06-1.06l2.613 2.612a.75.75 0 1 1-1.06 1.06l-2.613-2.612zM2.5 16.5a3 3 0 1 0 6 0a3 3 0 0 0-6 0z" fill="currentColor"/></g></svg>&nbsp;Nombre De Fichiers&nbsp; <i style="color:rgb(244 40 38);font-weight:900">vcf*  </i> : <strong>{}</strong></p>""".format(str(int(out))),unsafe_allow_html=True)
        filegetvcf = os.listdir(filevcf)
        vcf = ["Fichier vcf"]
        for element in filegetvcf:
            if element!="Filterring":
                vcf.append(element)
        with st.container():
            colselect,colbtn=st.columns([2,1])
            with  colselect:
                optionselect = st.selectbox('Télecharger',sorted(list(set(vcf))))
            with colbtn:
                if optionselect!="Fichier vcf":
                    with open(os.path.join("APP/data/variants.bcftools/",optionselect), "rb") as file:
                        st.download_button(
                               label="Telecharger le fichier",
                               data=file,
                               file_name="{}".format(optionselect),
                               mime="file/vcf")
                        

