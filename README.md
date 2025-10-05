# LB2_project_Group_9
This repository contains the code and data developed for the **Laboratory of Bioinformatics 2** course project.

---

## Table of Contents
1. [Data Collection](#data-collection)
2. [Data Preparation](#data-preparation)
3. [Data Analysis](#data-analysis)
4. [von Heijne Implementation and Model Evaluation](#von-heijne-implementation-and-model-evaluation)
5. [Discussion](#discussion)
6. [Contacts](#contacts)

---

## Data Collection
This phase focuses on retrieving protein datasets from **UniProtKB** using both:
- Web interface queries
- Automated API requests

The resulting datasets include:
- **Positive** proteins (containing signal peptides)  
- **Negative** proteins (without signal peptides)

Post-retrieval steps:
- **MMseqs2** was used to cluster sequences and remove redundancy.  
- Representative sequences were extracted to form balanced and biologically diverse sets.

📁 [Open Data Collection Folder](./Data%20Collection)

---

## Data Preparation
Preprocessing and organization of datasets for **cross-validation** and **benchmarking**.  
This includes:
- Creation of training, validation, and benchmark sets  
- Removal of redundant entries  
- Label assignment for supervised learning  
- Construction of consistent subsets for 5-fold validation

📁 [Open Data Preparation Folder](./Data%20Preparation)

---

## Data Analysis
Exploratory analysis and visualization of dataset properties, including:
- **Sequence length distribution**
- **Amino acid residue frequency**
- **Species and kingdom representation**
- **Comparison between training and benchmark datasets**

📁 [Open Data Analysis Folder](./Data%20Analysis)

---

## von Heijne Implementation and Model Evaluation
Implementation of the **von Heijne algorithm**, which computes **Position-Specific Weight Matrices (PSWMs)** for analyzing signal peptide sequences.  

This stage includes:
- Generation of PSWM matrices from training subsets  
- Scoring of validation and testing sequences  
- Evaluation via:
  - Precision–Recall curves  
  - Confusion matrices  
  - Matthews Correlation Coefficient (MCC)  
  - Accuracy, Precision, and Sensitivity

📁 [Open von Heijne Folder](./vonHeijne)

---

## Discussion
Interpretation of results and evaluation of algorithmic performance.  
Includes comparison between subsets and overall cross-validation outcomes, as well as biological insights derived from signal peptide sequence patterns.

---

## Contacts
- **Valerio Piersanti** — valerio.piersanti3@studio.unibo.it
- **Andrea Lenti** — andrea.lenti2@studio.unibo.it  
- **Kagan Saglam** — kagan.saglam@studio.unibo.it  
- **Enrico Gallus** — enrico.gallus@studio.unibo.it  
- **Massimo Lanari** — massimo.lanari@studio.unibo.it
