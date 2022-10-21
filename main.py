import os
from flask import Flask, render_template, request
import model

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        x1 = request.form['x1']
        x2 = request.form['x2']
        x3 = request.form['x3']
        x4 = request.form['x4']
        pred = model.prediction(x1, x2, x3, x4)
        print("The Elasticity of the product is",pred)

    return render_template("index.html")


if __name__ == "__main__":
    #app.run(debug=True)
    host='0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port,debug=True)
