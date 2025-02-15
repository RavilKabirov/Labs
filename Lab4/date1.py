from datetime import datetime, timedelta



new_date = datetime.now() - timedelta(days=5)

print(new_date.strftime("%x"))
