# Automatic-Ticket-Classification



## Overview

The project focuses on building a system which classifies the customer complaint into irrespective topics/categories. The project emphasises on two major tasks:

1. Topic modelling
2. Multi label classification
The final system is a classified model which is used to predict the class/product category of the input customer complaint. The dataset is in the json format which consists of customer complaints. The complaints have to catgorised into five categories :
   * Credit card / Prepaid card
   * Bank account services
   * Theft/Dispute reporting
   * Mortgages/loans
   * Others

After pre-processing ,EDA ,topic modelling and model training, the model is deployed using a flask application.

## Technical Aspects

### Data Pre-processing
* Initially, 78k customer complaints in JSON format were converted to a pandas dataframe.
* Basic text cleaning was performed, including handling missing data, converting text to lowercase, removing digits and punctuation, and eliminating masked characters and text in square brackets.
* To categorize text into five products, noun words were focused on, and only noun words were used for modeling.
* A tf-idf transformation was applied before feeding the data into the NMF model to achieve the desired results.

### Topic modelling using NMF
Non-negative matrix factorization (`NMF`) is a matrix decomposition method that can be used for a variety of applications, including topic modeling. NMF factorizes a non-negative data matrix into two non-negative matrices, where the resulting matrices can be interpreted as the topic-term matrix and the document-topic matrix.This project uses sklearn module to implement NMF.

### Mapping the predictions to five categories
The **NMF** model transformation gives the output as numbers between `0-4`. This has to me mapped to respective categories based on intuition.

### Multi-Label classification
Two models, logistic regression with hyperparameter tuning and XGBoost, were evaluated in the project. Surprisingly, logistic regression outperformed XGBoost on the given dataset, and was ultimately chosen as the final model.


### Deploying the model using flask
A simple web service was built using flask which exposes an api ```/predict``` to  make the model predictions.

## Setup

```bash
# 1. Install necessary packages
pip install -r requirements.txt

# 2. Download the en_core_web_sm model
python -m spacy download en_core_web_sm

# 3. Run the flask application
python app.py
```
The script to run [Flask application](app.py)

## Demo

The notebook here [demo_notebook](notebooks/inference.ipynb) demonstrates calling the predict api to make predicts.


## References

* https://www.kaggle.com/datasets/abhishek14398/automatic-ticket-classification-dataset
* https://github.com/RakshithaBS