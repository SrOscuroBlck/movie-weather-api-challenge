from datetime import datetime
import requests

def get_weather(lat, lon, date):
    """
    Fetches weather data for a given latitude, longitude, and date.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        date (str): Date for which weather data is needed (format: 'YYYY-MM-DD').
    
    Returns:
        dict: A dictionary containing weather data:
              - min_temp (float): Minimum temperature on the given date.
              - max_temp (float): Maximum temperature on the given date.
              - summary (str): A human-readable weather summary.
    
    Raises:
        ValueError: If weather data is not available for the given date or the date exceeds the past 92 days.
    """
    release_date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.utcnow()
    delta_days = (today - release_date).days

    if delta_days > 92:
        raise ValueError("Weather data is only available for the past 92 days.")

    # Construct the Open-Meteo API URL
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&daily=temperature_2m_max,temperature_2m_min"
        f"&past_days={delta_days}"
        f"&timezone=auto"
    )

    # Request weather data
    response = requests.get(url)
    response.raise_for_status()
    daily_data = response.json().get("daily", {})

    if not daily_data or "temperature_2m_min" not in daily_data or "temperature_2m_max" not in daily_data:
        raise ValueError("Weather data not available for the given date.")

    # Extract and summarize weather data
    min_temp = daily_data["temperature_2m_min"][0]
    max_temp = daily_data["temperature_2m_max"][0]
    weather_summary = f"Temperatures ranging from {min_temp}°C to {max_temp}°C."

    return {
        "min_temp": min_temp,
        "max_temp": max_temp,
        "summary": weather_summary,
    }
