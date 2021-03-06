import streamlit as st
import subprocess
import os
import pandas as pd
import plotly.graph_objects as go

user = str(os.getcwd())


def Matrix():
    st.write("")
    st.write()
    st.warning("La Matrice ci-dessous est fonction des parametres du filtrage [variants Filterring]")
    st.info("Appuyer sur le boutton demarer pour générer et Telecharger en suite ")
    file =  user+"/APP/data/variants.bcftools/Filterring"
    if os.path.exists(r'{}'.format(file)) == True:
        bashCmd = ["ls "+user+"/APP/data/variants.bcftools/Filterring/*_filtered.vcf | wc -l"]
        process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE, text=True, shell=True)
        out, err = process.communicate()
        st.markdown("""<p><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M5.25 3A3.25 3.25 0 0 0 2 6.25v6.007a5.477 5.477 0 0 1 2.5-1.166V8.75A3.25 3.25 0 0 1 7.75 5.5H19v-.25A2.25 2.25 0 0 0 16.75 3H5.25zm14.5 17.5h-7.775l-1.55-1.55A5.5 5.5 0 0 0 5.5 11V8.75A2.25 2.25 0 0 1 7.75 6.5h12A2.25 2.25 0 0 1 22 8.75v9.5a2.25 2.25 0 0 1-2.25 2.25zm-11.643-.332a4.5 4.5 0 1 1 1.06-1.06l2.613 2.612a.75.75 0 1 1-1.06 1.06l-2.613-2.612zM2.5 16.5a3 3 0 1 0 6 0a3 3 0 0 0-6 0z" fill="currentColor"/></g></svg>&nbsp;Nombre De Fichiers vcf : <strong>{}</strong></p>""".format(str(int(out))),unsafe_allow_html=True)
        if err==None:
            if st.button("Générer"):
                bashexmatrice=["bash APP/data/variants.bcftools/Filterring/matrix2.sh"]
                processexmatrice = subprocess.Popen(bashexmatrice, stdout=subprocess.PIPE, text=True, shell=True)
                outex, errex = processexmatrice.communicate()
                if errex==None:
                    st.success("Matrice générer avec succés...")
            st.write("")
            st.markdown("""<h4><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="24" height="24" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><g fill="none"><path d="M15.25 11.5c.966 0 1.75.784 1.75 1.75v4A1.75 1.75 0 0 1 15.25 19h-4.775l-.05-.05c.368-.737.575-1.57.575-2.45c0-1.177-.37-2.268-1-3.163V13h-.257a5.523 5.523 0 0 0-1.672-1.363c.209-.088.438-.137.679-.137h6.5zM11.5 16v1.5h3.75a.25.25 0 0 0 .25-.25V16h-4zm4-1.5v-1.25a.25.25 0 0 0-.25-.25H11.5v1.5h4zm2.5 6h-6.025l.512.513c.278.277.443.626.495.987H18a2 2 0 0 0 2-2V9.828a2 2 0 0 0-.586-1.414l-5.829-5.828a.491.491 0 0 0-.049-.04a.63.63 0 0 1-.036-.03a2.072 2.072 0 0 0-.219-.18a.652.652 0 0 0-.08-.044l-.048-.024l-.05-.029c-.054-.031-.109-.063-.166-.087a1.977 1.977 0 0 0-.624-.138c-.02-.001-.04-.004-.059-.007A.605.605 0 0 0 12.172 2H6a2 2 0 0 0-2 2v7.207c.477-.135.98-.207 1.5-.207V4a.5.5 0 0 1 .5-.5h6V8a2 2 0 0 0 2 2h4.5v10a.5.5 0 0 1-.5.5zm-.622-12H14a.5.5 0 0 1-.5-.5V4.621L17.378 8.5zM5.5 21a4.48 4.48 0 0 0 2.607-.832l2.613 2.612a.75.75 0 1 0 1.06-1.06l-2.612-2.613A4.5 4.5 0 1 0 5.5 21zm0-1.5a3 3 0 1 1 0-6a3 3 0 0 1 0 6z" fill="currentColor"/></g></svg>&nbsp;Visualiser La Matrice et Son Heatmap associé</h2>""",unsafe_allow_html=True)
            filematrice= user+"/APP/data/variants.bcftools/Filterring/MATRICE/MATRICE.tsv"
            if os.path.exists(r'{}'.format(filematrice)) == True:
                with  st.container():
                    st.write("")
                    Matrice=pd.read_table("APP/data/variants.bcftools/Filterring/MATRICE/MATRICE.tsv",sep="\t")
                    Matrice=Matrice.replace("<", "")
                    st.dataframe(Matrice)
                    csv=Matrice.to_csv(sep="\t",columns=Matrice.columns).encode('utf-8')
                    st.download_button("Telecharger",data=csv,file_name="MatriceSnps.csv",mime='text/csv')
                with st.container():
                    df=Matrice.iloc[:,3:]
                    df=df.replace("T","1")
                    df=df.replace("C","1")
                    df=df.replace("A","1")
                    df=df.replace("G","1")
                    df=df.replace("","0")
                    transpose=df.T
                    Position=Matrice.iloc[:,1]
                    pos=[]
                    for elt in Position:
                        pos.append(str(elt))

                    heatmap = go.Figure(data=go.Heatmap(z=transpose.values.tolist(),y=df.columns.tolist(),x=pos,colorscale = [[0, "rgb(47, 2, 99)"],[1, "rgb(255, 208, 1)"]]))
                    heatmap.update_xaxes(side="top")
                    st.plotly_chart(heatmap)
                
            else:
                st.error("Matrice non existante ou pas encore généré")

# with open(os.path.join("APP/data/variants.bcftools/Filterring/",option), "rb") as file:
#                         st.download_button(
#                                label="Telecharger le fichier",
#                                data=file,
#                                file_name="{}".format(option),
#                                mime="file/vcf")