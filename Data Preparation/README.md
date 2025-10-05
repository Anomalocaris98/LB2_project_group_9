# Data Preparation

This folder contains the scripts and datasets used to preprocess and structure the UniProt-based protein data for model training and validation.  
The steps performed here convert raw representative datasets (from Data Collection) into benchmark and training subsets used by the prediction algorithms.

---

## Overview

The Data Preparation stage:
- Creates benchmark and training subsets from the representative datasets.
- Enriches files with amino acid sequences and associated metadata.
- Adds tracking columns to identify subset membership.
- Merges subsets to form the final unified training file.

---

## Folder Contents

### benchmark_and_training_creation.py
Script that generates both the **benchmark set** (holdout test set) and the **five training subsets** used for cross-validation.

**Main workflow:**
1. Loads representative protein IDs from `positive_output_rep.tsv` and `negative_output_rep.tsv`.
2. Randomly shuffles and splits each into:
   - 80% → used for training (divided into five subsets)
   - 20% → used for benchmarking (holdout set)
3. Writes the benchmark IDs to `benchmark.tsv` and the training IDs to `subset1.tsv` through `subset5.tsv`.

**Core functions:**
- `benchmark()`: builds the benchmark and training splits.  
- `list_subset_positive_division()` and `list_subset_negative_division()`: divide training lists into 5 folds.  
- `merge()`: combines positive and negative lists per fold.  
- `training_subsets()`: writes subsets to file.  

[Open benchmark_and_training_creation.py](./benchmark_and_training_creation.py)

---

### adding_features.py
Script that enriches the `.tsv` subsets and benchmark file with the **sequence** corresponding to each protein ID.  
It creates new files named `*_arricchito.tsv`.

**Key steps:**
1. Loads the positive and negative FASTA and TSV datasets.
2. Maps protein IDs to both their features and sequences.
3. Combines them to generate enriched versions of:
   - `subset1_arricchito.tsv` → `subset5_arricchito.tsv`
   - `benchmark_arricchito.tsv`
4. Deletes the original, non-enriched files after processing.

**Functions included:**
- `carica_sequenze_fasta()`: reads FASTA sequences into a dictionary.  
- `carica_caratteristiche()`: loads TSV features.  
- `arricchisci_file_subset()`: writes enriched subset files with appended sequences.  
- `elimina_file_originali()`: safely removes original `.tsv` files after enrichment.

[Open adding_features.py](./adding_features.py)

---

### subset_column_tracking.py
Script that adds a **subset identification column** to each enriched subset file.  
This column is used to track from which subset each record originates.

**Process:**
- Reads each `subset*_arricchito.tsv` file.
- Adds a new column `subset_number` (1–5).
- Saves the updated version with the same filename.

[Open subset_column_tracking.py](./subset_column_tracking.py)

---

### merge_files_trainingset.py
Script that merges the five enriched subsets into a **single training dataset** (`training_file_all_seq.tsv`).

**What it does:**
- Reads `subset1_arricchito.tsv` to `subset5_arricchito.tsv`.
- Concatenates all rows in order.
- Saves the result to `training_file_all_seq.tsv`.
