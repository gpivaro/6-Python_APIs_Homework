import json

with open("/etc/config.json") as config_file:
    config = json.load(config_file)

# OpenWeatherMap API Key
weather_api_key = config.get("OPENWEATHERMAP_API_KEY")

# Google API Key
g_key = config.get("GOOGLE_API_KEY")
