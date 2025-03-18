# Predicting Excessive Absenteeism with Logistic Regression
Read more here https://joseph-ishola.github.io/Absenteeism/

## Project Overview
This project aims to predict excessive absenteeism in the workplace using a logistic regression model. By identifying factors contributing to excessive absenteeism, employers can develop targeted strategies to enhance workplace well-being and productivity.

## Dataset Overview
The dataset includes various employee attributes that influence absenteeism, such as:
- **Reason for Absence** (categorized into four types)
- **Date** (engineered into Month and Day of the Week)
- **Transportation Expense**
- **Distance to Work**
- **Age**
- **Daily Work Load Average**
- **Body Mass Index**
- **Education Level** (encoded as 1-4)
- **Number of Children**
- **Number of Pets**
- **Absenteeism Time in Hours**

## Target Variable
To define excessive absenteeism, a new target column, **Excessive Absence**, was created based on the median of "Absenteeism Time in Hours." The labeling criteria are:
- **1 (Excessive Absence):** If absenteeism hours > median (≥4 hours, equivalent to half a workday)
- **0 (Not Excessive Absence):** If absenteeism hours ≤ median

This ensures a balanced dataset, which is crucial for logistic regression.

## Methodology
1. **Data Preprocessing:**
   - Handling missing values
   - Feature engineering (categorizing reasons for absence, extracting date-based features)
   - Normalization and encoding categorical variables
2. **Exploratory Data Analysis (EDA):**
   - Understanding feature distributions
   - Identifying correlations with absenteeism
3. **Model Training & Evaluation:**
   - Implemented logistic regression
   - Evaluated model performance using accuracy, precision, recall, and ROC-AUC

## Key Findings
- Certain factors, such as **transportation expense** and **reason for absence**, showed strong correlations with absenteeism.
- The logistic regression model achieved a good balance of accuracy and interpretability.
[More here](http://nodeca.github.io/pica/demo/ "Absenteeism webpage")

## Future Improvements
- Experimenting with other models (e.g., Random Forest, XGBoost) to improve accuracy
- Incorporating additional features such as employee tenure and department information
- Deploying the model as a web application for HR analytics

## License Information
This project is licensed under the MIT License.

## Author
Joseph Ishola

