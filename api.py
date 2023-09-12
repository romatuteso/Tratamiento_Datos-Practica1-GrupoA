from flask import Flask
from yahoo_data_fetcher import get_price


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/api/<ticker>")
def api(ticker):
    return get_price("ticker")


@app.route("/api/multiple/")
def api_multiple():
    tickers = request.args.get("ticker")
    tickers = tickers.split(',')

    result =[]
    for t in tickers:
        result.append(get_price(t))
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
