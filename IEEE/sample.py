from flask import Flask, render_template, request
import pandas as pd
import pickle as p
app=Flask(__name__,template_folder="templates")
a=p.load(open("classifier1.pkl","rb"))
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict",methods=["POST"])
def predict():
    features =[int(x) for x in request.form.values()]
    data=pd.DataFrame(features)
    output=classifier1.predict(data)
    return render_template("index.html",prediction_text="Fertilizer Suggestion {}".format(output))
if __name__ =="__main__":
    app.run(debug=True)