#!/bin/sh

###################################################
#            FILTERING version 1.1                #
###################################################


rm -rf zone/*
# initialisation

#echo $@
Nbargument=$#
#parametre a recuperé avant la fin
count=$(expr $Nbargument - 4)
i=0
## Traitement
declare -a var
declare -a tab
for read in "$@"
do
    let i=i+1
    # mettre tous les fichiers dans un tableau
    if [ $i -lt  $count ];
    then
        tab[$i]="$read"
    else
        var[$i]="$read"
    fi
done

#recuperation des variables:
types=${var[-5]}
Qual=${var[-4]}
Dp=${var[-3]}
choix=${var[-2]}
zone=${var[-1]}



#echo ${tab[@]}
#echo ${#tab[@]}
#echo $choix
# echo $zone
 
# initialisation
j=0
if [[ $choix -eq 0 ]]
then
    #Tantque la variable j est inférieur ou égale à la taille du tableau
    while [ "$j" -le "${#tab[@]}" ]
    do
        # Incrémente j de deux pas
        let j=j+1
        #if [ $j -le "$#" ]
        #then
        #Extraire le préfixe du gène
        Input=${tab[$j]}
    
        #chemin=${Input:27} #pour chemin plus long dans script finale
        #echo "$chemin"
        prefix=$(echo $Input | cut -d'_' -f 1)
        bcftools view -v "$types" "$prefix"_normalized.vcf >> "$prefix"_filtertype.vcf
        bcftools filter -e "QUAL<$Qual || INFO/DP<$Dp"  "$prefix"_filtertype.vcf >> "$prefix"_filtered.vcf

        cp "$prefix"_filtered.vcf zone/
        bgzip zone/"$prefix"_filtered.vcf
        bcftools index zone/"$prefix"_filtered.vcf.gz
        bcftools view -r $zone zone/"$prefix"_filtered.vcf.gz >> "$prefix"_zone.vcf
     done
else
    echo "Traitement avec abscence de zone specifié"
    #Tantque la variable j est inférieur ou égale à la taille du tableau
    while [ "$j" -lt "${#tab[@]}" ]
    do
        let j=j+1
        Input=${tab[$j]}
        prefix=$(echo $Input | cut -d'_' -f 1)
   
        bcftools view -v "$types" ${tab[$j]}  >> "$prefix"_filtertype.vcf
        sleep 4
        bcftools filter -e "QUAL<$Qual || INFO/DP<$Dp"  "$prefix"_filtertype.vcf >> "$prefix"_filtered.vcf
    done
fi
mv APP/data/variants.bcftools/*_filtered.vcf APP/data/variants.bcftools/Filterring
mv APP/data/variants.bcftools/*_filtertype.vcf APP/data/variants.bcftools/Filterring