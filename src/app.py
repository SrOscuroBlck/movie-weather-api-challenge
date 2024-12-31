from flask import Flask, render_template, request, jsonify
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
        JSON: Combined movie and weather data if a POST request is made.
        HTML: The main page if a GET request is made.
    """
    if request.method == "POST":
        title = request.form["title"]
        
        try:
            # Fetch movie data
            movie = get_movie_details(title)
            release_date = movie["release_date"]

            # Fetch weather data for Cali, Colombia
            weather = get_weather(lat=3.4372, lon=-76.5225, date=release_date)

            # Combine movie and weather data
            combined_data = {
                "title": movie["title"],
                "genres": movie["genres"],
                "release_date": release_date,
                "weather": weather,
                "overview": movie["overview"],
            }
            
            # Send data to webhook and log success
            response_code = send_to_webhook(combined_data)
            print(f"Data sent to webhook successfully. Response Code: {response_code}")
            
            return jsonify(combined_data)
        
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
