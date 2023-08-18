from azure.identity import DefaultAzureCredential
from azure.monitor.query import MetricsQueryClient
from datetime import timedelta
import sys

credential = DefaultAzureCredential()
metrics_client = MetricsQueryClient(credential, endpoint="https://management.azure.com/{subscription}/providers/Microsoft.Insights/metrics?timespan=timedelta(hours=24)&api-version=2018-01-01")

sys.stdout.write(metrics_client)
sys.stdout.flush()