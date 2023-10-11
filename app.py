from flask import Flask, render_template, request

app = Flask(__name)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_pin', methods=['POST'])
def check_pin():
    pin = request.form['pin']
    if pin == "1234":
        return "Transaction Options"
    else:
        return "Wrong PIN number"

@app.route('/withdraw', methods=['POST'])
def withdraw():
    return "Withdraw Form"

@app.route('/perform_withdraw', methods=['POST'])
def perform_withdraw():
    withdraw_amount = int(request.form['withdraw-amount'])
    m = 25000
    if withdraw_amount <= m and withdraw_amount % 100 == 0:
        return f"Please take your amount: ${withdraw_amount}"
    else:
        return "Invalid cash"

@app.route('/balance_enquiry', methods=['POST'])
def balance_enquiry():
    m = 25000
    return f"Your available amount: ${m}"

@app.route('/fast_cash', methods=['POST'])
def fast_cash():
    return "Fast Cash Options"

@app.route('/perform_fast_cash', methods=['POST'])
def perform_fast_cash():
    fast_cash_option = int(request.form['fast-cash-option'])
    m = 25000
    if fast_cash_option == 1 and 5000 <= m:
        return "Please take cash: $5000"
    elif fast_cash_option == 2 and 10000 <= m:
        return "Please take cash: $10000"
    elif fast_cash_option == 3 and 15000 <= m:
        return "Please take cash: $15000"
    elif fast_cash_option == 4 and 20000 <= m:
        return "Please take cash: $20000"
    else:
        return "Invalid fast cash option"

if __name__ == '__main__':
    app.run(debug=True)

