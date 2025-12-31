"""
This module performs code for developing flask app
"""

from flask import Flask, request, render_template, jsonify
from SentimentAnalysis.sentiment import sentiment_analyzer

app = Flask(__name__)

@app.route("/")
def index():
    """ function for home page """

    return render_template("index.html")

@app.route("/analyze", methods = ["POST"])
def analyze():
    """ function to submit the text """

    try:
        data = request.get_json()

        if not data or "text" not in data :
            return jsonify({"error": "No text provided"}), 400

        text = data.get("text").strip()
        if text == "":
            return jsonify({"error": "Empty text is not allowed"})

        result = sentiment_analyzer(text)

        return jsonify({
            "text": text,
            "sentiment": result["sentiment"],
            "confidence": result["confidence"],
            "score": result["score"]
        })

    except Exception as e:      # pylint: disable=broad-exception-caught
        return jsonify({"error": "Internal server error",
                       "message": str(e)}), 500

if __name__ == "__main__" :
    app.run(debug="True")
