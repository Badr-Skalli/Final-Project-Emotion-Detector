from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def detect_emotion():
    statement = request.args.get("textToAnalyze")
    emotions = emotion_detector(statement)

    if (emotions["dominant_emotion"] == None):
        return "<b>Invalid text! Please try again!</b>"

    output = "For the given statement, the system response is "
    for index, (key, value) in enumerate(emotions.items()):
        if (index < len(emotions) - 2):
            output += f"'{key}': {value}, "
        elif(index == len(emotions) - 2 ):
            output = output[:-2] + f" and '{key}': {value}. "
        elif(index == len(emotions) - 1 ):
            output += f"The dominant emotion is <b>{value}.</b>"
    return output

@app.route('/')
def render_index_page():
    return render_template('index.html')

if (__name__ == '__main__'):
    app.run(host="localhost", port="5000")
