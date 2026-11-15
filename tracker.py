import boto3
from moto import mock_aws

@mock_aws
def get_resources():
    # 1. Connect to simulated EC2 and S3 in Mumbai region
    ec2 = boto3.client("ec2", region_name="ap-south-1")
    s3 = boto3.client("s3", region_name="ap-south-1")

    # 2. Simulate creating 2 servers and 1 storage bucket
    ec2.run_instances(ImageId="ami-12345678", MinCount=2, MaxCount=2)
    s3.create_bucket(
        Bucket="company-dev-logs-2026",
        CreateBucketConfiguration={"LocationConstraint": "ap-south-1"}
    )

    resources = []
    reservations = ec2.describe_instances()["Reservations"]
    for res in reservations:
        for instance in res["Instances"]:
            resources.append(
                ("EC2", instance["InstanceId"], instance["State"]["Name"])
            )

    buckets = s3.list_buckets()["Buckets"]
    for bucket in buckets:
        resources.append(("S3", bucket["Name"], "available"))

    return resources