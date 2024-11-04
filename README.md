# Startups Profit Prediction

An analysis and a Machine Learning-based web application that predicts startup profitability based on R&D, Administration, and Marketing spend in different states using a trained model deployed with Streamlit.

---

## Project Overview

In the competitive business environment, predicting profitability can guide investment decisions. This project is designed to forecast a startup's profit based on spending in critical areas like R&D, administration, and marketing, with consideration of geographical impact by state. 

## Problem Statement

Given the expenditure data across R&D, Administration, and Marketing for 50 startups, **can we predict their profit and understand spending efficiency for optimal resource allocation**?

## Project Objective

1. **Build a predictive model** to forecast startup profit based on expenditure data.
2. **Identify key spending areas** that influence profit maximization.
3. **Deploy an interactive application** that allows users to input their startup spending and receive a profit prediction.

## Table of Contents

- [Data Overview](#data-overview)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Data Preprocessing](#data-preprocessing)
- [Model Building](#model-building)
- [Model Evaluation](#model-evaluation)
- [Deployment](#deployment)
- [Conclusion](#conclusion)
- [Acknowledgments](#acknowledgments)

---

## Data Overview

The dataset was sourced from Kaggle, named `50_Startups.csv`, includes the following variables:

- **R&D Spend**: Expenditure on research and development.
- **Administration**: Expenditure on administrative activities.
- **Marketing Spend**: Expenditure on marketing.
- **State**: Location of the startup (California, Florida, or New York).
- **Profit**: Target variable representing the startup's profit.

## Exploratory Data Analysis

Key observations and visualizations were created to understand the data better:

1. **Profitability Analysis**: Scatterplots for each spending category and correlarion matrix heatmap were made to check for their relationship with the profit.
2. **Comparison Across States**: Barplots and Boxplots to analyze profit differences across California, Florida, and New York.
3. **Developing Investment Strategies**: Correlation heatmaps and Regression plots to reinforce that strategic investments in R&D and marketing are key drivers of profitability across these states


**Profitability Analysis**

![Scatterplots](https://github.com/Phenomkay/Startups-Profit-Predictor/blob/0e95c70354c56cef5b50a3839c44ac21e3b17353/50%20start%20ups%20profitability%20analysis.png)

## Data Preprocessing

1. **State Encoding**: Mapped categorical values to numerical format for the `State` column.
2. **Feature Scaling**: Standardized spending columns to ensure uniform influence on model training.

## Model Building

- **Algorithm**: Linear Regression
- **Libraries**: Scikit-Learn for model training, pickle for saving the model.
- **Steps**:
    - Split the data into training and testing sets.
    - Train the model on the training set.
    - Evaluate performance using the test set.

## Model Evaluation

The model achieved satisfactory results with a focus on:

- **Interpretability**: Linear regression offers insights into feature importance.
- **Accuracy**: High R-squared value indicated a strong fit for predicting profit.

## Deployment

The model was deployed using **Streamlit** with a user-friendly interface:

1. **Input Fields**: For R&D, Administration, and Marketing spend, plus state selection.
2. **Prediction**: Displays profit prediction based on user inputs.
3. **Styling**: Applied custom CSS for a refined interface.

### Running the Application

To run the app locally:

```bash
streamlit run app.py
```

---

## Conclusion

This project provides valuable insights into the relationship between startup spending and profit, offering predictions that can assist in investment decisions. The model indicates R&D spending is a critical factor, with a higher impact on profitability compared to other areas. This interactive application serves as a practical tool for potential startups and investors.

```
