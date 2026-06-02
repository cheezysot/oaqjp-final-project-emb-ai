"""
This module creates a server instance using emotion_detection.py.
"""
from flask import Flask, request, render_template
from .emotion_detection import emotion_detector

#Defines Flask app.
app = Flask(__name__)


@app.route("/emotionDetection")
def emotion_detection():
    """Defines app route and emotion_detection function"""
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    #If Statement returns appropriate string if response is empty.
    if response is None:
        return "Invalid text! Please try again."

    #Returns response if a valid input is given for the function.
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
 # defines webpage rendering properties.
@app.route("/")
def render_index_page():
    """Render the app home page."""
    return render_template("index.html")


#Defines server port to run application on
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
