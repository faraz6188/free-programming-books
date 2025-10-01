# air_logger.py
# API: OpenAQ (open licence)
import requests, datetime, csv

city = "Berlin"
url  = f"https://api.openaq.org/v2/measurements?city={city}&parameter=pm25"
data = requests.get(url, timeout=10).json()["results"][0]
row  = [datetime.datetime.utcnow().isoformat(), city, data["value"]]

with open("air.csv", "a", newline="") as f:
    csv.writer(f).writerow(row)
print(row, "saved")
