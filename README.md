News API Data Pipeline
Overview

This project is an automated data pipeline that extracts real-time news data from an external API, processes and cleans the data using Python, and prepares it for analysis and visualization. It follows a standard ETL (Extract, Transform, Load) workflow commonly used in data engineering systems.

Features
Fetches real-time news data from an API
Cleans and transforms raw data using Python and Pandas
Handles API errors and missing data gracefully
Modular pipeline structure for scalability
Can be extended for scheduling and automation
Ready for integration with Power BI or other visualization tools
Project Architecture

News API
→ Extract data using Python requests
→ Transform and clean data using Pandas
→ Load processed data into file or database
→ Use data for analytics and dashboards

Tech Stack
Python
Pandas
Requests
dotenv
Git and GitHub
Project Structure

News API Pipeline
extract.py (fetches data from API)
transform.py (cleans and processes data)
load.py (stores processed data)
pipeline.py (main script to run full workflow)
.env (stores API key)
requirements.txt (dependencies)
README.md

How to Run the Project

Step 1: Clone the repository
git clone https://github.com/Suhani246/news-api-data-pipeline.git

cd news-api-data-pipeline

Step 2: Create virtual environment
python -m venv venv
venv\Scripts\activate

Step 3: Install dependencies
pip install -r requirements.txt

Step 4: Add API key
Create a .env file and add
API_KEY=your_api_key_here

Step 5: Run the pipeline
python pipeline.py

Output
Clean structured dataset from news API
Processed data ready for analytics
Can be used for dashboards and reporting
Error Handling
Handles API request failures
Manages missing or null data
Ensures safe execution of pipeline steps
Future Improvements
Power BI dashboard integration
Database storage using MySQL 
Multi-source news data integration


Author
Suhani Avadia
Master’s in Applied Computing
Focus: Data Analytics and Data Engineering
