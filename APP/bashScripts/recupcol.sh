#!/bin/sh

###################################################
#            MATRIX version 1.1                   #
###################################################
# RECUPERE LES FICHIERS ISSUE DU FILTERING PUIS LES
# LES TRAITES POUR FORMER UNE MATRICE DE n,m ou LES
# COLONNES SONT LES INDIVIDUS(ALTERNATIFS) ET ASSO-
# CIE AUX POSTIONS , REFERENCES ET CHROMOSONES ...
###################################################

# Ce script represente le programme principal


cut -f 1 APP/data/variants.bcftools/Filterring/COMP.tsv >> APP/data/variants.bcftools/Filterring/Chromosones.tsv
cut -f 2 APP/data/variants.bcftools/Filterring/COMP.tsv >> APP/data/variants.bcftools/Filterring/Positions.tsv
cut -f 3 APP/data/variants.bcftools/Filterring/COMP.tsv >> APP/data/variants.bcftools/Filterring/References.tsv

sleep 1.5

sed -i '1iPOSITION' APP/data/variants.bcftools/Filterring/Positions.tsv
sed -i '1iREFERENCE' APP/data/variants.bcftools/Filterring/References.tsv
sed -i '1iCHROMOSOME' APP/data/variants.bcftools/Filterring/Chromosones.tsv

sleep 0.5

#!/bin/sh

###################################################
#            MATRIX version 1.1                   #
###################################################
# RECUPERE LES FICHIERS ISSUE DU FILTERING PUIS LES 
# LES TRAITES POUR FORMER UNE MATRICE DE n,m ou LES 
# COLONNES SONT LES INDIVIDUS(ALTERNATIFS) ET ASSO-
# CIE AUX POSTIONS , REFERENCES ET CHROMOSONES ...   
###################################################

# Ce script represente le programme principal

#initialisation
i=0
### Traitement
declare -a tab
for read in "$@"
do
    let i=i+1
    # mettre tous les fichiers dans un tableau
    tab[$i]="$read"
done

# initialisation
j=0
#Tantque la variable j est inférieur ou égale à la taille du tableau
while [ "$j" -lt "$#" ]
do
    # Incrémente j de deux pas
    let j=j+1
    #if [ $j -le "$#" ]
    #then
    #Extraire le préfixe du gène
    Input=${tab[$j]}
    
    prefix=$(echo $Input | cut -d'_' -f 1)
    # recuperer la dernier colonne des fichier tsv
    cut -f 11 "$prefix"_comp.tsv >> "$prefix"_alt.tsv
    sleep 0.2
    Id="1i$prefix"
    sed -i $Id "$prefix"_alt.tsv

done

sleep 0.5

paste Chromosones.tsv Positions.tsv References.tsv APP/data/variants.bcftools/Filterring/*_alt.tsv >> APP/data/variants.bcftools/Filterring/MATRICE.tsv
