from flask import Flask

from .utils.jsondata import part_offers

app = Flask(__name__)

@app.route("/health")
def health_check():
    return "<p>OK</p>"
