from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    # 1. Fetch live rates relative to USD
    url = "https://open.er-api.com/v6/latest/USD"
    
    try:
        response = requests.get(url)
        data = response.json() # Parse raw JSON string into Python dict
        
        # 2. Extract and format currency rates
        gbp_rate = round(data["rates"]["GBP"], 4)
        eur_rate = round(data["rates"]["EUR"], 4)
        jpy_rate = round(data["rates"]["JPY"], 2)
        
        market_data = {
            "gbp": gbp_rate,
            "eur": eur_rate,
            "jpy": jpy_rate,
            "status": "Live Data Connected"
        }
    except Exception as e:
        market_data = {
            "gbp": "N/A",
            "eur": "N/A",
            "jpy": "N/A",
            "status": f"Error: {e}"
        }

    return render_template("index.html", data=market_data)

if __name__ == "__main__":
    app.run(debug=True)