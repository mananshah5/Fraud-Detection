# CapOne DS Challenge

This repository contains my submission for the Capital One Data Science Challenge.

## Main Notebook

- The main notebook is **`CapOneDSChallenge.ipynb`** — it includes:
  - Data preprocessing and feature engineering
  - Sampling strategy
  - Model training and evaluation
  - Threshold tuning and final metrics

- A PDF version of the notebook (`CapOneDSChallenge.pdf`) is also included for easier viewing.

Note: Sometimes Jupyter notebooks may not render all outputs properly (e.g., long logs or plots). If that happens, please refer to the PDF version, which captures everything as seen during execution. Please trust the VSCode window to be able to view all the outputs if in Restricted Mode.

---

## Models & Data

- All major DataFrames and models are saved as **`.pkl`** files in the folders 'dataframes' and 'models' to preserve data types and avoid re-running heavy computations.
- Run convert.py in the dataframes folder to be able to see the dataframes as .csv
- The final model, **`gb_grid_auc_roc_w_new_feat.pkl`**, is the best-performing one after full grid search and threshold tuning.
  - ROC AUC: 87.42  
  - Final F1 Score: 0.62  
  - Precision: 0.53  
  - Recall: 0.75

---

## Challenge Questions

- A separate PDF (`Capital One Data Science Challenge - Q&A.pdf`) includes all the answers to the original challenge questions. These are the same responses from the .ipynb.

---

## Reproducibility

- The notebook includes all necessary code to rerun the pipeline from scratch if desired.
- You can install the dependencies using:
  pip install -r requirements.txt

---
