# FDM_Mini_Project

![Water Quality](https://github.com/IT21119644/FDM_Mini_Project/blob/main/FDM.png)

## Overview
Welcome to the Water Quality Prediction System, a tool that predicts the potability of water samples based on various parameters. Whether you are a policymaker, environmental agency, water treatment plant, researcher, or part of a community, this system can help you assess the quality of water samples you've collected.

## Technologies Used
- **Frontend:** Developed with React.js and Vite for a smooth user experience.
- **Backend:** Powered by Azure Serverless Function Apps, ensuring scalability and efficiency.
- **Machine Learning Models:** Built using Python's scikit-learn library to provide accurate predictions.

## Model Training
- Six models were trained: Logistic Regression, Support Vector Machine (SVM), K-Nearest Neighbors (K-NN), Decision Tree, Random Forest, and XGBoost.
- After thorough evaluation, the Random Forest model was selected for its superior performance.
- Data preprocessing included handling missing values, categorical variables, normalization of numeric values, and addressing outliers.

## How to Use
1. Access the web application [here](https://lemon-bush-0a7f9860f.3.azurestaticapps.net/).
2. Input water quality parameters, such as pH, iron content, and turbidity.
3. Receive a prediction on the potability of your water sample.

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
2. Install dependencies for the frontend and backend (npm install)
3. Run the application (FE: npm run dev)

## Acknowledgments
- Water quality dataset source: [Kaggle](https://www.kaggle.com/datasets/vanthanadevi08/water-quality-prediction)
