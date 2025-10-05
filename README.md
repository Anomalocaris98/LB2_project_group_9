# LB2_project_Group_9
This repository contains the code and data developed for the **Laboratory of Bioinformatics 2** course project.

---

## Table of Contents
1. [Data Collection](#data-collection)
2. [Data Preparation](#data-preparation)
3. [Data Analysis](#data-analysis)
4. [Feature Extraction](#feature-extraction)
5. [Machine Learning Implementation](#machine-learning-implementation)
6. [Model Evaluation](#model-evaluation)
7. [Discussion](#discussion)
8. [Contacts](#contacts)

---

## Data Collection
This phase focuses on retrieving protein datasets from **UniProtKB**.  
Both web interface and API approaches were used to obtain:
- Positive datasets (proteins containing signal peptides)
- Negative datasets (proteins without signal peptides)

After retrieval:
- **MMseqs2** was used to cluster sequences and reduce redundancy.  
- Representative sequences were extracted for use in downstream analysis.

[Go to Data Collection Folder](./Data%20Collection)

---

## Data Preparation
Preprocessing and organization of datasets for **cross-validation** and **benchmarking**.  
This includes:
- Creation of training and benchmark sets  
- Redundancy reduction  
- Labeling of sequences for supervised learning  
- Data splitting for 5-fold validation

[Go to Data Preparation Folder](./Data%20Preparation)

---

## Data Analysis
Analysis and visualization of dataset characteristics, including:
- Sequence length distribution  
- Amino acid frequency  
- Species and kingdom occurrence  
- Dataset balance and redundancy analysis  

[Go to Data Analysis Folder](./Data%20Analysis)

---

## Feature Extraction
Extraction of relevant biological and positional features used for classification models.  
This phase includes:
- Construction of **Position-Specific Weight Matrices (PSWMs)**  
- Computation of positional amino acid frequencies  
- Identification of discriminative features between positive and negative sets

[Go to Feature Extraction Folder](./Feature_Extraction)

---

## Machine Learning Implementation
Implementation of:
- **von Heijne’s algorithm** for position-specific scoring  
- **Support Vector Machine (SVM)** classifier for supervised learning  

[Go to von Heijne Implementation Folder](./vonHeijne)

---

## Model Evaluation
Evaluation of algorithms using:
- Cross-validation  
- Precision–Recall curves  
- Confusion matrices  
- Matthews Correlation Coefficient (MCC)  

The evaluation pipeline ensures robust model performance analysis on both benchmark and blind test sets.

---

## Discussion
This section provides interpretation of the obtained results, comparison of methods, and insights into biological implications of the predictions.

---

## Contacts
- **Valerio Piersanti** — valerio.piersanti3@studio.unibo.it  
- **Kagan Saglam** — kagan.saglam@studio.unibo.it  
- **Andrea Lenti** — andrea.lenti2@studio.unibo.it  
- **Enrico Gallus** — enrico.gallus@studio.unibo.it  
- **Massimo Lanari** — massimo.lanari@studio.unibo.it
