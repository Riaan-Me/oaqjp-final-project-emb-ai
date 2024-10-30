'''Program to Test Emotion. v0.9; Date: ...'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    ''' Does Emotion Detection Work '''
    emotion_text = request.args.get('textToAnalyze')
    json_response = emotion_detector(emotion_text)

    if json_response['dominant_emotion'] is not None:
        return f"For the given statement, the system response is 'anger': {json_response['anger']},\
         'disgust': {json_response['disgust']}, 'fear': {json_response['fear']}, \
        'joy': {json_response['joy']}, 'sadness': {json_response['sadness']}. \
        The dominant emotion is <b>{json_response['dominant_emotion']}.</b>"

    if json_response['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"

    return None

@app.route("/")
def render_index_page():
    ''' Display the Template '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
