# Product Category Classifier

This project contains a machine learning solution for automatically predicting product categories based on product titles.

## Overview

Manually categorizing thousands of products is time-consuming and error-prone. This project uses **TF-IDF vectorization** + **Naive Bayes** to classify products efficiently.

## Dataset

- Source: `data/products.csv`
- Key columns used:
  - `product_title` (input)
  - `category_label` (target)

## Project Structure

- `data/` - raw dataset
- `model/` - trained model saved as `.pkl`
- `notebooks/` - Jupyter notebook for analysis and training
- `scripts/train_model.py` - script to train and save model
- `scripts/test_model.py` - interactive script for predicting categories
- `README.md` - project documentation
