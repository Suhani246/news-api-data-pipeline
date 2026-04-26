from apscheduler.schedulers.blocking import BlockingScheduler
from pipeline import run_pipeline

scheduler = BlockingScheduler()

# Run every 1 hour 
scheduler.add_job(run_pipeline, 'interval', hours=1)

print("Scheduler running...")

# RUN ON START 
run_pipeline()

scheduler.start()