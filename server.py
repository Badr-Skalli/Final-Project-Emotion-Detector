''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def detect_emotion():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using EmotionPredict()
        function. The output returned is a dictionary of every emotion
        and its predicted score, as well as the dominant emotion based
        on the prediction scores.
    '''
    statement = request.args.get("textToAnalyze")
    emotions = emotion_detector(statement)

    if emotions["dominant_emotion"] is None:
        return "<b>Invalid text! Please try again!</b>"

    output = "For the given statement, the system response is "
    for index, (key, value) in enumerate(emotions.items()):
        if index < len(emotions) - 2:
            output += f"'{key}': {value}, "
        elif index == len(emotions) - 2 :
            output = output[:-2] + f" and '{key}': {value}. "
        elif index == len(emotions) - 1 :
            output += f"The dominant emotion is <b>{value}.</b>"
    return output

@app.route('/')
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost", port="5000")
