# Signal Peptide Classification Using PSWM and Physicochemical Features

## Overview
This project builds a machine learning pipeline for detecting **signal peptides** in protein sequences.  
The workflow extracts **sequence-based features** from amino acid sequences and trains **Random Forest (RF)** and **Support Vector Machine (SVM)** models to classify proteins as *signal peptide–positive* or *negative*.

The notebook implements:
1. Feature extraction from raw protein sequences (FASTA-like `.tsv` files).  
2. Construction of **Position-Specific Weight Matrices (PSWM)** using positive sequences.  
3. Generation of physicochemical and compositional features for each sequence.  
4. Training and evaluation of classifiers using **5-fold cross-validation**, without shuffling data.

---

## Repository Structure

| File | Description |
|------|--------------|
| `all_features_extraction.ipynb` | Main Jupyter Notebook containing all feature extraction, model training, and evaluation code. |
| `subset1_arricchito.tsv` – `subset5_arricchito.tsv` | Input datasets. Each file contains amino acid sequences and metadata (`Sequence`, `SP cleavage`, etc.). |
| `matrix1.npz` – `matrix5.npz` | Precomputed NumPy feature matrices saved by the notebook (one per subset). |
| `foldX_mcc_vs_features.png` | Plots showing validation MCC versus number of top-ranked features for each fold. |
| `foldX_rf_importances.png` | Random Forest feature importance bar plots for each fold. |

---

## Feature Set

Each sequence is represented by **33 numerical features** and one label (0/1).  
| **Index** | **Feature Name**             | **Description**                                                                            |
| --------- | ---------------------------- | ------------------------------------------------------------------------------------------ |
| 0         | `P_count_first70`            | Number of Proline (P) residues in the first 70 amino acids                                 |
| 1         | `P_density_first70`          | Proline density in the first 70 amino acids (`count / length`)                             |
| 2         | `pswm_score`                 | Maximum PSWM (Position-Specific Weight Matrix) score across the sequence (Von Heijne-like) |
| 3         | `kd_mean_70`                 | Mean hydrophobicity (Kyte–Doolittle scale) in the first 70 residues                        |
| 4         | `kd_win7_max`                | Maximum 7-residue window mean (Kyte–Doolittle hydrophobicity)                              |
| 5         | `polarity_mean_70`           | Mean polarity (Zimmerman scale) in the first 70 residues                                   |
| 6         | `polarity_win7_max`          | Maximum 7-residue window mean for polarity                                                 |
| 7         | `volume_mean_70`             | Mean side-chain volume in the first 70 residues                                            |
| 8         | `volume_win7_max`            | Maximum 7-residue window mean for side-chain volume                                        |
| 9         | `charge_mean_70`             | Mean side-chain charge at pH 7 across the first 70 residues                                |
| 10        | `charge_win7_max`            | Maximum 7-residue window mean for charge                                                   |
| 11        | `longest_hydrophobic_run_70` | Longest contiguous hydrophobic run (Kyte–Doolittle ≥ 1.6)                                  |
| 12        | `entropy_70`                 | Shannon entropy in the first 70 residues (sequence complexity)                             |
| 13        | `num_disulfide_motifs_70`    | Count of disulfide motifs “C…C” (2–5 aa apart) within the first 70 residues                |
| 14        | `%A`                         | Fraction of Alanine in the first 70 residues                                               |
| 15        | `%C`                         | Fraction of Cysteine                                                                       |
| 16        | `%D`                         | Fraction of Aspartic acid                                                                  |
| 17        | `%E`                         | Fraction of Glutamic acid                                                                  |
| 18        | `%F`                         | Fraction of Phenylalanine                                                                  |
| 19        | `%G`                         | Fraction of Glycine                                                                        |
| 20        | `%H`                         | Fraction of Histidine                                                                      |
| 21        | `%I`                         | Fraction of Isoleucine                                                                     |
| 22        | `%K`                         | Fraction of Lysine                                                                         |
| 23        | `%L`                         | Fraction of Leucine                                                                        |
| 24        | `%M`                         | Fraction of Methionine                                                                     |
| 25        | `%N`                         | Fraction of Asparagine                                                                     |
| 26        | `%P`                         | Fraction of Proline                                                                        |
| 27        | `%Q`                         | Fraction of Glutamine                                                                      |
| 28        | `%R`                         | Fraction of Arginine                                                                       |
| 29        | `%S`                         | Fraction of Serine                                                                         |
| 30        | `%T`                         | Fraction of Threonine                                                                      |
| 31        | `%V`                         | Fraction of Valine                                                                         |
| 32        | `%W`                         | Fraction of Tryptophan                                                                     |
| 33        | `%Y`                         | Fraction of Tyrosine                                                                       |
| 34        | `label`                      | Binary class label (0 = no signal peptide, 1 = contains signal peptide)                    |



---

## Cross-Validation and Modeling

The notebook performs **5-fold cross-validation**:
- Each subset (`subset1_arricchito.tsv` to `subset5_arricchito.tsv`) acts as **test**, **validation**, or **training** in rotation.  
- **Random Forest** is used to rank feature importance (Gini index).  
- **SVM (RBF kernel)** is optimized via a manual grid search on parameters **C** and **gamma**.  
- Validation MCC is used for model selection, and test MCC is used for final evaluation.

No random shuffling is applied; folds correspond exactly to the predefined subsets.

---

## Results Summary (5-Fold CV)

| Fold | Best Baseline Params | Best k | Val MCC | Refined Params | Refined Val MCC | Test MCC |
|------|----------------------|--------|----------|----------------|-----------------|-----------|
| 1 | C=1.0, γ=scale | 28 | 0.784 | C=10.0, γ=0.01 | 0.791 | **0.781** |
| 2 | C=10.0, γ=0.01 | 28 | 0.820 | C=10.0, γ=0.01 | 0.820 | **0.787** |
| 3 | C=1.0, γ=0.01 | 23 | 0.781 | C=1.0, γ=0.01 | 0.781 | **0.821** |
| 4 | C=1.0, γ=scale | 14 | 0.829 | C=1.0, γ=scale | 0.829 | **0.751** |
| 5 | C=10.0, γ=0.01 | 12 | 0.805 | C=10.0, γ=0.01 | 0.805 | **0.808** |

**Mean Test MCC:** 0.790  
**Std Dev:** ±0.024  

---

## Output

| File | Description |
|------|--------------|
| `foldX_mcc_vs_features.png` | Validation MCC vs. number of top features. |
| `foldX_rf_importances.png` | Random Forest feature importances for each fold. |
| `matrixX.npz` | NumPy arrays containing extracted features and labels. |

---
