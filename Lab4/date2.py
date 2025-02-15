from datetime import datetime, timedelta
x = datetime.now()
t = timedelta(days=1)
y = x - t
z = x + t
print(x, y, z)