from flask import Flask, render_template, request
from services.movie_service import get_movie_details
from services.weather_service import get_weather
from services.webhook_service import send_to_webhook

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
                "weather": weather,
            }
            
            # Send data to webhook and log success
            response_code = send_to_webhook(result)
            print(f"Data sent to webhook successfully. Response Code: {response_code}")
        
        except ValueError as e:
            result = {"error": str(e)}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
