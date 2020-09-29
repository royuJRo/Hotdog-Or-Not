from flask import Flask, render_template

import classifier.classifier

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World !</h1>'


if __name__ == '__main__':
    try:
        detector = classifier.Classifier()
        detector.load_model()
    except NotImplementedError:
        print("core is not implemented")
    app.run()
