# news-api-data-pipeline
End-to-end data pipeline that extracts news from an API, processes it using Pandas, and stores it in MySQL with automated scheduling.

Overview

This project is an automated data pipeline that fetches real-time news data from an external API, processes and cleans the data using Python, and prepares it for downstream analytics and visualization. It simulates a real-world ETL (Extract, Transform, Load) workflow commonly used in data engineering and analytics systems.

Key Features

Automated extraction of real-time news data from API
Data cleaning and transformation using Pandas
Robust error handling for API failures and missing data
Scheduled execution support for continuous data updates
Structured pipeline design (modular ETL workflow)
Ready for analytics and dashboard integration (Power BI / Tableau)

Project Architecture

News API
   ↓
Extract (API Request - Python Requests)
   ↓
Transform (Pandas Data Cleaning & Formatting)
   ↓
Load (CSV / Database-ready output)
   ↓
Analytics / Visualization (Power BI - upcoming)


Tech Stack

Python 
Pandas 
Requests 
Dotenv 
Git & GitHub 

📂 Project Structure

News API Pipeline/
│
├── extract.py        # Fetches data from News API
├── transform.py      # Cleans and processes raw data
├── load.py           # Stores processed data
├── pipeline.py       # Main pipeline execution file
├── .env              # API keys (not pushed to GitHub)
├── requirements.txt  # Dependencies
└── README.md

How to Run This Project

1. Clone the repository
git clone https://github.com/Suhani246/news-api-data-pipeline.git
cd news-api-data-pipeline

2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt

4.Add environment variables
Create a .env file:
API_KEY=your_api_key_here

5. Run the pipeline
python pipeline.py

Output

Cleaned and structured news dataset
Ready for analytics, dashboards, or storage systems
Can be extended for Power BI or database integration

Error Handling

The pipeline includes:
API timeout handling
Missing or null data checks
Safe transformation steps to prevent crashes
Future Improvements
Power BI dashboard integration
Database storage (MySQL)
Advanced scheduling with Airflow or Cron jobs
Cloud deployment (AWS / Azure)
Multi-source news aggregation

Author

Suhani Avadia
Master’s in Applied Computing
Focused on Data Analytics & Data Engineering
