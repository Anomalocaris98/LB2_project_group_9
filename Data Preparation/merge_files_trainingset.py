def unisci_file(lista_file, file_output):
    """
    Unisce il contenuto di più file di testo in un unico file.
    
    Parametri:
    - lista_file: lista di nomi dei file da unire
    - file_output: nome del file finale unito
    """
    with open(file_output, "w", encoding="utf-8") as out:
        for nome in lista_file:
            with open(nome, "r", encoding="utf-8") as f:
                contenuto = f.read()
                out.write(contenuto + "\n")  # aggiungo anche una riga vuota tra i file

# esempio di utilizzo
file_da_unire = ['subset1_arricchito.tsv','subset2_arricchito.tsv','subset3_arricchito.tsv','subset4_arricchito.tsv','subset5_arricchito.tsv']
unisci_file(file_da_unire, "training_file_all_seq.tsv")
