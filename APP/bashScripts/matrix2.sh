bash APP/bashScripts/generation.sh APP/data/variants.bcftools/Filterring/*_filtered.vcf

sleep 1.5

bash APP/bashScripts/comparaison.sh APP/data/variants.bcftools/Filterring/*_CPRA.txt

sleep 1.5

bash APP/bashScripts/recupcol.sh APP/data/variants.bcftools/Filterring/*_comp.tsv

sleep 1.5
#mkdir /home/user/IPCITOOLSKIT/APP/data/variants.bcftools/Filterring/MATRICE/fake.tsv
#rm -rf MATRICE/*
mv /APP/data/variants.bcftools/Filterring/MATRICE.tsv APP/data/variants.bcftools/Filterring/MATRICE/
