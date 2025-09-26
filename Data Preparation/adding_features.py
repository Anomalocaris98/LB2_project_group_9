"Script which enriches the .tsv subsets files and the benchmark file with the sequence linked to each ID, creating new files called *_arricchito.tsv"

import os

def carica_sequenze_fasta(percorso_file_fasta):
    """
    Legge un file FASTA e lo carica in un dizionario.
    La chiave è l'ID della proteina, il valore è la sequenza.
    Gestisce il formato di header di UniProt (es. >sp|Q9Y5Q6|...).
    """
    print(f"Sto leggendo il file FASTA: {percorso_file_fasta}...")
    sequenze = {}
    if not os.path.exists(percorso_file_fasta):
        print(f"ERRORE: File FASTA non trovato al percorso: {percorso_file_fasta}")
        return None
        
    with open(percorso_file_fasta, 'r') as file:
        id_corrente = None
        sequenza_corrente = []
        for linea in file:
            linea = linea.strip()
            if linea.startswith('>'):
                if id_corrente:
                    sequenze[id_corrente] = "".join(sequenza_corrente)
                # Estrae l'ID dal formato >sp|ID|NOME
                try:
                    id_corrente = linea.split('|')[1]
                except IndexError:
                    # Formato più semplice, es. >ID
                    id_corrente = linea[1:].split()[0]
                sequenza_corrente = []
            elif id_corrente:
                sequenza_corrente.append(linea)
        if id_corrente:
            sequenze[id_corrente] = "".join(sequenza_corrente)
            
    print(f"Caricate {len(sequenze)} sequenze.")
    return sequenze

def carica_caratteristiche(percorso_file_tsv):
    """
    Legge un file TSV con le caratteristiche e lo carica in un dizionario.
    La chiave è l'ID della proteina, il valore è l'intera riga.
    Restituisce anche la riga di intestazione.
    """
    print(f"Sto leggendo il file delle caratteristiche: {percorso_file_tsv}...")
    caratteristiche = {}
    intestazione = ""
    if not os.path.exists(percorso_file_tsv):
        print(f"ERRORE: File delle caratteristiche non trovato al percorso: {percorso_file_tsv}")
        return None, None
        
    with open(percorso_file_tsv, 'r') as file:
        intestazione = file.readline().strip()
        for linea in file:
            parti = linea.strip().split('\t')
            if parti and parti[0]:
                protein_id = parti[0]
                caratteristiche[protein_id] = linea.strip()
                
    print(f"Caricate {len(caratteristiche)} righe di caratteristiche.")
    return caratteristiche, intestazione

def arricchisci_file_subset(percorso_input, percorso_output, mappa_caratteristiche, mappa_sequenze, intestazione_master):
    """
    Crea un nuovo file di subset/benchmark arricchito con caratteristiche e sequenze.
    """
    print(f"Processando {percorso_input} -> {percorso_output}...")
    id_trovati = 0
    id_mancanti = 0
    
    with open(percorso_input, 'r') as f_in, open(percorso_output, 'w') as f_out:
        f_out.write(f"{intestazione_master}\tSequence\n")
        
        for linea in f_in:
            protein_id = linea.strip()
            if not protein_id:
                continue

            if protein_id in mappa_caratteristiche and protein_id in mappa_sequenze:
                riga_caratteristiche = mappa_caratteristiche[protein_id]
                sequenza = mappa_sequenze[protein_id]
                f_out.write(f"{riga_caratteristiche}\t{sequenza}\n")
                id_trovati += 1
            else:
                print(f"  - Attenzione: ID '{protein_id}' non trovato nei file di riferimento. Verrà saltato.")
                id_mancanti += 1
    
    print(f"Completato. Righe scritte: {id_trovati}, ID mancanti: {id_mancanti}.\n")

def elimina_file_originali(lista_file):
    """
    Elimina i file specificati nella lista, mostrando un messaggio di conferma.
    """
    print("\n--- Passo 3: Eliminazione dei file subset originali ---")
    for percorso_file in lista_file:
        if os.path.exists(percorso_file):
            try:
                os.remove(percorso_file)
                print(f"File eliminato con successo: {percorso_file}")
            except OSError as e:
                print(f"ERRORE: Impossibile eliminare il file {percorso_file}: {e}")
        else:
            # Questo messaggio è utile se lo script viene eseguito più volte
            print(f"Info: Il file da eliminare non è stato trovato (potrebbe essere già stato rimosso): {percorso_file}")




# 1. Definisci i nomi dei file sorgente (positivi e negativi)
file_fasta_pos = "positive_dataset.fasta"
file_fasta_neg = "negative_dataset.fasta"
file_tsv_pos = "positive_dataset.tsv"
file_tsv_neg = "negative_dataset.tsv"

# 2. Carica e unisci i dati di riferimento
print("--- Passo 1: Caricamento dei dati di riferimento ---")
# Unisci le sequenze
seq_pos = carica_sequenze_fasta(file_fasta_pos)
seq_neg = carica_sequenze_fasta(file_fasta_neg)
mappa_sequenze_completa = {**seq_pos, **seq_neg} if seq_pos and seq_neg else None

# Unisci le caratteristiche
feat_pos, intestazione_master = carica_caratteristiche(file_tsv_pos)
feat_neg, _ = carica_caratteristiche(file_tsv_neg)
mappa_caratteristiche_completa = {**feat_pos, **feat_neg} if feat_pos and feat_neg else None

if mappa_sequenze_completa and mappa_caratteristiche_completa:
    print(f"\nTotale sequenze uniche caricate: {len(mappa_sequenze_completa)}")
    print(f"Totale caratteristiche uniche caricate: {len(mappa_caratteristiche_completa)}")
    
    # 3. Definisci i file di input da processare
    file_da_processare = [
        "subset1.tsv",
        "subset2.tsv",
        "subset3.tsv",
        "subset4.tsv",
        "subset5.tsv",
        "benchmark.tsv"
    ]

    print("\n--- Passo 2: Inizio del processo di arricchimento dei file ---")

    # 4. Cicla su ogni file ed esegui l'arricchimento
    errori_arricchimento = False
    for nome_file in file_da_processare:
        if os.path.exists(nome_file):
            base, ext = os.path.splitext(nome_file)
            nome_output = f"{base}_arricchito{ext}"
            
            arricchisci_file_subset(
                nome_file, 
                nome_output, 
                mappa_caratteristiche_completa, 
                mappa_sequenze_completa, 
                intestazione_master
            )
        else:
            print(f"ERRORE: Il file di input '{nome_file}' non è stato trovato. Verrà saltato.\n")
            errori_arricchimento = True

    # 5. Se non ci sono stati errori, elimina i file originali
    if not errori_arricchimento:
        elimina_file_originali(file_da_processare)
        print("\n--- Processo completato con successo! ---")
    else:
        print("\n--- Processo completato con errori. L'eliminazione dei file originali è stata saltata. ---")
        
else:
    print("\nProcesso interrotto. Controlla gli errori riportati sopra, uno o più file sorgente non sono stati trovati o sono vuoti.")