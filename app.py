from flask import Flask,render_template,request
import pickle
import numpy as np

# model=pickle.load(open("model.pkl","rb"))

app = Flask(__name__)

@app.route("/")
def index():
    return "hELLO WORLD"

if __name__=="__main__":
    app.run(debug=True)