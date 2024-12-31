from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form["title"]
        
        # Fetching and WebHook code goes here
        
        return jsonify({"title": title})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
