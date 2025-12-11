def unisci_file(lista_file, file_output):
    """
    Unisce il contenuto di più file TSV con lo stesso header
    in un unico file, scrivendo l'header solo una volta.
    """
    first = True
    with open(file_output, "w", encoding="utf-8") as out:
        for nome in lista_file:
            with open(nome, "r", encoding="utf-8") as f:
                lines = f.readlines()
                if first:
                    # Scrivo anche l'header del primo file
                    out.writelines(lines)
                    first = False
                else:
                    # Dal secondo file in poi salto la prima riga (header)
                    out.writelines(lines[1:])