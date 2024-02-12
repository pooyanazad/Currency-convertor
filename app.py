from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

API_KEY = '55555555555555555555555' #insert your real api 
API_URL = 'https://v6.exchangerate-api.com/v6/{}/latest/'.format(API_KEY)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currency Converter</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f3e5f5;
            color: #424242;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
        }
        .container {
            background-color: #e1bee7;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        h2 {
            color: #6a1b9a;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        input, select, button {
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
            outline: none;
        }
        button {
            background-color: #ab47bc;
            color: white;
            cursor: pointer;
            border: none;
        }
        button:hover {
            background-color: #9c27b0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Currency Converter</h2>
        <form method="POST">
            <input type="number" name="amount" placeholder="Amount" step="0.01" required>
            <select name="from_currency">
                <option value="USD">USD - US Dollar</option>
                <option value="EUR">EUR - Euro</option>
                <option value="GBP">GBP - British Pound</option>
                <option value="JPY">JPY - Japanese Yen</option>
                <option value="AUD">AUD - Australian Dollar</option>
                <option value="CAD">CAD - Canadian Dollar</option>
                <option value="CHF">CHF - Swiss Franc</option>
                <option value="CNY">CNY - Chinese Yuan</option>
                <option value="SEK">SEK - Swedish Krona</option>
                <option value="NZD">NZD - New Zealand Dollar</option>
            </select>
            <select name="to_currency">
                <option value="USD">USD - US Dollar</option>
                <option value="EUR">EUR - Euro</option>
                <option value="GBP">GBP - British Pound</option>
                <option value="JPY">JPY - Japanese Yen</option>
                <option value="AUD">AUD - Australian Dollar</option>
                <option value="CAD">CAD - Canadian Dollar</option>
                <option value="CHF">CHF - Swiss Franc</option>
                <option value="CNY">CNY - Chinese Yuan</option>
                <option value="SEK">SEK - Swedish Krona</option>
                <option value="NZD">NZD - New Zealand Dollar</option>
            </select>
            <button type="submit">Convert</button>
        </form>
        {% if conversion_result %}
            <div>
                <h3>Converted Amount:</h3>
                <p>{{ conversion_result }}</p>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""
@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    conversion_result = None
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        
        # Making an API request to get the conversion rate
        response = requests.get(f"{API_URL}{from_currency}")
        if response.status_code == 200:
            data = response.json()
            rate = data['conversion_rates'][to_currency]
            converted_amount = amount * rate
            conversion_result = f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
        else:
            conversion_result = "Error: Unable to fetch conversion rate."
        
    return render_template_string(HTML_TEMPLATE, conversion_result=conversion_result)

if __name__ == '__main__':
    app.run(debug=True)
