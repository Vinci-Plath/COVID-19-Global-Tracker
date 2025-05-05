# COVID-19 Global Data Tracker

## Overview
This project is a comprehensive data analysis dashboard built using Jupyter Notebook. It tracks the global progression of COVID-19 cases, deaths, vaccinations, and (optionally) hospitalizations. The analysis includes data cleaning, visualizations, interactive controls, and key insights derived from global trends.

## Objectives
- Analyze the spread and impact of COVID-19 across different countries.
- Compare key metrics such as total cases, deaths, and vaccination rates.
- Visualize trends and patterns over time.
- Enable user interactivity through dynamic filters and widgets.
- Offer policy-level insights and recommendations based on data patterns.

## Tools & Libraries Used
- **Jupyter Notebook**
- **Python 3.6+**
- **pandas** for data manipulation  
- **matplotlib** and **seaborn** for plotting  
- **plotly** (optional) for choropleth visualizations  
- **ipywidgets** for interactive controls  
- **numpy** for numerical operations

## How to Run the Project

### Option 1: From Jupyter Notebook (Recommended)
1. Clone or download the repository.
2. Install required packages:
   ```bash
   pip install pandas matplotlib seaborn numpy plotly ipywidgets
    ```
3.  Launch Jupyter Notebook:
   ```bash
   jupyter notebook

     ```

4. Open the notebook file (covid_dashboard.ipynb) and run all cells sequentially.


###  Option 2: View Only
You can view the .ipynb notebook directly on GitHub (with outputs included) without installing anything.

 The dashboard will be displayed, and you can interact with the country dropdown, date range slider, and checkbox to view specific data.

5. Files Included
covid_dashboard.ipynb: Jupyter Notebook file containing the interactive dashboard.
covid_dashboard.py: Python script for the dashboard.
README.md: This readme file.


Features
1.  Time series analysis of total cases, deaths, and vaccinations
2. Choropleth map of total cases per million people
3. Interactive dashboard with country/date filtering and hospitalization toggle
4. Key insights and recommendations for public health strategy
5. Output summary metrics and visual comparisons
6. Optional Stretch Goals Implemented:
 - Country and date range selection using dropdown and slider widgets
 - Toggle to include hospitalization/ICU data
 - Fully interactive dashboard within Jupyter using ipywidgets

Key Insights
Case Growth Patterns: The US and India had dramatic case increases; Kenya remained significantly lower.
Vaccination Disparities: Developed countries reached high vaccination rates faster than developing ones.
Death Rate Trends: Death rates generally declined over time due to better treatments and hospital preparedness.
Multiple Waves: Most countries experienced repeated waves of infection.
Data Completeness: Varies across countries; vaccination and hospitalization data was less complete in some.

Recommendations
Increase vaccine equity in developing countries to move toward global herd immunity.
Standardize international data collection for better crisis response.
Recognize and plan for multiple waves in future pandemic strategies.

Data Source
Our World in Data – COVID-19 Dataset

License
This project is intended for educational use. Data is open-source and publicly available.

Author
Chalonreay Bahati Kahindi

Acknowledgments
Our World in Data
Johns Hopkins University
Python open-source community



