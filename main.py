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
        print(pred)
        my_pred = pred

    return render_template("index.html", A=my_pred)


if __name__ == "__main__":
    app.run(debug=True)
