# main.py
import argparse
import requests
import json

def get_weather(api_key, city):
    """
    Retrieves the current weather for a given city.

    Args:
    api_key (str): The API key for OpenWeatherMap.
    city (str): The name of the city to retrieve the weather for.

    Returns:
    dict: A dictionary containing the current weather information.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def parse_weather(weather_data):
    """
    Parses the weather data into a user-friendly format.

    Args:
    weather_data (dict): A dictionary containing the weather information.

    Returns:
    str: A string containing the parsed weather information.
    """
    if weather_data is None:
        return "Error: Unable to retrieve weather data."
    city = weather_data["name"]
    description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    return f"Weather in {city}:\nDescription: {description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"

def main():
    """
    The main entry point of the program.
    """
    parser = argparse.ArgumentParser(description="A simple weather CLI tool.")
    parser.add_argument("-k", "--api_key", required=True, help="The API key for OpenWeatherMap.")
    parser.add_argument("-c", "--city", required=True, help="The name of the city to retrieve the weather for.")
    args = parser.parse_args()
    weather_data = get_weather(args.api_key, args.city)
    print(parse_weather(weather_data))

if __name__ == "__main__":
    main()