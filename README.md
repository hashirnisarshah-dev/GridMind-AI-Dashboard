# ⚡ GridMind AI – Electricity Consumption Analysis Dashboard

### AI-Powered Electricity Consumption Analysis and Demand Forecasting
https://gridmind-ai-dashboard-7zp698cvaqsh5rthu2xrym.streamlit.app/?utm_source=chatgpt.com
## 📌 Project Overview

GridMind AI is a data science project designed to analyze electricity consumption patterns across six cities in Pakistan. It provides an interactive dashboard for exploring electricity usage, comparing cities, and understanding hourly and monthly consumption trends.

## 🎯 Project Objectives

- Analyze electricity consumption patterns.
- Compare electricity usage across different cities.
- Identify hourly, monthly, and seasonal trends.
- Explore household electricity consumption.
- Support data-driven energy management decisions.

## 📊 Dataset

The project uses an hourly electricity consumption dataset containing approximately:

- **Records:** 502,811
- **Columns:** 61
- **Cities:** 6
- **Households:** 59

Cities included:
- Islamabad
- Karachi
- Lahore
- Multan
- Peshawar
- Skardu

Main dataset fields include city, household number, datetime, usage_kw, and household characteristics.

## 🚀 Dashboard Features

- Interactive city filter
- Electricity consumption KPIs
- City-wise consumption comparison
- Hourly electricity usage analysis
- Monthly consumption trends
- Interactive Plotly visualizations

## 🛠️ Technologies Used

- Python
- Pandas
- Streamlit
- Plotly
- Scikit-learn
- Google Colab

## 📂 Project Structure

```text
GridMind-AI-Dashboard/
│
├── app.py
├── requirements.txt
├── README.md
└── gridmind_hourly.parquet
```

## ⚙️ Installation and Usage

1. Clone this repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Open the project folder.

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Place the dataset in the project folder and configure the dataset path in `app.py`.

5. Run the dashboard:

```bash
streamlit run app.py
```

## 🌍 Project Scope

GridMind AI is an academic and portfolio data science project. Its analysis is based on the available household-level dataset and does not represent a live national electricity grid monitoring system.

## 👨‍💻 Project Developer

**Hashir Nisar**

Data Science Student  
City University of Science and Information Technology (CUSIT), Peshawar

---

*GridMind AI – Turning Electricity Data into Meaningful Insights.*
