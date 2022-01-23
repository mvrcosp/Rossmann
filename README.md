# Rossmann Sales Prediction

## Forecasting sales for the European drugstore chain Rossmann



![](https://github.com/mvrcosp/Rossmann/blob/main/img/Rossmann.png)

**Disclaimer:** The dataset I used to create this project is public and it was provided by Kaggle as part of one of their competitions, you can find it [here.](https://www.kaggle.com/c/rossmann-store-sales/data)  The goal of this project is to simulate a real business situation.  

## Business Problem

Rossmann is one of the largest drug store chains in Europe, operating over 3,000 stores in 7 European countries. Recently Rossmann store managers were challenged with the task of **predicting their total sales for each store during a period of six weeks.** Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. 

## Problem Understanding

* **Motivation**: Forecast sales to help the business team with decision making.
* **Root cause**: The necessity to plan inventory for the upcoming weeks
* **Solution Format**: A Regression model to predict sales for each store for the next six weeks.

## Business Assumptions

	- Managers have different experiences and perspectives on sales forecasting
	- The CFO usually runs into problems when setting the budget and making decisions
	- A Machine Learning model may be useful to predict sales for all stores.

## Solution Strategy

1. **Step 01 - Loading data and first look:** Collecting data and taking a look at its attributes, target variable, dtypes, basic statistics and missing values. 
2. **Step 02 - Dealing with missing values and data cleaning:** Filling in missing values, changing data types, renaming columns.
3. **Step 03 - Descriptive Statistics:** Taking a deeper look at each numerical attribute with descriptive statistics, especially the target variable **sales**.
4. **Step 04 - Feature Engineering:** New features were created from the raw data. This part of the process is very important to a better model performance.
3. **Step 05 -  Data Filtering:** Cleaning our data a bit more to make it tidy for the next step.
3. **Step 06 - Data Exploratory Analysis:** Performed univariate, bivariate (attribute vs target variable) and multivariate data analysis (correlation heatmap). I tested some business hypothesis and found out interesting insights that I will present in the topic bellow.
3. **Step 07 - Data Preparation:**  Numerical features were rescaled, categorical features were transformed and cyclic data (such as months, weeks and days) was transformed using mathematical trigonometrical functions.
3. **Step 08 - Feature Selection:**  I selected the most relevant features to build the model with the help of the Boruta Library, a feature selection method. 
3. **Step 09 - Machine Learning modeling:** I built a prediction model based on the average values to each store to use it as baseline and I trained 4 different machine learning methods: Linear Regression, Lasso, Random Forest and XGBoost. 
3. **Step 10 - Comparing models performance:**  Made use of metrics such as the `mean absolute error (MAE)`, `mean absolute percentage error (MAPE)` and `Root-Mean Squared error (RMSE)` to evaluate the models and choose the best one. I will be talking more about this process in a topic bellow.
3. **Step 11 - Hyper-parameter fine tuning:** Discovered the best hyper-parameters to a better model performance using Random Search.
3. **Step 12 - Training final model and evaluating error:** Training the final model and interpreting  the error metrics to present it to business.
3. **Step 13 - Model Deploy:** Deploy to production so managers can access the predictions results.

## Top Data Insights









 Rossmann sales prediction project

