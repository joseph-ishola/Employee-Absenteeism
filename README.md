# Logistic Regression Model to Predict Employee Absenteeism
Read more here https://joseph-ishola.github.io/Employee-Absenteeism/

## Project Overview
This project employs a logistic regression approach to predict excessive absenteeism in the workplace. By analyzing employee data, the model identifies key factors contributing to absenteeism. The insights derived from this analysis can help employers implement targeted strategies to improve employee well-being and reduce unnecessary absences.

## Methodology
1. **Exploratory Data Analysis (EDA):**
   - Understanding feature distributions
   - Identifying correlations with absenteeism
2. **Data Preprocessing:**
   - Handling missing values
   - Feature engineering (categorizing reasons for absence, extracting date-based features)
   - Normalization and encoding categorical variables
3. **Model Training & Evaluation:**
   - Implemented logistic regression
   - Evaluated model performance using accuracy, precision, recall, and ROC-AUC

## Dataset Description
The dataset used in this project contains various features related to employee attendance and demographic information, including:

- **Reason for Absence:**  
  - Originally provided as categorical data, this column was transformed into four distinct binary variables: *Reason Type 1, Reason Type 2, Reason Type 3, and Reason Type 4.*
  - These categories were created to better capture different types of absence reasons while reducing multicollinearity in the dataset.
- **Date:**  
  This was later engineered into two features: **Month** and **Day of the Week** to capture potential temporal patterns.
- **Transportation Expense:**  
  Represents the cost incurred for commuting.
- **Distance to Work:**  
  Measures the distance between the employee's home and the workplace.
- **Age:**  
  The age of the employee.
- **Daily Work Load Average:**  
  Indicates the average work intensity per day.
- **Body Mass Index (BMI):**  
  A health-related metric.
- **Education:**  
  - Originally encoded as 1: High School, 2: Graduate, 3: Postgraduate, 4: Masters/PhD.  
  - To simplify the data and highlight education's impact on absenteeism, we engineered it into a **binary variable**:
    - *High school (1) was mapped to 0.*
    - *Graduate, Postgraduate, and Masters/PhD (2, 3, 4) were mapped to 1.*
- **Children and Pets:**  
  Demographic information.
- **Absenteeism Time in Hours:**  
  Total hours an employee was absent, which is used to create the target variable.

### Feature Engineering
- **Temporal Features:**  
  - The original **Date** column was split into **Month** and **Day of the Week** to investigate seasonal or weekday patterns.

- **Reason for Absence Transformation:**  
  - The **Reason for Absence** column was restructured into four binary categorical features (**Reason Type 1, Reason Type 2, Reason Type 3, and Reason Type 4**). This transformation allows for better representation of different types of absences while avoiding multicollinearity issues.

- **Education Transformation:**  
  - The **Education** column was mapped into a **binary class (0 and 1)**, where:
    - *0* represents employees with only a high school education.
    - *1* represents employees with higher education levels (Graduate, Postgraduate, Masters, or PhD).

- **Target Variable Creation:**  
  - To define excessive absenteeism, a new binary column, **Excessive Absence**, was created based on the median value of **Absenteeism Time in Hours**. The labeling criteria are:
      - **1 (Excessive Absence):** If absenteeism hours > median (Employees with an absenteeism time exceeding 3 hours (i.e., 4 hours or more))
      - **0 (Not Excessive Absence):** If absenteeism hours ≤ median
  - This ensures a balanced dataset for logistic regression.

## Modeling and Feature Selection
- **Initial Model Training:**  
  A logistic regression model was trained using all available features.
  
- **Feature Selection Based on Coefficients:**  
  After training, the coefficients of the model were examined:
  - **High-Impact Features:**  
    - *Reason Type 3* (Coefficient: 3.10, Odds Ratio: 22.13) and *Reason Type 1* (Coefficient: 2.80, Odds Ratio: 16.47) were found to have a strong positive association with excessive absenteeism.
    - *Reason Type 2* and *Reason Type 4* also contributed positively, though with smaller effects.
  - **Low-Impact Features:**  
    - Features such as *Daily Work Load Average* (Coefficient: -0.000077) and *Distance to Work* (Coefficient: -0.007779) had coefficients very close to zero, indicating minimal influence on the target variable.  
    These were dropped from the final model to improve its simplicity and interpretability.

## Model Performance
The final logistic regression model achieved the following on the test set:
- **Accuracy:** 75%
- **Classification Report:**
  - **Class 0 (Non-Excessive Absence):**  
    - Precision: 0.75, Recall: 0.80, F1-score: 0.77
  - **Class 1 (Excessive Absence):**  
    - Precision: 0.75, Recall: 0.70, F1-score: 0.72
- **ROC AUC Score:** 0.78

These metrics suggest that the model has a robust performance with a balanced prediction capability between the two classes.
[More here](https://joseph-ishola.github.io/Absenteeism/ "Absenteeism webpage")

## Future Improvements
- Experimenting with other models (e.g., Random Forest, XGBoost) to improve accuracy
- Incorporating additional features such as employee tenure and department information
- Deploying the model as a web application for HR analytics

## Dependencies
- Python 3.x
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

## Conclusion and Future Work
This project demonstrates the effectiveness of logistic regression in predicting excessive employee absenteeism. The analysis highlights that certain absence reasons have a strong impact on the likelihood of excessive absence.

In the future, the model could be enhanced by:
- Exploring ensemble techniques for improved accuracy.
- Incorporating additional features, such as employee job roles or work environment factors.
- Refining feature selection further using domain expertise.

## License Information
This project is licensed under the MIT License.

## Author
Joseph Ishola

