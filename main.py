from report import save_to_csv
from alert import send_sns_alert

def run_pipeline():
    print("Starting AWS Resource Tracker pipeline...")
    save_to_csv()
    send_sns_alert()
    print("Pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()