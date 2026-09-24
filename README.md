# 🛡️ HR Employee Attrition Command Center

## Overview
This project is an end-to-end data analysis of HR employee attrition. The goal is to identify the primary factors that drive employees to leave a company and present those findings through both a detailed programmatic analysis and an interactive web dashboard. 

## Dataset

IBM HR Analytics Employee Attrition & Performance dataset (public, Kaggle): **1,470 employees, 35 features** covering demographics, job role, compensation, satisfaction, and attrition status.

## What's Inside

| File | Description |
|------|-------------|
| `PTX.ipynb` | Full EDA: data loading, cleaning, **8 univariate questions** on workforce demographics, and **15 bivariate questions** on attrition |
| `app.py` | Streamlit dashboard with a department filter, KPI cards, and charts for job role, monthly income, and overtime |
| `HR-Employee-Attrition.csv` | Raw dataset |
| `Cleaned_HR_Employee_Attrition.csv` | Cleaned dataset (4 non-informative columns removed: `EmployeeCount`, `Over18`, `StandardHours`, `EmployeeNumber`) |
| `requirements.txt` | Python dependencies |

## Key Findings

- **Overall attrition is 16.1%** (237 of 1,470 employees left).
- **Overtime is the strongest signal:** 30.5% of employees working overtime left, versus 10.4% of those who did not.
- **Job role matters:** Sales Representatives have the highest attrition (39.8%), followed by Laboratory Technicians (23.9%) and Human Resources (23.1%).
- **Pay:** employees who left had a median monthly income of 3,202, about 38% lower than the 5,204 median for those who stayed.
- **Travel and marital status:** frequent travelers left at 24.9% (versus 8.0% for non-travelers), and single employees at 25.5% (versus 12.5% for married employees).

## Dashboard Features

- Filter the workforce by department
- KPI cards: total personnel, total attrition, attrition rate
- Attrition by job role, monthly income vs. attrition, and overtime impact

## Tech Stack

Python · Pandas · Plotly Express · Streamlit · Jupyter Notebook

## Run Locally

```bash
git clone https://github.com/ALMoataz-Bellahx/IBM-HR-Analytics-Employee-Attrition-Performance.git
cd IBM-HR-Analytics-Employee-Attrition-Performance
pip install -r requirements.txt
streamlit run app.py
```

## Author

**Abd-Elrahman Al-Moataz Bellah**: [LinkedIn](https://www.linkedin.com/in/al-moataz/) · [GitHub](https://github.com/ALMoataz-Bellahx)

