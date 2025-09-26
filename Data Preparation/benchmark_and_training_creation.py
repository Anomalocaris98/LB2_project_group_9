"""
The following script takes in input the tsv files for the positive representatives and for the negative representatives, creating 
the training set (constituted of 80% of each representative file, shuffled and divided into 5 subsets). Also the script creates the benchmark set (or holdout set)
with the remaining shuffled 20% of each input file merged.
"""


file_input_pos="positive_output_rep.tsv"
file_input_neg="negative_output_rep.tsv"
file_output_benchmark="benchmark.tsv"


import random


def benchmark(file_input_neg,file_input_pos,benchmark_file):
    reps_id_pos=[]
    reps_id_neg=[]

    random.seed(18) #shuffling with random library
    
    
    with open(file_input_pos,"r") as file: #reading the reps file and filling a list with them
        for line in file:
            reps_id_pos.append(line.strip())
    
    with open(file_input_neg,"r") as file: #reading the reps file and filling a list with them
        for line in file:
            reps_id_neg.append(line.strip())
    
    random.shuffle(reps_id_pos)
    random.shuffle(reps_id_neg)

    split_index_pos=int(len(reps_id_pos)*0.8)
    split_index_neg=int(len(reps_id_neg)*0.8)

    benchmark_list_pos=reps_id_pos[split_index_pos:]
    benchmark_list_neg=reps_id_neg[split_index_neg:]

    benchmark_list_final=benchmark_list_neg+benchmark_list_pos

    random.shuffle(benchmark_list_final)
    with open(benchmark_file, "w") as file:
        for id in benchmark_list_final:
            file.write(id+"\n")
    

    return reps_id_neg,reps_id_pos,split_index_pos,split_index_neg

reps_id_neg,reps_id_pos,split_index_pos,split_index_neg=benchmark(file_input_neg,file_input_pos,file_output_benchmark)

training_list_pos=reps_id_pos[:split_index_pos]
training_list_neg=reps_id_neg[:split_index_neg]


    
def list_subset_positive_division(training_list_pos):
    
    dimensione_base_pos = len(training_list_pos) // 5
    # Calcola quanti elementi "extra" ci sono (resto della divisione)
    resto_pos = len(training_list_pos) % 5
    sottoliste_pos = []
    inizio_pos = 0
    for i in range(5):
        # La dimensione di questa parte è la dimensione base più 1 se ci sono ancora elementi extra da distribuire
        dimensione_corrente_pos = dimensione_base_pos + (1 if i < resto_pos else 0)
        fine_pos = inizio_pos + dimensione_corrente_pos
        sottoliste_pos.append(training_list_pos[inizio_pos:fine_pos])
        inizio_pos = fine_pos
    
    return sottoliste_pos

def list_subset_negative_division(training_list_neg):
    
    dimensione_base_neg = len(training_list_neg) // 5
    # Calcola quanti elementi "extra" ci sono (resto della divisione)
    resto_neg = len(training_list_neg) % 5
    sottoliste_neg = []
    inizio_neg = 0
    for i in range(5):
        # La dimensione di questa parte è la dimensione base più 1 se ci sono ancora elementi extra da distribuire
        dimensione_corrente_neg = dimensione_base_neg + (1 if i < resto_neg else 0)
        fine_neg = inizio_neg + dimensione_corrente_neg
        sottoliste_neg.append(training_list_neg[inizio_neg:fine_neg])
        inizio_neg = fine_neg
    
    return sottoliste_neg

sottoliste_pos=list_subset_positive_division(training_list_pos)
sottoliste_neg=list_subset_negative_division(training_list_neg)

def merge(sottoliste_pos,sottoliste_neg):
    
    final=[] #lista fatta da 5 sottoliste, ognuna è uno dei training set (quindi comprende positives e negatives)
    
    for i in range(5):
        list=sottoliste_pos[i]+sottoliste_neg[i]
        final.append(list)
        list=[]
    
    return final

final=merge(sottoliste_pos,sottoliste_neg)

def training_subsets(subset1,subset2,subset3,subset4,subset5,final):

    # Crea una lista con i nomi dei file
    nomi_file = [subset1,subset2,subset3,subset4,subset5]


    # Crea una lista vuota per contenere i riferimenti ai file aperti
    file_aperti = []

    # Cicla su ogni nome di file
    for nome in nomi_file:
        # Apri il file in modalità scrittura ("w")
        # La funzione open() restituisce un oggetto file
        file = open(nome, "w")
        # Aggiungi l'oggetto file alla lista
        file_aperti.append(file)

    # A questo punto, tutti i 5 file sono aperti e pronti per essere usati.
    # Puoi scrivere in ogni file accedendo alla lista 'file_aperti'
    for i in range(5):
        for element in final[i]:
            file_aperti[i].write(element + "\n") 
    
    for f in file_aperti:
        f.close()

    return "The 5 subsets files are completed"

subset1="subset1.tsv"
subset2="subset2.tsv"
subset3="subset3.tsv"
subset4="subset4.tsv"
subset5="subset5.tsv"

    




print(benchmark(file_input_neg,file_input_pos,file_output_benchmark))
print(training_subsets(subset1,subset2,subset3,subset4,subset5,final))
print(len(training_list_neg))
print(len(training_list_pos))










        




