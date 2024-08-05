"""
A Flask web application for emotion detection in text.

This module sets up the Flask application, defines routes for analyzing emotions in text,
and renders the index page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze the emotions in the provided text and return the results.

    Returns:
        str: A string describing the emotion scores and the dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    highest_emotion = response['dominant_emotion']

    if highest_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {anger_score}, "
        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} "
        f"and 'sadness': {sadness_score}. The dominant emotion is {highest_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Render the index page.

    Returns:
        str: The rendered HTML of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
