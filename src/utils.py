from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def generate_date_list():
    today = datetime.today()
    start_date = today - timedelta(days=1)
    end_date = today - relativedelta(months=1)

    date_list = [(start_date - timedelta(days=i)).strftime('%Y-%m-%d') for i in range((start_date - end_date).days + 1)]
    
    return date_list