from datetime import datetime, timedelta

def n_days_ago(n):
    return datetime.now() - timedelta(days=n)
