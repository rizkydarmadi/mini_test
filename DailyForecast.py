import requests
from datetime import datetime
from collections import defaultdict

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast",
    params={
        "lat": -6.17,
        "lon": 106.82,
        "appid": "a470aa7faa24d5307a07201cc4299954",
        "units": "metric",
    },
)

raw_data = []
for i in response.json()["list"]:
    date = datetime.fromtimestamp(i["dt"])
    raw_data.append({"date": date, "temp": i["main"]["temp"]})

daily_data = defaultdict(list)
for iterate in raw_data:
    date_obj: datetime = iterate["date"]
    temp = iterate["temp"]

    # Store temperature for the specific date
    daily_data[date_obj.date()].append(temp)

# Calculate the average temperature per day
average_temps = []
for date, temps in daily_data.items():
    avg_temp = sum(temps) / len(temps)
    average_temps.append({"date": date.strftime("%a, %d %b %Y"), "avg_temp": avg_temp})

# Print the results in the desired format
print("Weather Forecast: ")
for iterate in average_temps:
    formatted_date = iterate["date"]
    avg_temp = iterate["avg_temp"]
    print(f"{formatted_date}: {avg_temp:.2f}°C")
