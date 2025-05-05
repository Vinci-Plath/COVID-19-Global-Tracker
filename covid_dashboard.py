# covid_dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
@st.cache_data
def load_data():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    return pd.read_csv(url)

covid_df = load_data()
covid_df['date'] = pd.to_datetime(covid_df['date'])

# Sidebar controls
st.sidebar.header("Dashboard Controls")
countries = sorted(covid_df['location'].unique())
selected_country = st.sidebar.selectbox("Select Country", countries, index=countries.index('United States'))

min_date = covid_df['date'].min().to_pydatetime()
max_date = covid_df['date'].max().to_pydatetime()
date_range = st.sidebar.date_input(
    "Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

show_hosp = st.sidebar.checkbox("Show Hospitalization Data", value=False)

# Process data
def prepare_data(country, start_date, end_date):
    mask = (
        (covid_df['location'] == country) & 
        (covid_df['date'] >= pd.to_datetime(start_date)) & 
        (covid_df['date'] <= pd.to_datetime(end_date))
    )
    df = covid_df.loc[mask].copy()
    
    cols = ['total_cases', 'total_deaths', 'total_vaccinations']
    if show_hosp and 'hosp_patients' in df.columns:
        cols.extend(['hosp_patients', 'icu_patients'])
    
    df[cols] = df[cols].fillna(method='ffill').fillna(0)
    return df

if len(date_range) == 2:
    df = prepare_data(selected_country, date_range[0], date_range[1])
    
    # Dashboard title
    st.title(f"COVID-19 Dashboard: {selected_country}")
    
    # Metrics columns
    latest = df.iloc[-1]
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Cases", f"{latest['total_cases']:,.0f}")
    with col2:
        st.metric("Total Deaths", f"{latest['total_deaths']:,.0f}")
    with col3:
        death_rate = latest['total_deaths']/latest['total_cases'] if latest['total_cases'] > 0 else 0
        st.metric("Death Rate", f"{death_rate:.2%}")
    with col4:
        vaccinations = f"{latest['total_vaccinations']:,.0f}" if pd.notna(latest['total_vaccinations']) else "N/A"
        st.metric("Total Vaccinations", vaccinations)
    
    if show_hosp and 'hosp_patients' in latest:
        col5, col6 = st.columns(2)
        with col5:
            st.metric("Hospital Patients", f"{latest['hosp_patients']:,.0f}")
        with col6:
            st.metric("ICU Patients", f"{latest['icu_patients']:,.0f}")
    
    # Charts
    st.header("Trend Analysis")
    
    fig, ax = plt.subplots(3 if not show_hosp else 5, 1, figsize=(10, 18 if show_hosp else 12))
    
    # Cases
    ax[0].plot(df['date'], df['total_cases'])
    ax[0].set_title('Total Cases')
    ax[0].grid(True)
    
    # Deaths
    ax[1].plot(df['date'], df['total_deaths'], color='red')
    ax[1].set_title('Total Deaths')
    ax[1].grid(True)
    
    # Vaccinations
    ax[2].plot(df['date'], df['total_vaccinations'], color='green')
    ax[2].set_title('Total Vaccinations')
    ax[2].grid(True)
    
    # Hospitalization data if enabled
    if show_hosp and 'hosp_patients' in df.columns:
        ax[3].plot(df['date'], df['hosp_patients'], color='purple')
        ax[3].set_title('Hospital Patients')
        ax[3].grid(True)
        
        ax[4].plot(df['date'], df['icu_patients'], color='orange')
        ax[4].set_title('ICU Patients')
        ax[4].grid(True)
    
    plt.tight_layout()
    st.pyplot(fig)
else:
    st.warning("Please select a date range")