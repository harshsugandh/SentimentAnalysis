import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
vect = pickle.load(open('vect.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    my_test = pd.DataFrame([request.form.values()])
    my_test.columns = ["comment"]
    t = my_test["comment"]
    my_test_p = vect.transform(t)
    prediction = model.predict(my_test_p)

    output = prediction[0]

    return render_template('index.html', prediction_text='Sentiment score is {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)