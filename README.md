# Automated AWS Resource Tracker

A modular Python automation pipeline that audits active AWS resources (EC2 instances and S3 buckets), exports an inventory report to CSV, and publishes notifications via AWS SNS.

## 🎯 Problem Statement & Solution
In cloud environments, engineering teams frequently spin up virtual servers (EC2) and storage buckets (S3) for testing and forget to decommission them, leading to unnecessary cloud spend. Manually checking dashboards across services does not scale.

This project automates resource auditing in a decoupled, zero-cost local lab using **`boto3`** (AWS SDK) and **`moto`** (in-memory AWS emulator), allowing the entire workflow to be built and tested without incurring cloud charges.

## 🏗️ Architecture
- `tracker.py` — Queries active EC2 instances and S3 buckets via `boto3` (simulated with `moto`).
- `report.py` — Formats and exports the resource inventory to `aws_report.csv`.
- `alert.py` — Reads `aws_report.csv` (with `FileNotFoundError` handling) and publishes a summary alert to an AWS SNS topic.
- `main.py` — Orchestrates the end-to-end scan, report generation, and notification pipeline.

## ⚡ Quick Start
```bash
# 1. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the full pipeline
python main.py


## 🚀 Future Enhancements
- **Scheduled Execution:** Trigger `main.py` automatically on a daily schedule using Linux `cron`, AWS EventBridge, or GitHub Actions.
- **Tag-Based Auto-Remediation:** Filter EC2 instances by `Environment=Dev` tags and automatically stop idle servers outside working hours to reduce cloud spend.
- **ChatOps Integration:** Forward alert summaries directly to a team Slack or Discord channel using incoming webhooks.
- **Multi-Region Scanning:** Expand `tracker.py` to loop through multiple AWS regions instead of scanning a single region.