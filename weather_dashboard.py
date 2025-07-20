import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# ✅ Your working OpenWeatherMap API key
API_KEY = "c98291c71bffbfc12eb16041de0dcee0"
CITY = "Mumbai"

# ✅ Construct the API URL
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# ✅ Make the API request
try:
    response = requests.get(URL)
    data = response.json()
except Exception as e:
    print("Request failed:", e)
    exit()

# ✅ Check if API returned data correctly
if "list" not in data:
    print("API Error:", data.get("message", "Unknown error"))
    exit()

# ✅ Extract temperature and date info
dates = []
temps = []

for item in data["list"]:
    try:
        date = datetime.datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
        temp = item["main"]["temp"]
        dates.append(date)
        temps.append(temp)
    except KeyError as e:
        print(f"Skipping malformed entry: {e}")
        continue

# ✅ Plot the data
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")
sns.lineplot(x=dates, y=temps, marker="o", color="blue")
plt.title(f"5-Day Weather Forecast for {CITY}", fontsize=16)
plt.xlabel("Date & Time", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
