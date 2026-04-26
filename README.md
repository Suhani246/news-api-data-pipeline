# News API Data Pipeline

## Overview
This project is an automated data pipeline that extracts real-time news data from an external API, processes and cleans the data using Python, and prepares it for analysis and visualization. It follows a standard ETL (Extract, Transform, Load) workflow used in data engineering.

---

## Features
- Fetches real-time news data from an API
- Cleans and transforms raw data using Python and Pandas
- Handles API errors and missing data
- Modular ETL pipeline design
- Ready for analytics and dashboard integration

---

## Project Architecture

News API  
→ Extract (Python Requests)  
→ Transform (Pandas)  
→ Load (CSV / Database)  
→ Analytics / Visualization  

---

## Tech Stack
- Python
- Pandas
- Requests
- python-dotenv
- Git and GitHub

---

## Project Structure

news-api-data-pipeline/
- extract.py
- transform.py
- load.py
- pipeline.py
- requirements.txt
- .env
- README.md

---

## How to Run the Project

### 1. Clone the repository
git clone https://github.com/Suhani246/news-api-data-pipeline.git  
cd news-api-data-pipeline  

### 2. Create virtual environment
python -m venv venv  
venv\Scripts\activate  

### 3. Install dependencies
pip install -r requirements.txt  

### 4. Add API Key
Create a .env file and add:  
API_KEY=your_api_key_here  

### 5. Run the pipeline
python pipeline.py  

---

## Output
- Clean structured dataset from news API
- Data ready for analysis and dashboards

---

## Error Handling
- Handles API request failures
- Manages missing or null data
- Ensures stable pipeline execution

---

## Future Improvements
- Power BI dashboard integration
- Database storage (MySQL/ PostgreSQL)
- Pipeline scheduling (Airflow / Cron)
- Multi-source news aggregation

---

## Author
Suhani Avadia  
Master’s in Applied Computing  
Focus: Data Analytics and Data Engineering
