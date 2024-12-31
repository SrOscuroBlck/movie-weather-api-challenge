import os
import sys

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request
from src.services.movie_service import get_movie_details
from src.services.weather_service import get_weather
from src.services.webhook_service import send_to_webhook

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handles the main route for the application. Allows users to search for a movie,
    fetches relevant movie details and associated weather data, and combines the results.
    
    Returns:
        Rendered HTML: Displays movie and weather details on the main page.
    """
    result = None
    if request.method == "POST":
        title = request.form["title"]
        
        try:
            # Fetch movie data
            movie = get_movie_details(title)
            release_date = movie["release_date"]

            # Fetch weather data for Cali, Colombia
            weather = get_weather(lat=3.4372, lon=-76.5225, date=release_date)

            # Combine movie and weather data
            result = {
                "title": movie["title"],
                "genres": movie["genres"],
                "release_date": release_date,
                "overview": movie["overview"],
                "min_temp": weather["min_temp"],
                "max_temp": weather["max_temp"],
                "weather_summary": weather["summary"],
            }
            
            # Send data to webhook and log success
            webhook_response = send_to_webhook(result)
            if isinstance(webhook_response, str) and webhook_response.startswith("Error"):
                result["webhook_error"] = webhook_response
            else:
                result["webhook_status"] = f"Data sent to webhook successfully. Response Code: {webhook_response}"
        
        except ValueError as e:
            result = {"error": str(e)}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Use the PORT environment variable or default to 5000
    app.run(host="0.0.0.0", port=port, debug=False)
