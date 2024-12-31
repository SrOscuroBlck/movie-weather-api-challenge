# Movie & Weather API Integration

## Project Overview
This application integrates two APIs to fetch and combine movie data with weather information. It provides a simple interface to search for a movie, displays details including its release date, genre(s), and combines this data with the weather conditions (min and max temperatures) on the release date for a specific location. The result is displayed and sent to a webhook for further processing.

---

## Features
- Search for a movie by title.
- Retrieve movie details (title, genre(s), release date, overview).
- Fetch weather data for the movie's release date.
- Combine and display movie and weather data.
- Send combined data to a webhook endpoint.

---

## Requirements
### APIs Used:
1. **Movie Database API** ([API Reference](https://developers.themoviedb.org/3/getting-started/introduction))
   - Requires an API token (free account needed).

2. **Open-Meteo API** ([API Reference](https://open-meteo.com/en/docs))
   - Free to use, no API key required.

### Additional Requirements:
- **Webhook URL:** Data is sent to this endpoint: `https://eo9m0nh4z7lacho.m.pipedream.net`.
- **Environment:** Python environment with Flask and other dependencies.

---

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie-weather-api-challenge.git
   cd movie-weather-api-challenge
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Create a `.env` file in the project root:
     ```plaintext
     TMDB_API_TOKEN=your_api_token
     ```

5. Run the application:
   ```bash
   python src/app.py
   ```

---

## Usage
1. Open the app in your browser:
   - Visit `http://127.0.0.1:5000`.

2. Search for a movie by entering its title in the form and submitting it.

3. View the combined movie and weather data.

4. The combined data will also be sent to the webhook.

---

## Project Structure
```plaintext
movie-weather-api-challenge/
├── src/
│   ├── app.py              # Main Flask application
│   ├── services/           # Service modules for API integrations
│   │   ├── movie_service.py
│   │   ├── weather_service.py
│   │   ├── webhook_service.py
│   ├── templates/          # HTML templates
│   │   └── index.html
├── .gitignore
├── .env.example            # Example for environment variables (your own .env file should be created)
├── README.md
├── requirements.txt        # Project dependencies
```

---

## Testing
- To test the application locally, follow the installation instructions.

---

## Contribution
Feel free to fork the repository and submit a pull request for improvements.
