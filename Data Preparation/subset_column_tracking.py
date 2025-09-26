"Script that adds an additional column to each subset*_arricchito.tsv file in order to map each ID with the relative subset for later usage."
import os
import pandas as pd

lista=["subset1_arricchito.tsv","subset2_arricchito.tsv","subset3_arricchito.tsv","subset4_arricchito.tsv","subset5_arricchito.tsv"]

def aggiungi_colonna_magica(lista):
   
    numero_da_usare = 1

    for nome_del_file in lista:

        df = pd.read_csv(nome_del_file, sep='\t', engine='python')
        df["subset_number"] = numero_da_usare
        df.to_csv(nome_del_file, sep="\t", index=False)
        numero_da_usare = numero_da_usare + 1

    print("Updated files")


aggiungi_colonna_magica(lista)

