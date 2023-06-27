from flask import Flask, render_template, url_for, request, redirect, session
import joblib

import os
import re
from newsapi import NewsApiClient

app = Flask(__name__)

model = joblib.load("C:/Users/Deepika/PycharmProjects/pythonProject/model_joblib.pkl")


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/')
def predict():
    if request.methods == 'POST':
        newsline = request.form["newheadline"]
        pred = [newsline]
        output = model.predict(pred)
        print(output)
        if output == ['positive']:
            return render_template('index.html', output='upward movement in gold price')
        if output == ['negative']:
            return render_template('index.html', output='downward movement in gold price')
        if output == ['neutral']:
            return render_template('index.html', output='steady movement in gold price')
        if output == ['none']:
            return render_template('index.html', output='this news headline is not related to gold news')
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
