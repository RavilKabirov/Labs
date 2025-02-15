from datetime import datetime, timedelta
x = datetime(2025, 12, 23, 11, 23, 52)
y = datetime(2025, 11, 7, 2, 32, 3)
z = x - y
print(z.seconds)
