# 🛡️ HR Employee Attrition Command Center

## Overview
This project is an end-to-end data analysis of HR employee attrition. The goal is to identify the primary factors that drive employees to leave a company and present those findings through both a detailed programmatic analysis and an interactive web dashboard. 

## Project Components
1. **Jupyter Notebook (`PTX.ipynb`):** Contains the complete Exploratory Data Analysis (EDA). It walks through data loading, cleaning (removing zero-variance features), univariate analysis of workforce demographics, and bivariate analysis answering 15 specific business questions regarding attrition.
2. **Streamlit Dashboard (`app.py`):** An interactive web application built to serve as a high-level command center. It allows users to filter the workforce by department and instantly see the impact of Overtime, Job Role, and Monthly Income on attrition rates.
3. **Cleaned Dataset (`Cleaned_HR_Employee_Attrition.csv`):** The processed dataset used to power the dashboard.

## Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas
* **Data Visualization:** Plotly Express
* **Web Framework:** Streamlit

## Key Insights Explored
* Overall attrition rates and demographic breakdowns.
* The financial correlation between monthly income and turnover.
* The impact of workplace requirements, such as business travel and overtime.
* Tenure and experience distributions across different roles.

## How to Run the Dashboard Locally

1. Clone this repository to your local machine.
2. Ensure you have the required libraries installed:
   ```bash
   pip install pandas plotly streamlit
