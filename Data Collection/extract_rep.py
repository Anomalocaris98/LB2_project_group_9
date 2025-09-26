"This script extracts the first column from the resulting .tsv files (positive and negative) coming from the mmseq2 command"

file_input=input("Insert the filename: ")
file_output=input("Insert the output: ")

def extract_rep (file_input,file_output):
    list_rep = []
    list_rep_cleaned=[]
    with open(file_input, "r") as tsv:
        for line in tsv:
            columns = line.split()
            list_rep.append(columns[0])
        for seq in list_rep:
            if seq not in list_rep_cleaned:
                list_rep_cleaned.append(seq)
    with open(file_output,"w") as output:
        for element in list_rep_cleaned:
            output.write(element + "\n")
            

    return list_rep_cleaned

print(extract_rep(file_input,file_output))

