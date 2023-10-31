from flask import Flask, render_template, request
app = Flask(__name__)
import pickle
import numpy as np

model= pickle.load(open('insurancepred.pkl','rb'))


@app.route('/')
def start():
    return render_template('index.html')

@app.route('/login',methods=['POST'])

def login():


    p=request.form["age"]

    q=request.form["se"]
    if(q=="f"):
        q=0
    else:
        q=1
    s=request.form["bmi"]

    r=request.form["s"]
    if(r=="ne"):
        r=0
    elif(r=="nw"):
        r=1
    elif(r=="se"):
        r=2
    else:
        r=3

    t=request.form["chi"]
    u=request.form["b"]
    if(u=="y"):
        u=1
    else:
        u=0

    w= [[float(p),float(q),float(r),float(s),float(t),float(u)]]
    output=model.predict(w)
    print(output)
    return render_template("index.html",y="The predicted Insurance charge is    " +str(np.round(output[0])))

if __name__ == '__main__' :
    app.run(debug=True)