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
The features fall into three main groups:

### 1. PSWM-Based Feature
| Index | Feature | Description |
|--------|----------|-------------|
| 0 | `PSWM_score` | Highest log-odds score obtained by sliding a window (length=15) across the sequence using the Position-Specific Weight Matrix computed from positive sequences. |

### 2. Proline Composition (2 features)
| Index | Feature | Description |
|--------|----------|-------------|
| 1 | `P_count_70` | Number of proline residues in the first 70 amino acids. |
| 2 | `P_density_70` | Proline count normalized by sequence length (0–70 aa). |

### 3. Physicochemical Descriptors (10 features)
| Index | Feature | Description |
|--------|----------|-------------|
| 3 | `kd_mean_70` | Mean Kyte–Doolittle hydrophobicity (first 70 aa). |
| 4 | `kd_win7_max` | Maximum 7-aa window mean hydrophobicity. |
| 5 | `polarity_mean_70` | Mean polarity (Zimmerman scale). |
| 6 | `polarity_win7_max` | Maximum 7-aa window polarity mean. |
| 7 | `volume_mean_70` | Mean side-chain volume. |
| 8 | `volume_win7_max` | Maximum side-chain volume mean. |
| 9 | `charge_mean_70` | Mean side-chain charge at pH ~7. |
| 10 | `charge_win7_max` | Maximum 7-aa window charge mean. |
| 11 | `longest_hydrophobic_run_70` | Length of the longest continuous run with hydrophobicity ≥ 1.6. |
| 12 | `entropy_70` | Shannon entropy of amino acid composition (first 70 aa). |

### 4. Amino Acid Composition (20 features)
| Index | Feature | Description |
|--------|----------|-------------|
| 13–32 | `%A` to `%Y` | Relative frequency of each amino acid (A, C, D, …, Y) in the first 70 residues. |

### 5. Label
| Index | Feature | Description |
|--------|----------|-------------|
| 33 | `label` | Binary class label (1 = signal peptide, 0 = no signal peptide). |

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

## How to Run

1. Place all five `.tsv` input files in the same directory as the notebook.  
2. Open and run `all_features_extraction.ipynb` in Jupyter or VSCode.  
3. The notebook will:
   - Extract all features from the sequences.
   - Compute PSWM matrices from positive examples.
   - Build 5 feature matrices (`matrix1`–`matrix5`).
   - Train and evaluate Random Forest + SVM models.
   - Save result plots in the working directory.

---

## Output Files

| File | Description |
|------|--------------|
| `foldX_mcc_vs_features.png` | Validation MCC vs. number of top features. |
| `foldX_rf_importances.png` | Random Forest feature importances for each fold. |
| `matrixX.npz` | NumPy arrays containing extracted features and labels. |

---

## Requirements

- Python ≥ 3.9  
- NumPy, Pandas, Matplotlib  
- scikit-learn  
- Biopython (for amino acid scales, optional)
