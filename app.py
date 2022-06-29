import json

import pandas as pd
import plotly
import plotly.express as px
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = pd.read_csv("bmw.csv")
    fig = px.scatter(data, x="price", y="mileage")
    plotly_figure = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", plotly_figure=plotly_figure)


if __name__ == "__main__":
    app.run()
