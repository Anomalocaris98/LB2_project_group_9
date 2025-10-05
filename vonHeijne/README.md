# von Heijne – PSWM Cross-Validation

This folder contains the notebook and scripts implementing a von Heijne–style Position-Specific Weight Matrix (PSWM) algorithm for signal peptide scoring and evaluation through 5-fold cross-validation.

---

## Contents
- [cross_validation.ipynb](./cross_validation.ipynb)

---

## Overview

This notebook performs:
1. **Dataset Loading**  
   Imports the five enriched subsets:
   - `subset1_arricchito.tsv`
   - `subset2_arricchito.tsv`
   - `subset3_arricchito.tsv`
   - `subset4_arricchito.tsv`
   - `subset5_arricchito.tsv`

2. **PSWM Construction**  
   Builds position-specific matrices from positive training sequences and computes background frequencies.

3. **Sliding-Window Scoring**  
   Evaluates each sequence in the validation/test sets by scanning overlapping 15-residue windows and selecting the **maximum score**.

4. **Optimal Threshold Determination**  
   Derives precision–recall curves and selects the **threshold** that maximizes the F1-score.

5. **Model Evaluation and Visualization**  
   Produces quantitative metrics and visual outputs:
   - Confusion matrices  
   - Precision–Recall (PR) curves  
   - MCC, Precision, Accuracy, Sensitivity  

   Figures are automatically saved in the `Plots/` directory:
   - `heatmap_pswm_matrix_{i}_dark.png`  
   - `pr_curve_subset_{i}.png`  
   - `all_pr_curves.png`

---

## How to Run

Open and execute the notebook step-by-step (e.g., in Jupyter or VS Code).  
Make sure the five `subset*_arricchito.tsv` files are available in the working directory.

Dependencies:
- Python ≥ 3.8  
- `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

---

## Example Outputs

### Aggregated Precision–Recall Curves
<p align="center">
  <img src="./Plots/all_pr_curves.png" alt="Precision–Recall Curves across Subsets" width="600"/>
</p>

### Example PSWM Heatmap
<p align="center">
  <img src="./Plots/heatmap_pswm_matrix_0_dark.png" alt="PSWM Heatmap Example" width="600"/>
</p>

---

## Cross-Validation Results

| Subset | MCC   | Precision | Accuracy | Sensitivity | Confusion Matrix |
|:------:|:-----:|:----------:|:---------:|:-------------:|:----------------:|
| **0** | 0.679 | 0.710 | 0.938 | 0.718 | `[[1378, 51], [49, 125]]` |
| **1** | 0.679 | 0.776 | 0.941 | 0.651 | `[[1397, 33], [61, 114]]` |
| **2** | 0.682 | 0.735 | 0.940 | 0.697 | `[[1386, 44], [53, 122]]` |
| **3** | 0.658 | 0.755 | 0.938 | 0.634 | `[[1393, 36], [64, 111]]` |
| **4** | 0.585 | 0.671 | 0.924 | 0.586 | `[[1379, 50], [72, 102]]` |

These results summarize the five folds of the cross-validation procedure, showing consistent classification performance across subsets with minor variation in recall and precision.

---

## Outputs

- **Heatmaps:** visualize the positional amino-acid weights of each PSWM.  
- **Precision–Recall Curves:** depict the trade-off between precision and recall for each validation fold.  
- **`all_pr_curves.png`** provides an aggregated comparison of all subsets.

---

**Authors:**  
LB2 Project Group 9 – *Signal Peptide Prediction Pipeline*
