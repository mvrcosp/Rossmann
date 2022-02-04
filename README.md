# Rossmann Sales Prediction

## Forecasting sales for the European drugstore chain Rossmann

<p align="center">
  <img src="https://github.com/mvrcosp/Rossmann/blob/main/img/Rossmann.png">
</p>

**Disclaimer:** The dataset I used to create this project is public and it was provided by Kaggle as part of one of their competitions, you can find it [here.](https://www.kaggle.com/c/rossmann-store-sales/data)  The goal of this project is to simulate a real business situation.  

## Business Problem

Rossmann is one of the largest drug store chains in Europe, operating over 3,000 stores in 7 European countries. Recently Rossmann store managers were challenged with the task of **predicting their total sales for each store during a period of six weeks.** Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality. 

## Problem Understanding

* **Motivation**: Forecast sales to help the business team with decision making.
* **Root cause**: The CFO necessity to set budget for the upcoming weeks
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

## Top 3 (+1) Data Insights

The most interesting findings I had while performing Exploratory Data Analysis. You can  find all business hypothesis that I tested in the EDA notebook.

* **Business Hypothesis #2** - **Stores with local competitors should sell less.**

  **False:** In the visualization bellow, representing total sales versus competition distance, we can see that stores with competitors nearby sell more and that sales decreases when distance increases.

<p align="left">
  <img src="https://github.com/mvrcosp/Rossmann/blob/main/img/CompetitionDistanceBinned.png">
</p>

* **Business Hypothesis #4** - **Stores that keep their promos active for longer periods should sell more.**

  **False:** We can see that when promotion time increases (described in weeks in the visualization bellow), sales actually start to drop.

<p align="left">
  <img src="https://github.com/mvrcosp/Rossmann/blob/main/img/SalesOverWeeks.png">
</p>


* **Business Hypothesis #8** - **Stores should sell more at the 2nd semester of the year.**

  **False:** Sales decrease drastically after July. We can clearly see bellow that the 1st semester  outperforms the 2nd semester in terms of sales.

  <p align="left">
    <img src="https://github.com/mvrcosp/Rossmann/blob/main/img/SalesThroughoutTheMonths.png">
  </p>


* 🐰 **Easter Egg:  Business Hypothesis # 6** - **Stores that open during Christmas season should sell more.**

  **False:** In average, Easter holiday sells better than Christmas. Sorry Santa, but Bunny got this one :(

  <p align="left">
    <img src="https://github.com/mvrcosp/Rossmann/blob/main/img/SalesHolidays.png">
  </p>

## Machine Learning Models Performance

I trained four different machine learning algorithms performing cross-validation on each one of them to better prevent overfitting. The metrics results are presented bellow. We can see that the linear algorithms didn't perform too well when compared to the tree-based algorithms. The I algorithm I chose to deploy to production was **XGBoost** since it runs much faster than Random Forest, the algorithm that performed the best. 

  <p align="center">
    <img src="https://github.com/mvrcosp/Rossmann/blob/main/img/MetricsResults.png">
  </p>


## Business Results

The predictions made by our algorithm expects a total (all stores included) sales value of $ 285,860,480.00 for the next six weeks. You can see the prediction for each store, with worst and best scenarios calculated, [in this csv file](https://github.com/mvrcosp/Rossmann/blob/main/data/processed/StoreSalesPredictions.csv). To calculate worst and best scenarios we used the `mean absolute error (MAE)` metric. In the image bellow we have a lineplot comparing our predictions with the actual values of our validation dataset. You can find more business information on our notebook #8.

  <p align="center">
    <img src="https://github.com/mvrcosp/Rossmann/blob/main/img/SalesPredictionsOverTime.png">
  </p>

## Conclusion

This sales forecast can possibly be used by the CFO to help when setting budget for each store. We also hope to bring some interesting insights with the results of our exploratory analysis. Our model is hosted in a production environment at **Heroku**, so store managers can easily access it. They can use an application such as **Postman** to send a JSON file with the store's attributes and receive back the store's prediction. We've also built a **Telegram bot** so they can access the predictions on mobile phones. In this case, they must pass the number of the store to obtain its sales prediction. 

You can try our telegram bot using the link bellow.  To use it, you must pass a sidebar (/) followed by a store number (for example: /25, /806, /1097, etc.) and the bot will return how much that store will sell in the next six weeks. 

[<img alt="Telegram" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>](http://t.me/mp_rossmann_bot)

## Next steps and improvements

We can test a few ideas to increase model's performance, such as:

* Try different strategies for data cleaning and imputation;
* Try a different approach for data engineering, rescaling and encoding;
* Try others classical methods for time series forecasting (such as autoregression and moving averages).
