from flask import Flask, render_template, request
from pnl import compute_pnl

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        strategy = request.form.get('strategy')
        sql_database = request.form.get('sql_database')

        try:
            result = compute_pnl(strategy, sql_database)
        except Exception as e:
            error = str(e)

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
