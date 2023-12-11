# Project_PredictiveAnalytics

## Project Domain
![Heart Image](https://raw.githubusercontent.com/febbyarynt/assets/4d604b149e3df0c0d34514dad135f58f8a3981db/heart%20failure.jpeg)

The heart is an organ that plays a crucial role in human survival by distributing blood from the lungs to all parts of the body. The blood carries a large amount of oxygen, aiding the metabolic processes in the human body. Therefore, the heart needs to be protected, cared for, and maintained to prevent damage that can lead to heart failure.

Cardiovascular disease (CVD) patients, which include disorders of the heart or coronary heart disease, are increasing globally and becoming the most fatal diseases. Healthcare systems worldwide face difficulties due to the lack of medical staff expertise in determining and predicting these diseases. One effective way to identify and predict heart disease is by utilizing machine learning algorithms. Machine learning can overcome the complexity of diagnosing heart disease with predictive models.

Early prediction of heart failure based on health history is essential for preventive measures. This prediction can be obtained by utilizing machine learning technology to discover new knowledge from basic data, thus identifying valid, useful, and easily learnable patterns. The proposed solution involves utilizing machine learning with regression methods to predict the likelihood of someone developing heart failure by considering various factors. This can be developed into an application to help the public predict their health and continue to adopt healthier lifestyles.

## Business Understanding

### Problem Statements
- The community and healthcare professionals need the best model to predict individuals at risk of heart disease from available data. This serves as a guide to improving efficiency in healthcare, impacting public health statistics.

### Goals
- Build the best model to predict heart disease, beneficial for individuals potentially at risk, enabling early prevention.

### Solution Statements
- Offer a predictive system solution using regression methods. To obtain the best solution, three different models (KNN, RandomForest, Boosting) with hyperparameter tuning will be used. Additionally, the performance of the model will be measured using the Mean Squared Error (MSE) metric, where the best model should obtain the smallest MSE value from the test dataset.
- Two metrics used are:
  - Accuracy: a reference for prediction results, derived from sklearn with the Accuracy/score formula.
  - Mean Squared Error (MSE): a reference for the reduction of actual values, derived from sklearn with the name MSE.

## Data Understanding

Based on the dataset source: [Heart Failure Prediction Dataset](https://www.kaggle.com/fedesoriano/heart-failure-prediction), the information obtained is:
**Abstract**: The dataset consists of 1190 data points (rows) collected from several countries, including:
Cleveland: 303 observations
Hungarian: 294 observations
Switzerland: 123 observations
Long Beach VA: 200 observations
Stalog (Heart) Data Set: 270 observations

Table 1. Dataset Information

| | Description |
| ----------- | ----------- |
| Data Set Characteristics | Multivariate |
| Attribute Characteristics | Real |
| Associated Tasks | Regression |
| Number of Instances | 918 |
| Number of Attributes | 4 |
| Missing Values? | N/A |
| Area | Computer |

### Variables in the Heart Failure Prediction Dataset are as follows:
Age: patient's age [years]
Sex: patient's gender [M: Male, F: Female]
ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
RestingBP: patient's blood pressure [mm Hg]
Cholesterol: serum cholesterol [mm/dl]
FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
MaxHR: maximum heart rate [Numeric value between 60 and 202]
Oldpeak: old peak = ST [Numeric value measured in depression]
ST_Slope: slope of the peak exercise segment [Up: upsloping, Flat: flat, Down: downsloping]
HeartDisease: output class [1: heart disease, 0: Normal]

### Handling Missing Values
To detect missing values, the `isnull().sum()` function is used, resulting in:

Table 2. Missing Value Detection Result

| Feature | Number of Missing Values |
|:---:|:---:|
| Age | 0 |
| Cholesterol | 0 |
| RestingBP | 0 |
| MaxHR | 0 |

From Table 2, it can be seen that each feature does not have missing values (NULL or NAN), so we can proceed to the next steps, which involve handling outliers.

### Handling Outliers
In this case, to

 handle outliers in the dataset, the Z-score method is used. The Z-score measures the number of standard deviations a data point is from the mean. If the Z-score exceeds a certain threshold, the data point is identified as an outlier.

The steps to handle outliers are as follows:
1. Calculate the Z-score for each data point.
2. Set a threshold to identify outliers (commonly, a threshold of 3 is used).
3. Remove or adjust the outliers accordingly.

After handling missing values and outliers, the data is ready for the next stage of the project. The next steps involve data visualization, preprocessing, and model development.

Continuing with the translation:

---

## Data Visualization

### Data Distribution Visualization
To understand the distribution of each feature in the dataset, histograms are used. Histograms provide a visual representation of the frequency distribution of a dataset.

![Data Distribution](https://raw.githubusercontent.com/febbyarynt/assets/4d604b149e3df0c0d34514dad135f58f8a3981db/data%20distribution.png)

Figure 1. Data Distribution Visualization

### Correlation Matrix Visualization
A correlation matrix is utilized to understand the linear relationship between different features in the dataset. This is crucial for feature selection and model development.

![Correlation Matrix](https://raw.githubusercontent.com/febbyarynt/assets/4d604b149e3df0c0d34514dad135f58f8a3981db/correlation%20matrix.png)

Figure 2. Correlation Matrix Visualization

## Data Preprocessing

### Feature Encoding
For machine learning models to process categorical variables, encoding is necessary. The categorical variables in this dataset are "Sex" and "ChestPainType." These are encoded using the one-hot encoding method.

### Feature Scaling
To ensure that all features contribute equally to the model, feature scaling is applied. The Z-score standardization method is used for this purpose.

### Train-Test Split
The dataset is split into training and testing sets to evaluate the model's performance accurately. The common split ratio used is 80:20, with 80% of the data used for training and 20% for testing.

## Model Development

### K-Nearest Neighbors (KNN)
KNN is a supervised machine learning algorithm used for classification and regression tasks. It classifies data points based on the points nearest to them.

### Random Forest
Random Forest is an ensemble learning method that constructs a multitude of decision trees during training and outputs the mode of the classes (classification) or the mean prediction (regression) of the individual trees.

### Boosting
Boosting is an ensemble learning method that combines weak learners to create a strong learner. AdaBoost, a popular boosting algorithm, is used in this project.

### Hyperparameter Tuning
To enhance model performance, hyperparameter tuning is performed. Grid search is applied to find the optimal hyperparameters for each model.

## Model Evaluation

### Evaluation Metrics
The models are evaluated using two metrics:
- Accuracy: a measure of the overall correctness of the model's predictions.
- Mean Squared Error (MSE): a measure of the average squared difference between actual and predicted values.

### Results
The performance of each model is compared based on these metrics, and the model with the highest accuracy and lowest MSE is selected as the best predictive model.

## Conclusion
The project aims to develop a predictive analytics solution for early detection of heart failure using machine learning. Through thorough data analysis, preprocessing, and model development, the goal is to provide a reliable and accurate predictive model to assist individuals and healthcare professionals in identifying potential risks of heart disease.

