import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
from nlp.speech_classifier import CommentClassifier


class CommentClassifierServer:
    def __init__(self):
        self.tc = CommentClassifier()
        self.tc.fit()


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

tc_server = CommentClassifierServer()


@app.route('/')
@cross_origin()
def root():
    return 'Hello world!'


@app.route('/block-hate-speech', methods=['POST'])
@cross_origin()
def classify_tweet():
    request_data = request.get_json()
    youtube_comment = None
    prediction = None


if __name__ == '__main__':
    app.run()
