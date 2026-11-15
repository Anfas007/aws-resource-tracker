import csv
from tracker import get_resources

def save_to_csv(filename="aws_report.csv"):
    data = get_resources()

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Service", "Resource_ID_or_Name", "Status"])
        writer.writerows(data)

    print(f"Saved {len(data)} resources to {filename}")

if __name__ == "__main__":
    save_to_csv()