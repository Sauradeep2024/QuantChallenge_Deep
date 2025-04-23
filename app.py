from flask import Flask, render_template, request
from pnl import compute_pnl

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        selected_option = request.form.get('strategy_select')
        custom_strategy = request.form.get('custom_strategy', '').strip()
        sql_database = request.form.get('sql_database')

        strategy = custom_strategy if selected_option == 'custom' and custom_strategy else selected_option

        try:
            result = compute_pnl(strategy, sql_database)
        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
    